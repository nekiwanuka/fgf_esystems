# Use an appropriate Python image for your Django project
FROM python:3.10

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Gunicorn configuration file
RUN echo "workers = 4\nbind = '0.0.0.0:8000'" > gunicorn_config.py

# Copy the project code into the container
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "fgf.wsgi:application", "--config", "gunicorn_config.py"]
