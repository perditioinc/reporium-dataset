# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.0.0] - 2026-03-17

### Added
- Initial release of reporium-dataset
- Nightly automated dataset generation via GitHub Actions
- `generate.py` for building curated AI/ML repo datasets
- Build counter for nightly versioning
- Security scanning workflow
- Reusable test failure workflow via perditio-devkit
- Test suite (`tests/test_generate.py`)

### Fixed
- Real metrics, live data sources, test and nightly badges
- Dataset fallback partitions fetch (all partitions now included)
- `asyncio` moved to top-level import to fix F401 lint failure
