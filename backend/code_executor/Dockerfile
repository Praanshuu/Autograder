# Dockerfile for Multi-Language Code Execution
# Optimized for high concurrency and low footprint
FROM python:3.11-slim-bookworm

# Set working directory
WORKDIR /app

# Install dependencies for C, C++, Java, Node.js
# We use --no-install-recommends to keep size down
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    default-jre-headless \
    nodejs \
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

# Labels
LABEL maintainer="Autograder System"
LABEL description="Secure Multi-Language Code Execution Container"
LABEL version="2.5"

# Default command
CMD ["python", "execute.py"]
