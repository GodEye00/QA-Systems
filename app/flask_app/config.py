import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ELASTICSEARCH_HOST = os.environ.get('ELASTICSEARCH_HOST') or 'localhost'
    ELASTICSEARCH_PORT = os.environ.get('ELASTICSEARCH_PORT') or 9200
