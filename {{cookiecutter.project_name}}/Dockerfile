FROM python:{{ cookiecutter.python_version }}

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["gunicorn" "app.main:app"]
