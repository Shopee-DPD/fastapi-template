# FastAPI Template

## Technology Stack

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
1. Install [cookiecutter](https://github.com/cookiecutter/cookiecutter)
```
> pip install cookiecutter
```

2. Clone the [fastapi template](https://github.com/Shopee-DPD/fastapi-template)
```
> cookiecutter git@github.com:Shopee-DPD/fastapi-template.git
```

3. Provide the following inputs:
  - project_name: The name of the project, which will be used to create folders and populate the README
  - project_description: A description of the project, which will be added to the README
  - python_version: The Python version, which will be specified in poetry and the Dockerfile
  - build_docker_image: Whether to create a docker-compose file
  - send_logs_to_elk: Whether to send logs to ELK
