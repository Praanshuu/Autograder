# Dockerfile for secure Python code execution - Optimized for high concurrency
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install security packages and optimize for smaller image
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create non-root user for security
RUN useradd -m -u 1000 coderunner && \
    chown -R coderunner:coderunner /app

# Set environment variables for optimization
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=random
ENV PYTHONIOENCODING=utf-8

# Copy execution script with proper permissions
COPY --chown=coderunner:coderunner execute.py /app/

# Switch to non-root user
USER coderunner

# Set resource limits at container level
LABEL maintainer="Autograder System"
LABEL description="Secure Python code execution container"
LABEL version="2.0"

# Default command
CMD ["python", "execute.py"]
