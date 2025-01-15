# Use an official Python image as the base
FROM python:3.10-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY src/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the source code and models
COPY src /app/src
COPY models /app/models
COPY data /app/data

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Ensure the virtual environment is active and run the build_models script
CMD ["python", "/app/src/build_models.py"]