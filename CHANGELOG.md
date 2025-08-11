# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-08-11
### Added
- Initial release of **Data Cleaner API**.
- Implemented endpoint for cleaning datasets by:
  - Removing duplicate rows.
  - Handling missing values.
  - Standardising column names.
  - Correcting data types.
- Added support for multiple input formats:
  - CSV
  - Excel
  - Parquet
  - JSON
- Included flexible configuration options for cleaning parameters via API request body.
- Implemented robust error handling for invalid inputs and unsupported formats.
- Added Dockerfile for containerised deployment.
- Configured automated linting and formatting with **Black** and **Flake8**.
- Created initial project structure using the [Aerhed AI Python API Template](https://github.com/aerhedai/python-api-template).
- Added basic unit tests for core cleaning functions.
- Created example request and response payloads in API documentation.

## [1.0.1] - 2025-08-11
### Fixed
- Resolved pandas chained assignment warning related to inplace operations when filling missing values.
- Improved data cleaning function to avoid splicing issues by modifying DataFrame columns safely.
- Enhanced stability and correctness of missing value imputation logic.


### Documentation
- Added `README.md` with:
  - Installation instructions.
  - Usage examples.
  - API endpoint details.
  - Project structure.
- Added `CHANGELOG.md` for tracking future changes.
- Included `.env.example` file for environment configuration.
- Documented local development setup.

### DevOps
- Added `.dockerignore` and `.gitignore` for cleaner repository management.
- Configured `requirements.txt` with all necessary dependencies.
- Included `Makefile` for common development commands.
- Set up GitHub repository for version tracking and collaboration.
