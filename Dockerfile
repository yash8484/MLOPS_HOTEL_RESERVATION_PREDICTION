# Use a lightweight Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and ensure logs are shown in real-time
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GOOGLE_APPLICATION_CREDENTIALS="c:\Users\Asus\Downloads\beaming-team-447617-k7-15028f5f7927.json"  # 👈 Set GCP credentials path if needed

# Set the working directory
WORKDIR /app

# Install system dependencies required by LightGBM and others
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the entire application
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -e .

# Optional: COPY credentials.json only if you're baking into the image (not recommended for production)
# COPY credentials.json /app/credentials.json

# Run training pipeline
RUN python pipeline/training_pipeline.py

# Expose port used by Flask
EXPOSE 5000

# Start the application
CMD ["python", "application.py"]
