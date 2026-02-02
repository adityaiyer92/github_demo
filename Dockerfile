# Base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run application
CMD ["uvicorn", "fastapi_to_do:app", "--host", "0.0.0.0", "--port", "8000"]