# FastAPI French Wrapper for spaCy

This project is a FastAPI wrapper for the spaCy NLP library. It provides an easy-to-use API for various NLP tasks such as tokenization(in french)
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the API, ensure you have Docker installed on your system. If you do not have Docker installed, follow the instructions here: [Install Docker](https://docs.docker.com/get-docker/).

### Installing

To run the FastAPI wrapper, you need to pull the Docker image and then use Docker Compose to build and run the container.

1. **Pull the Docker Image**
   
   Pull the image from Docker Hub:

   ```bash
   docker pull riadm/spacy-api 

2. **Run the Docker Image**


    ```bash
   docker run -d -p 8000:8000 riadm/spacy-api


3. ** Now go look at the docs**
    ```bash
    http://localhost:8000/docs
