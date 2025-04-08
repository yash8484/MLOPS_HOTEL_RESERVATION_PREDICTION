# Use a lightweight Python image
FROM python:slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Optional: Set GCP credentials path inside the container
# Make sure the file is copied into the container and path matches
# ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials/gcp-key.json"

# Set the working directory
WORKDIR /app

# Install system dependencies required by LightGBM
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code into the container
COPY . .

# Install the package in editable mode
RUN pip install --no-cache-dir -e .

# Run the training pipeline
RUN python pipeline/training_pipeline.py

# Expose the port that Flask will run on
EXPOSE 5000

# Start the Flask application
CMD ["python", "application.py"]

