# Docker-for-ML
this repository explains how ML applications are being deployed and maintained via DOCKER
# Overview 
This repository demonstrates how to deploy a machine learning model using Docker. We've built a calorie predictor model that estimates calories burned based on various factors. The model is containerized for easy deployment and reproducibility.
# Project Structure
    calories_predictor/
    ├── config.py
    ├── data_preprocessing.py
    ├── model_evaluation.py
    ├── model_building.py
    └── tests/
        └── test_prediction.py
    data/
    ├── raw_data.csv
    ├── processed_data.csv
    ├── train.csv
    └── test.csv
    docs/
    └── project_documentation.xlsx
    LICENSE
    MANIFEST.in
    requirements.txt
    setup.py
    Dockerfile
    main.py
# Usage
## Building a Docker image
    docker build -t calorie_predictor .
## Running Container
    docker run -it -p 8000:80 calorie_predictor
## Running Unit test
    pytest test_prediction.py



