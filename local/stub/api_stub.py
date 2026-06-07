"""Local OSS stub for reporium-api.

Zero-dependency stdlib HTTP server that emulates the two reporium-api endpoints
that generate.py actually consumes:

    GET /repos?sort=stars&limit=<n>&page=<n>   -> {"repos": [...], "page", "limit", "total"}
    GET /library?limit=1                        -> {"stats": {...}, ...}

Data is read from a seed JSON file (LOCAL_SEED env, default /seed/dataset.json)
so no production/cloud service is contacted. This is an env-pointed network
substitute: the real generate.py is run unmodified, with REPORIUM_API_URL
pointed at this server.
"""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

SEED_PATH = os.getenv("LOCAL_SEED", "/seed/dataset.json")
HOST = os.getenv("STUB_HOST", "0.0.0.0")
PORT = int(os.getenv("STUB_PORT", "8000"))


def _load_seed() -> dict:
    with open(SEED_PATH, encoding="utf-8") as f:
        return json.load(f)


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 (stdlib API)
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"
        query = parse_qs(parsed.query)

        try:
            seed = _load_seed()
        except Exception as exc:  # noqa: BLE001
            self._send_json(500, {"error": f"seed load failed: {exc}"})
            return

        repos = seed.get("repos", [])
        stats = seed.get("stats", {})

        if path == "/health":
            self._send_json(200, {"status": "ok", "repos": len(repos)})
            return

        if path == "/repos":
            # Mirror reporium-api: sort=stars, paginate by limit/page.
            sort = query.get("sort", [""])[0]
            limit = int(query.get("limit", ["200"])[0])
            page = int(query.get("page", ["1"])[0])

            ordered = list(repos)
            if sort == "stars":
                ordered.sort(key=lambda r: r.get("parent_stars") or 0, reverse=True)

            start = (page - 1) * limit
            batch = ordered[start : start + limit]
            self._send_json(
                200,
                {"repos": batch, "page": page, "limit": limit, "total": len(repos)},
            )
            return

        if path == "/library":
            self._send_json(
                200,
                {
                    "repos": [],
                    "stats": stats,
                    "categories": [],
                    "tag_metrics": [],
                    "total": stats.get("total_repos", len(repos)),
                    "page": 1,
                    "limit": int(query.get("limit", ["1"])[0]),
                },
            )
            return

        self._send_json(404, {"error": f"no such endpoint: {path}"})

    def log_message(self, fmt: str, *args) -> None:  # quieter logs
        print("[api-stub] " + (fmt % args))


def main() -> None:
    print(f"[api-stub] serving seed {SEED_PATH} on {HOST}:{PORT}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
