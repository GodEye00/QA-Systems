Here is the corrected README:

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
export ELASTICSEARCH_HOST=<your-host-elasticsearch-url>
export ELASTICSEARCH_API_KEY=<your-host-elasticsearch-api-key>
export OPENAI_API_KEY=<your-openai-api-key>
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

1. **Enter the docker directory**:

```bash
cd QA-Systems/docker
```

2. **Build the Docker Image**:

```bash
docker build --no-cache -t flask_app .
```

3. **Run the Docker Container**:

Once the image is built, you can run a Docker container using the following command:

```bash
docker run -p 5000:5000 flask_app
```

4. **Access the Application**:

You can access the application at `http://localhost:5000`.

Please note that this Docker container assumes that the necessary Python packages and dependencies are listed in the `requirements.txt` file, and they will be installed during the build process.

For a detailed technical explanation of the design choices made for each task, please refer to the [Technical Design Document](https://github.com/GodEye00/QA-Systems/blob/master/docs/technical.pdf).

--- 
