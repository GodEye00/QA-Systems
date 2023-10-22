---

# Question and Answers System (QA System)

## Overview

The Question and Answers Assistant is a system designed to provide answers to user queries based on indexed documents. It utilizes Elasticsearch for document indexing and retrieval, as well as a pre-trained language model (GPT-3.5 Turbo) for question answering.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Indexing Documents](#indexing-documents)
  - [Retrieving Documents](#retrieving-documents)
  - [Running the Frontend](#running-the-frontend)
  - [Running the Flask App](#running-the-flask-app)
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
git clone https://github.com/GodEye00/QA-Systems.git
```

2. cd into the `QA-Systems` directory.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Run exports:

```bash
OPENAI_API_KEY=<your-openai-api-key>
ELASTICSEARCH_CLOUD_ID=<your-elastic-search-cloud-id>
ELASTICSEARCH_API_KEY=<your-elastic-search-api-key>
ELASTICSEARCH_INDEX=<your-elastic-search-index-for-this-project>
```

## Usage

### Indexing Documents

1. Add your documents to the `QA-Systems/app` directory.

```bash
cd QA-Systems/app
```

2. Run the indexing script:

```bash
python3 indexing.py
```

### Retrieving Documents

1. Add your documents to the `QA-Systems/app` directory.

```bash
cd QA-Systems/app
```

2. Run the retrieval script:

```bash
python3 retrieval.py
```

### Running the Frontend

1. cd into the `QA-Systems/app` directory.

```bash
cd QA-Systems/app
```

2. Start the Streamlit app:

```bash
streamlit run gui.py
```

3. Access the frontend in your web browser at `http://<your-api-address>:8501`.

### Running the Flask App

1. cd into the `QA-Systems/app` directory.

```bash
cd QA-Systems/app
```

2. Export path:

```bash
export FLASK_APP=flask_app/__init__.py
```

3. Start the Flask app:

```bash
flask run
```

4. Access the Flask endpoint at `http://localhost:5000`.

## Running the Docker Container

To run the Question and Answers Assistant using Docker, follow these steps:


1. **Pull the docker image**:

```bash
docker pull dawuda/qa_system:v1
```

2. **create an .env file with the following config**:

```bash
OPENAI_API_KEY=<your-openai-api-key>
ELASTICSEARCH_CLOUD_ID=<your-elastic-search-cloud-id>
ELASTICSEARCH_API_KEY=<your-elastic-search-api-key>
ELASTICSEARCH_INDEX=<your-elastic-search-index-for-this-project>
```

3. **Run the Docker Container**:

Once the image is successfully pulled, run the image using the following command. **Note**:  Make sure the .env file you created in step 2 is in the same directory as where you run the docker image:

```bash
docker run --env-file .env -p 5000:5000 -p 8501:8501 dawuda/qa_system:v1
```

4. **Access both the flask and streamlit Application after the run completes**:

Waiting for the application to finish downloading and you can access the flask application at `http://localhost:5000`
and the streamlit UI application at `http://localhost:8501` or `http://<your-network-ip-address>:8501`.

Please note that this Docker container assumes that the necessary Python packages and dependencies are listed in the `requirements.txt` file, and they will be installed during the build process.

For a detailed technical explanation of the design choices made for each task, please refer to the [Technical Design Document](https://github.com/GodEye00/QA-Systems/blob/master/docs/technical.pdf).

--- 
