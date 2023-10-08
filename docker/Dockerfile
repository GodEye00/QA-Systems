# Using a base image with Python already installed
FROM python:3.8

# Setting the working directory inside the container
WORKDIR /app

# Copying the app directory containing the Flask application
COPY ./app ./app

# Installing supervisord and all necessary Python packages
RUN apt-get update && apt-get install -y supervisor && \
    mkdir -p /var/log/supervisor && \
    pip install --no-cache-dir -r app/requirements.txt

# Copying the supervisor configuration to the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Exposing the ports for Flask (5000) and Streamlit (8501)
EXPOSE 5000 8501

# Setting environment variable for Flask
ENV FLASK_APP=app/flask_app/__init__

# Using supervisord to run both Flask and Streamlit
CMD ["/usr/bin/supervisord"]
