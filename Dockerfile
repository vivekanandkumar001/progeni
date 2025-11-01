# Docker for HF Spaces (listens on 7860)
FROM python:3.10-slim


RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app
COPY --chown=user:user . /app
USER root
RUN apt-get update && apt-get install -y build-essential poppler-utils && rm -rf /var/lib/apt/lists/*
USER user

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


ENV PORT=7860
EXPOSE 7860


CMD ["gunicorn", "app:create_app()", "-w", "2", "-k", "gthread", "--threads", "4", "-b", "0.0.0.0:7860", "--timeout", "120"]
