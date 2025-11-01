# Dockerfile for Hugging Face Spaces (Flask)
FROM python:3.10-slim

# create non-root user (good practice)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# copy files as non-root
COPY --chown=user:1000 . /app

# Install system deps (add more if your model needs them)
USER root
RUN apt-get update && apt-get install -y build-essential poppler-utils \
    && rm -rf /var/lib/apt/lists/*

USER user
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose HF required port
ENV PORT=7860
EXPOSE 7860

# Use gunicorn to run create_app() factory
CMD ["gunicorn", "app:create_app()", "-w", "2", "-k", "gthread", "--threads", "4", "-b", "0.0.0.0:7860", "--timeout", "120"]
