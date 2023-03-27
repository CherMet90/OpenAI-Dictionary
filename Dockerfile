# Base image
FROM python:3.11.2-slim-buster

# Set environment variables
ENV FLASK_APP=src.backend
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY ./src ./src

# Expose port
EXPOSE 5000

# Start the application
CMD ["flask", "run", "--reload"]
