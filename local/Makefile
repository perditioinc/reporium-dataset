# Local OSS substrate for reporium-dataset.
# $0 / OSS / additive / local-only. Never touches production or cloud.

COMPOSE := docker compose -f docker-compose.yml

.PHONY: help up down seed smoke teardown logs

help:
	@echo "reporium-dataset local OSS substrate"
	@echo ""
	@echo "  make up        Start the api-stub (OSS reporium-api substitute), wait until healthy"
	@echo "  make seed      Show the seeded dataset the stub serves"
	@echo "  make smoke     Run the real generate.py against the local stub and assert the README"
	@echo "  make down      Stop and remove containers + volumes"
	@echo "  make teardown  Alias for down (full cleanup)"
	@echo "  make logs      Tail api-stub logs"

up:
	$(COMPOSE) up -d --wait api-stub

seed:
	@echo "Seeded dataset (local/seed/dataset.json):"
	@$(COMPOSE) run --rm --no-deps api-stub python -c "import json;d=json.load(open('/seed/dataset.json'));s=d['stats'];print('total_repos =',s['total_repos']);print('languages  =',list(s['languages'].keys()));print('repos      =',[r['owner']+'/'+r['name'] for r in d['repos']])"

smoke:
	$(COMPOSE) run --rm smoke

down:
	$(COMPOSE) down -v

teardown: down

logs:
	$(COMPOSE) logs -f api-stub
