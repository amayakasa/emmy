FROM python:3.11-slim-bookworm as builder

RUN pip install poetry==1.5.1

ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV POETRY_CACHE_DIR=/tmp/emmy_poetry_cache

WORKDIR /emmy

COPY ./pyproject.toml ./poetry.lock ./
RUN touch README.md

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --only main --no-root

FROM python:3.11-slim-bookworm as runtime

ENV VIRTUAL_ENV=/emmy/.venv
ENV PATH=/emmy/.venv/bin:$PATH

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /sources

COPY ./sources ./

ENTRYPOINT python -m emmy
