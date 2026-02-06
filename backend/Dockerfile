# ---------- Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /build

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock* ./

# uv crée un .venv ici
RUN uv sync --no-dev


# ---------- Runtime ----------
FROM python:3.11-slim

WORKDIR /code

# copier le venv construit
COPY --from=builder /build/.venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

ENV APP_TITLE=UserAPIEnsai

CMD ["python", "main.py"]