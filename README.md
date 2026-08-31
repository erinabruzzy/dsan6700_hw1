# mypkg

A package for doing great things!

## Installation

```bash
pip install mypkg
```

## Usage

- TODO

## Contributing

Clone and set up the repository with

```bash
git clone TODO && cd mypkg
pip install -e ".[dev]"
```

Install pre-commit hooks with

```bash
pre-commit install
```

Run tests using

```
pytest -v tests
```

---
**Personal Notes:**

1) Make sure your team shares one environment (via uv.lock) and that everyone
has the repository cloned with remote tracking set up. For now it is enough
to share the repo and push to it.

- Declare dependencies in pyproject.toml
- Then, generate uv.lock using the `uv sync --extra dev` command

2) Scaffold a package with the src/ layout. Use uv init (you may start from the course cookiecutter template) to create a project whose package lives under src/.

3) Write your pyproject.toml. Declare a build backend (e.g. hatchling), your runtime
dependencies, and a dev optional-dependency group for your tooling (ruff, pytest, mypy, pre-commit). Commit the generated uv.lock.

- This command creates a skeleton pyproject.toml: `uv init --package src/mypkg`
- Use this command to declare the libraries the service needs to run:
`uv add fastapi pydantic pydantic-settings uvicorn`
- Add development and quality-checking tools:
`uv add --dev ruff pytest mypy pre-commit httpx`

4) Stand up a small FastAPI service skeleton. Your app does not have to do anything
interesting yet, but it must be a real web service:

- a FastAPI application with at least a /health endpoint that returns a small typed
response and lets a caller (or a container, or a grader) confirm the service is up;
- at least one Pydantic request/response model so input is validated at the edge and
output is serialized predictably;
- a placeholder "predict"-style endpoint is welcome but optional this week.

`src/mypkg/main.py`

5)  Configure your application. Add typed configuration with Pydantic Settings:
the app reads its settings from the environment, with validators that fail fast
at startup on bad config (crash loudly, do not limp along). Provide paired example
environment files (for example a local-dev shape and a deployed shape) so a new
developer knows exactly which knobs exist. Never commit real secrets.

`src/mypkg/config.py`

6) Add quality checks:

- ruff for linting and formatting (run both)
- pytest with at least one meaningful test — for example, hitting your /health
endpoint with FastAPI's test client, or asserting that your settings validation
rejects a bad value. A test that asserts nothing does not count
- pre-commit with a Git hook that runs ruff (and whatever else you like) before
each commit, so low-quality code never enters the repository

7)  Incorporate GitHub Workflows. Add a GitHub Actions workflow at
.github/workflows/ci.yml that runs on every push and pull request and performs
each step:
- pick an operating system and install Python;
- check out the repository;
- install uv and run uv sync --extra dev --frozen;
- run uv run ruff check and uv run ruff format --check;
- run uv run mypy src/ (type-checking);
- run uv run pytest

8) Provide documentation. Write an informative README with clear, copy-pasteable
instructions for installing and running your service on a clean machine. The
Diátaxis framework offers sound advice on structuring technical documentation.
Add docstrings to your functions (autoDocstring can scaffold them).

- Downloaded autoDocstring Extension
