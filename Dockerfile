FROM python:slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy app code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

# Keep Docker from appearing idle
RUN echo "Training pipeline starting..." && \
    python pipeline/training_pipeline.py && \
    echo "Training pipeline completed!"

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "application.py"]
