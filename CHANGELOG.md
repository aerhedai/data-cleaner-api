# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-07-23

### 🎉 Initial Release

#### Added
- ✅ Dockerfile for building and running the API in a containerised environment.
- ✅ `main.py` for FastAPI app instantiation and route registration.
- ✅ Modular folder structure:
  - `api/` – Contains route definitions.
  - `services/` – Business logic layer (example included).
  - `models/` – Pydantic schemas for request/response models.
  - `core/` – Pydantic config for setup.
  - `utils/` – Logger utility included.
  - `tests/` – Sample unit test structure.
- ✅ `logging.py` for basic application logging using the standard library.
- ✅ Example endpoint: `/example`.
- ✅ Swagger/OpenAPI support via FastAPI (`/docs` and `/redoc`).
- ✅ Requirements file for dependency management.
- ✅ Readme with full instructions and project overview.

## [1.0.1] - 2025-07-23

### Fixed
- 🐛 Added missing `httpx` dependency required for testing with `TestClient`.
- ✅ Ensured all test routes run successfully using `pytest`.


---

> Future versions will include enhancements like database support, authentication, advanced logging, environment-based configuration, and more.

