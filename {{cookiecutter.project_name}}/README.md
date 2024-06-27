# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Prerequisites

- [poetry](https://python-poetry.org/): dependency and virtual environment management
- Coding style
  - [flake8](https://flake8.pycqa.org/en/latest/): check style, programming errors and complexity
  - [black](https://github.com/psf/black): auto format your code
  - [isort](https://pycqa.github.io/isort/): auto sort your package importing
- Test thought [pytest](https://docs.pytest.org/en/) with the following supports
  - [pytest-cov](https://github.com/pytest-dev/pytest-cov): generate test coverage repo
  - [pytest-mock](https://github.com/pytest-dev/pytest-mock/): mocking
- [commitizen](https://commitizen-tools.github.io/commitizen/):
  - regulate git commit convention
  - generate changelog automatically
- [invoke](http://www.pyinvoke.org/): organize the tools above
- [pre-commit](https://pre-commit.com/): git-hook to run the above tools automatically
- Consolidate most of the tool configurations in `pyproject.toml`

## Getting Started

### Set up a Development Environment & Run Server

#### 1. Prerequisite Setup

Before starting, make sure to create a `.env` file with your own parameters based on the `.env.example` file.

#### 2. Development Environment Setup

Install dependencies and set up the virtual environment:

```shell
$ poetry install
```

#### 3. Server Run

##### Method 1: Using poetry

```shell
$ inv env.run
```

##### Method 2: Using Docker Compose

```shell
$ docker compose up --build
```

## Running Tests

To run all test cases, use the following command:

```shell
$ inv test.run
```

Run a specific test file in app/routers/{file}

```shell
$ inv test.run --file=file_name
$ inv test.run -f=file_name
```

For a test coverage report, run:

```shell
$ inv test.coverage
```

## Coding Style

To check the code style using `black`, `isort`, and `flake8`, execute:

```shell
$ inv style.run
```

To reformat Python files using `black` and `isort`, use:

```shell
$ inv style.run --reformat
$ inv style.run -r
```

## Security Check

To perform security checks using safety and bandit, use:

```shell
$ inv secure.run
```
