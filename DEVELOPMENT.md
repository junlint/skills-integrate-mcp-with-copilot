# Development / local run

This repository contains a small FastAPI app under `src/`. The following files have been added to make local development easier:

- `Dockerfile` - container image for running the FastAPI app
- `docker-compose.yml` - compose file to run the app locally on port 8000
- `Makefile` - convenience targets: `make build`, `make up`, `make down`, `make test`
- `requirements-dev.txt` - dev/test dependencies (pytest, requests)
- `tests/` - contains minimal pytest tests

Quick start (requires Docker):

1. Build and run using docker-compose:

   docker-compose up --build

2. Visit http://localhost:8000 in your browser (the UI is served under `/static/index.html`).

Running tests locally (without Docker):

1. Create a virtualenv and install dependencies:

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt -r requirements-dev.txt

2. Run tests:

   pytest -q

If you'd like, I can now create a branch, commit these changes, run the tests here, and push + open a PR. Tell me to continue and I'll do the git steps next.
