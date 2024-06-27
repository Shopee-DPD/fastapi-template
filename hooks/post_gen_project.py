import os


def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def main():
    if "{{ cookiecutter.build_docker_image }}" == "n":
        remove_file("Dockerfile")
        remove_file("docker-compose.yml")


if __name__ == "__main__":
    main()
