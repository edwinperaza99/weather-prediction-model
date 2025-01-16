FROM python:3.10.15-bullseye

WORKDIR /app

# Set the PYTHONPATH environment variable to include the /app/api directory
ENV PYTHONPATH=/app/api

COPY api/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy only the `api` and `models` directories
COPY api /app/api
# COPY models /app/models

# Expose the port for Gunicorn
EXPOSE 8000

# Run the application using Gunicorn with Uvicorn workers
CMD ["gunicorn", "-w", "4", "api.app:app", "--bind", "0.0.0.0:8000"]