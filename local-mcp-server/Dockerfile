# Use a minimal Python base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install only the MCP package (and update pip first)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastmcp

# Copy only the required files
COPY server.py .

# Run the server
CMD ["python", "server.py"]
