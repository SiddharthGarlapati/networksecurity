# Use a lightweight Python image
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies required for some Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to avoid dependency issues
RUN pip install --upgrade pip

# Install dependencies without caching issues
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python3", "app.py"]
