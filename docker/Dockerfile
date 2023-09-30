# Usinging a base image with Python already installed
FROM python:3.8

# Setting the working directory inside the container
WORKDIR /app

# Copying the app directory containing the Flask application
COPY ./app ./app

# Installing all necessary Python packages
RUN pip install --no-cache-dir -r app/requirements.txt

# Exposing the port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app/__init__

# Define the command to run your Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
