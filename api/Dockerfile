FROM python:3.10-slim-bullseye

WORKDIR /app

# Set the PYTHONPATH environment variable to include the /app/api directory
ENV PYTHONPATH=/app/api

COPY api/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy only the `api` and `models` directories
COPY api /app/api
# COPY models /app/models

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]