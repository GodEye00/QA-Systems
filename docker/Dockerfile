# Using a base image with Python already installed
FROM python:3.8

WORKDIR /app/docker
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=../app/flask_app/__init__

CMD ["flask", "run", "--host", "0.0.0.0"]
