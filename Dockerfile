FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY apps ./apps

RUN uv sync --no-dev --no-editable

EXPOSE 8000

CMD ["/app/.venv/bin/uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "8000"]
