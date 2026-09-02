# DSAN6700: Homework 1

A a clean, packaged, tested, CI-checked service skeleton managed with [`uv`](https://github.com/astral-sh/uv).

---

## Install/Run Guide

Here are copy-pasteable instructions for installing and running the service on a clean machine.

### 1. Prerequisites & Installation

Ensure you have `uv` installed on your machine. Clone the repository and install all dependencies (including development tools) directly from the lockfile:

```bash
# Clone the repository
git clone [https://github.com/erinabruzzy/dsan6700_hw1.git](https://github.com/erinabruzzy/dsan6700_hw1.git)
cd dsan6700_hw1

# Install dependencies deterministically from uv.lock
uv sync --extra dev --frozen
```

2. Environment Configuration
Copy the example environment configuration to create your local .env file:

`cp .env.example .env`

> Note: The application uses Pydantic Settings and will fail fast at startup if required environment variables (such as ENVIRONMENT) are missing.

3. Running the Service Locally

Start the local Uvicorn development server:

`uv run uvicorn mypkg.main:app --reload`

Once running, you can access the service endpoints in your browser or API client:

Health Check Endpoint: http://127.0.0.1:8000/health

Interactive OpenAPI Docs (Swagger UI): http://127.0.0.1:8000/docs

**Quality & Development Reference**

Execute all quality gates locally to ensure code meets repository standards before pushing:

```bash
# Run Ruff (Linting)
uv run ruff check .

# Run Ruff (Formatting Check)
uv run ruff format --check .

# Run MyPy (Type Checking)
uv run mypy src/

# Run Pytest (Unit Testing)
uv run pytest
```

**Git Pre-Commit Hooks**

Install local pre-commit hooks so linting and formatting run automatically before every commit:

`uv run pre-commit install`

**Continuous Integration (CI)**

A GitHub Actions workflow is configured at .github/workflows/ci.yml. On every push or pull request to the Main branch, CI executes:

```
uv sync --extra dev --frozen

uv run ruff check .

uv run ruff format --check .

uv run mypy src/

uv run pytest
```

---
**Personal Notes**

[x] 1. Shared Environment

Managed via uv.lock. Repository tracking configured on remote branch Main.

Commands: uv sync --extra dev

[x] 2. Package Layout

Package configured using src/ layout.

Command: uv init --package src/mypkg

[x] 3. Project Dependencies

Declared hatchling as build backend in pyproject.toml.

Runtime dependencies: uv add fastapi pydantic pydantic-settings uvicorn

Development tools: uv add --dev ruff pytest mypy pre-commit httpx

[x] 4. FastAPI Skeleton

Service implemented in src/mypkg/main.py.

Typed /health endpoint returning Pydantic models.

[x] 5. Application Config

Implemented fail-fast settings in src/mypkg/config.py using Pydantic Settings.

Paired example file provided (.env.example).

[x] 6. Quality Checks

Ruff: Configured for linting and formatting.

Pytest: Unit tests verifying /health response and settings fail-fast behavior.

Pre-commit: Git hooks configured in .pre-commit-config.yaml.

[x] 7. GitHub Actions Workflow

Workflow active at .github/workflows/ci.yml targeting Main.

Runs uv sync --extra dev --frozen, ruff check, ruff format, mypy src/, and pytest.

[x] 8. Technical Docs

Structured README with installation instructions.

Function docstrings scaffolded via autoDocstring extension.
