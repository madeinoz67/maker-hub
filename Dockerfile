FROM python:3.11.0b1-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat git && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

COPY . ./

CMD poetry run gunicorn --worker-tmp-dir /dev/shm --workers=3 --threads=4 -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080 app.main:app --name=Maker-Hub