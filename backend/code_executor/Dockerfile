# Dockerfile for secure Python code execution
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install security packages
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 coderunner && \
    chown -R coderunner:coderunner /app

# Switch to non-root user
USER coderunner

# Set resource limits
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Copy execution script
COPY --chown=coderunner:coderunner execute.py /app/

# Default command
CMD ["python", "execute.py"]
