# Contributing

Contributions are welcome. Please follow the guidelines below.

## Setup

```bash
git clone https://github.com/your-username/imdb-wrapper.git
cd imdb-wrapper
pip install -e .
```

## Workflow

1. Fork the repo and create a branch from `main`
2. Make your changes
3. Test manually with `python main.py`
4. Commit with a meaningful message (e.g. `feat: add search by name`)
5. Open a pull request

## Commit Style

Use conventional commits:

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation only
- `chore:` tooling, config, dependencies
- `refactor:` code change with no behavior change

## Guidelines

- No external dependencies — stdlib only
- Keep dataclasses in `models.py`, queries in `queries.py`, HTTP logic in `client.py`
- This project is for **educational purposes only** — do not add features that facilitate commercial use of IMDb data

## Reporting Issues

Open a GitHub issue with a clear description and, if applicable, the IMDb title ID that caused the problem.
