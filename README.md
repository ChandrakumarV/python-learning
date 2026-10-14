> uv run python-learning

## Important `uv` Commands for Beginners

| Command                     | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| `uv --version`              | Check the installed `uv` version.                                  |
| `uv init my-project`        | Create a new Python project.                                       |
| `uv python list`            | List available Python versions.                                    |
| `uv python install 3.12`    | Install Python 3.12.                                               |
| `uv python pin 3.12`        | Set the Python version for the project.                            |
| `uv venv`                   | Create a virtual environment named `.venv`.                        |
| `uv add requests`           | Install a dependency and add it to `pyproject.toml`.               |
| `uv add sqlalchemy fastapi` | Install multiple dependencies.                                     |
| `uv add --dev pytest`       | Install a development dependency.                                  |
| `uv remove requests`        | Remove a dependency from the project.                              |
| `uv run main.py`            | Run a Python file using the project environment.                   |
| `uv run pytest`             | Run tests using the project environment.                           |
| `uv run python`             | Open the Python interactive shell.                                 |
| `uv sync`                   | Sync the environment with the project's dependencies and lockfile. |
| `uv lock`                   | Create or update `uv.lock`.                                        |
| `uv tree`                   | Display the dependency tree.                                       |
| `uv sync --locked`          | Sync dependencies without allowing the lockfile to change.         |

## `requirements.txt` Commands

| Command                                                              | Description                                                         |
| -------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `uv pip install -r requirements.txt`                                 | Install dependencies listed in `requirements.txt`.                  |
| `uv pip install requests`                                            | Install a package using uv's pip-compatible interface.              |
| `uv pip uninstall requests`                                          | Uninstall a package using uv's pip-compatible interface.            |
| `uv export --format requirements.txt --output-file requirements.txt` | Export project dependencies to `requirements.txt`.                  |
| `uv add -r requirements.txt`                                         | Add dependencies from an existing requirements file to the project. |

## Useful Environment Commands

| Command                 | Description                                     |
| ----------------------- | ----------------------------------------------- |
| `uv venv --python 3.12` | Create a virtual environment using Python 3.12. |
| `uv pip list`           | List installed packages.                        |
| `uv pip freeze`         | Display installed packages and their versions.  |
| `uv cache clean`        | Clear uv's cached files.                        |

Beginner tip: For a new project, the usual workflow is `uv init` → `uv add package-name` → `uv run main.py`. Use `pyproject.toml` and `uv.lock` to manage and reproduce dependencies.
