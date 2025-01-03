# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . /app

# Expose port (optional, for any web server or similar)
EXPOSE 8000

# Set the entry point for container
CMD ["python", "src/main.py"]
