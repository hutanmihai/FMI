ARG BUILD_TIME_PYTHONBUFFERED=1


# BASE STAGE
FROM python:3.11.4 AS base

ARG BUILD_TIME_PYTHONBUFFERED
ENV POETRY_VERSION=1.4.0 \
        PYTHONBUFFERED=$BUILD_TIME_PYTHONBUFFERED

RUN pip3 install "poetry==$POETRY_VERSION"


# DEVELOPMENT STAGE
FROM base AS development

WORKDIR /src

COPY . .

RUN poetry lock --no-update
RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "poe", "run_app"]


# PREPARE WHEELS FOR PRODUCTION STAGE
FROM base AS prepare_production

WORKDIR /src

COPY pyproject.toml poetry.lock ./
RUN poetry lock --no-update
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt


# PRODUCTION STAGE
FROM python:3.11.4-slim AS production

ARG BUILD_TIME_PYTHONBUFFERED
ENV  PYTHONBUFFERED=$BUILD_TIME_PYTHONBUFFERED

COPY --from=prepare_production ./src/requirements.txt ./
RUN pip3 install -r requirements.txt
RUN rm -rf /requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY ./src ./src

EXPOSE 8080

WORKDIR /src

RUN export PYTHONPATH=$PYTHONPATH
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
