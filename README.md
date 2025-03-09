# Depression Detection Project

## Project Overview
This project detects depression based on users' posts. Users can upload their posts in the form of text files, image files, or audio files. The system uses machine learning (SVM - Support Vector Machine) to analyze the posts and classify them as either "Negative" (depression-related) or "Positive" (normal posts). If a user's post is detected as negative (indicating depression), the system sends motivating messages to help the user.

## Objective
The primary objective of this project is to identify depression from online posts. With the increasing use of social networks for communication, it is vital to provide an application that can detect depression by analyzing users' posts (text, image, or audio). The system uses an SVM classifier to analyze these posts and generate motivational responses.

## Technology Stack
- **Backend Framework**: Django
- **Machine Learning**: SVM (Support Vector Machine)
- **Database**: MySQL
- **File Storage**: Local file storage using Django's FileSystemStorage
- **Libraries Used**:
  - `scikit-learn` for SVM classification
  - `pymysql` for MySQL database interaction
  - `pytesseract` for OCR (Optical Character Recognition) in images
  - `speech_recognition` for audio file processing
  - `matplotlib` for visualizing post statistics

## Features
- **Upload Posts**: Users can upload posts in text, image, or audio format.
- **Depression Detection**: The system classifies the content as either "Positive" or "Negative" based on the sentiment expressed.
- **Motivational Messages**: If depression is detected, users receive motivational posts.
- **Admin Panel**: Admins can view users' posts and send motivational messages to those in need.
- **User Registration and Login**: Users can register, log in, and manage their posts.

## Project Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SowmyaHariniDeviKumpatla/Depression-Detection-Project.git
2. **Install dependencies**:  
   Ensure you have a virtual environment set up, then install the required libraries:
   ```bash
   pip install -r requirements.txt
3. **Database Setup**:
   Set up MySQL and create the database:
   ```bash
   CREATE DATABASE depression;
   Update the DATABASES settings in settings.py with your MySQL credentials.
   Run migrations to set up the necessary database tables:
   ```bash
   python manage.py migrate
5. **Run the project:**:
   ```bash
   python manage.py runserver

## Project Setup
This project is an ongoing project that current students are still working on. The source code is made available for educational and informational purposes. By viewing this repository, you agree not to make any changes or distribute it further. The repository is licensed under the MIT License, but contributions and modifications are not allowed at this stage.



