ARG BUILD_TIME_PYTHONBUFFERED=1


# BASE STAGE
FROM python:3.11-slim AS base

ARG BUILD_TIME_PYTHONBUFFERED
ENV POETRY_VERSION=1.4.0 \
        PYTHONBUFFERED=$BUILD_TIME_PYTHONBUFFERED

RUN pip3 install "poetry==$POETRY_VERSION"


# DEVELOPMENT STAGE
FROM base AS development

WORKDIR /app

COPY . .

RUN poetry lock --no-update
RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "run_app"]


# PREPARE WHEELS FOR PRODUCTION STAGE
FROM base AS prepare_production

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY ./app ./app
RUN poetry lock --no-update
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt


# PRODUCTION STAGE
FROM python:3.11-slim AS production

ARG BUILD_TIME_PYTHONBUFFERED
ENV  PYTHONBUFFERED=$BUILD_TIME_PYTHONBUFFERED

WORKDIR /app

COPY --from=prepare_production /app/requirements.txt ./
RUN pip3 install -r requirements.txt
RUN rm -rf /app/requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8080

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
