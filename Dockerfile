
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.6-slim

EXPOSE 8000

WORKDIR /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install underlying platform updates
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat git && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install poetry requirements
COPY poetry.lock pyproject.toml /app
RUN pip install poetry && \
    poetry export --without-hashes > requirements.txt && \
    pip install -r requirements.txt
# poetry config virtualenvs.in-project true && \
# poetry install --no-dev

COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser


RUN alembic upgrade head
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
#CMD gunicorn -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 app.main:app --name=maker-hub