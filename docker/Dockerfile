# builder
FROM python:3.11-slim AS builder

WORKDIR /build
ENV PIP_NO_CACHE_DIR=1

# создаём venv в /opt/venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# сначала только зависимости — кэш слоёв
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# runtime
FROM python:3.11-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTICODE=1 \ 
    PATH="/opt/venv/bin:$PATH"

RUN useradd -m -u 1000 appuser
WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

COPY app ./app
COPY frontend ./frontend
COPY alembic ./alembic
COPY alembic.ini ./
COPY scripts ./scripts

USER appuser
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
