FROM python:3.11

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY bot/ ./bot/
COPY settings/ ./settings/
COPY tools/ ./tools/

CMD ["python", "main.py"]