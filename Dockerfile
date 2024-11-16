FROM python:3.12-slim-bookworm

RUN useradd -ms /bin/bash -d /app app

COPY dist/*.whl .

RUN pip install *.whl && rm -rf *.whl

USER app

WORKDIR /app

RUN mkdir configs migrations
