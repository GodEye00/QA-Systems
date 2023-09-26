from flask import request, jsonify
from app import app

# Defining routes and endpoints within the application

@app.route('/ask_question', method=['POST'])
def ask_question():
    pass

@app.route('/upload_document', method=['POST'])
def upload_document():
    pass