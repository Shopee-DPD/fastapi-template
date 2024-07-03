# FastAPI Template
## Quick Start
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
