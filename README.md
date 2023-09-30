# Question and Answers System (QA System)

## Overview

The Question and Answers Assistant is a system designed to provide answers to user queries based on indexed documents. It utilizes Elasticsearch for document indexing and retrieval, as well as a pre-trained language model (gpt-3.5 turbo) for question answering.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Indexing Documents](#indexing-documents)
  - [Running the Frontend](#running-the-frontend)
  - [Running the Flask app](#running-the-flask-app)
  - [Running the Docker Container](#running-the-docker-container)

## Getting Started

### Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python >= 3.6
- Elasticsearch
- Other Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository from the master branch:

```bash
git clone https://github.com/GodEye00/QA-Systems.git master
```
2. cd into the qa_system directory
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Indexing Documents

1. Add your documents to the `qa_system` directory.
   
2. Run the indexing script:

```bash
python3 indexing.py
```

### Running the Frontend
1. cd into the app directory within the qa_system directory

2. Start the Streamlit app:

```bash
streamlit run gui.py
```

3. Access the frontend in your web browser at `http://localhost:8501`.


### Running the Flask App
1. cd into the app directory within the qa_system directory
2. export path
   ```bash
   export FLASK_APP=flask_app/__init__
   ```
4. start the flask app
```bash
flask run
```

3. Access the flask endpoint at `http://localhost:5000`.


## Running the Docker Container

To run the Question and Answers Assistant using Docker, follow these steps:

1. **Build the Docker Image**:

  

   ```
   docker build --no-cache -t flask_app .
   ```

   This command will use the `Dockerfile` to build an image named `qa_system`.

2. **Run the Docker Container**:

   Once the image is built, you can run a Docker container using the following command:

   ```
   docker run -p 5000:5000 qa_system
   ```
3. **Access the Application**:

  You can access the application `http://localhost:5000`

Please note that this Docker container assumes that the necessary Python packages and dependencies are listed in the `requirements.txt` file, and they will be installed during the build process.

For a detailed technical explanation of the design choices made for each task, please refer to the [Technical Design Document](https://github.com/GodEye00/QA-Systems/blob/master/docs/technical.pdf).
