# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]