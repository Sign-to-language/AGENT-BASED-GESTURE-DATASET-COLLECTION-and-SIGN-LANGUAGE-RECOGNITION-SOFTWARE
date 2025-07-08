# Agent-Based American Sign Language (ASL) Dataset Collection and Recognition Project

This project focuses on the development of a sign language recognition system specifically for **American Sign Language (ASL)**. The solution was designed to address both the data collection and recognition aspects of sign language processing using automation and machine learning.

## Project Overview

The project was structured in three main phases:

### 1. Automated Dataset Collection
- **Tool Used**: Selenium (Python)
- **Purpose**: Automatically scrape and collect ASL gesture images and videos from web-based platforms.
- **Outcome**: A rich and diverse ASL image dataset was constructed to train and evaluate recognition models.

### 2. GUI Development & Preprocessing
- **Interface**: Developed with **Tkinter** for ease of use.
- **Hand Detection**: Integrated **MediaPipe** to detect and extract hand landmarks in real-time.
- **Data Structuring**: Extracted keypoints (landmarks) were formatted into structured tables suitable for ML models.

### 3. Sign Language Recognition with ML
- **Algorithms**: Various machine learning models were trained on the processed hand keypoint data.
- **Goal**: Classify ASL signs with high accuracy based on real-time or recorded input.
- **Evaluation**: Achieved strong performance metrics in classification of common ASL gestures.

## Technologies Used

- **Python**  
- **Selenium** – Web-based data scraping  
- **Tkinter** – GUI for end-user interaction  
- **MediaPipe** – Real-time hand tracking and landmark extraction  
- **NumPy / Pandas** – Data preprocessing and structuring  
- **Scikit-learn / TensorFlow** – Machine learning models

## Objectives

- To automate the collection of large-scale ASL gesture data
- To create an interactive system that can detect and recognize hand gestures in real time
- To support accessibility tools for the hearing-impaired using AI-based solutions

## Output

- A self-collected and labeled ASL dataset
- A complete desktop application with a user-friendly interface
- Trained models capable of accurately predicting ASL gestures

