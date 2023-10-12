# Project Title

## Docker Image for Sentiment Analysis

![image](https://github.com/praveendecode/docker-sentiment-ai/assets/95226524/e4922f14-b789-4cf2-93dd-0843d7a78054)



# Overview

    This project presents a Dockerized Sentiment Analysis solution using TextBlob. It provides a containerized environment for sentiment analysis on textual data. Leveraging the TextBlob library, this Docker image simplifies sentiment analysis tasks. It offers portability, making it easy to deploy and scale sentiment analysis tasks.

    
# Features

    Containerized Sentiment Analysis: A portable solution for analyzing sentiment in textual data.
    
    Python 3.10 Base Image: Utilizes Python 3.10 for running the sentiment analysis script.
    
    TextBlob Library: Uses the TextBlob library for sentiment analysis.
    
    Simplified Setup: Dockerfile specifies the base image, work directory, and installation steps.
    
    Easy Deployment: Deploy the container to perform sentiment analysis on text.
    
    Sentiment Classification: Classifies sentiment into positive, negative, or neutral based on polarity.
    
    User Interaction: Users can input text for sentiment analysis.
    
    Integration-Ready: Use this Docker image in various applications or services.
    
    Enhanced Understanding: Gain insights into the sentiment of textual content.

# Getting Started

    Pull Docker Image: Find and pull the Docker image from the Docker Hub repository.

    Run Docker Container: Deploy the sentiment analysis service by running the Docker container using the pulled image.

# Technical Steps

### Step 1 : Dockerfile

    Base Image: Utilizes the Python 3.10 base image.
    
    Working Directory: Sets the working directory to "/app" for file operations.
    
    Copy Script: Copies the "sentiment_analysis.py" script to the working directory.
    
    Install Dependency: Installs the "textblob" library using pip.
    
    Run Command: Executes the "sentiment_analysis.py" script using the "CMD" directive in the Docker container.

### Step 2 : sentiment_analysis.py

    The Python script uses the TextBlob library for sentiment analysis.
    
    Users can input text for analysis.
    
    Sentiment is classified as positive, negative, or neutral based on polarity.

# Skills Covered ✅

    Containerization with Docker
    
    Python (Scripting)
    
    TextBlob Library for Sentiment Analysis
    
    Command Line Interface (CLI) for user interaction
    
    Sentiment Classification
    
    Text Analysis and Understanding

# Results

    This Docker image simplifies sentiment analysis tasks by containerizing the service and using the TextBlob library. It is an accessible and user-friendly solution for analyzing sentiment in textual data. Users can easily classify text as positive, negative, or neutral, enhancing the understanding of sentiment in various applications and software.
    
# Connect through LinkedIn for queries !!!!

