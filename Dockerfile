# Use the official Python image from the Docker Hub, based on Alpine Linux for a smaller image size
FROM python:3.10-alpine

# Set environment variables to prevent Python from writing .pyc files and to enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /shelves-app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]