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
   git clone https://github.com/your-username/Depression-Detection-Project.git
2. **Install dependencies**: You need to install the required Python libraries
   ```bash
   pip install -r requirements.txt
3. **Database Setup**: Ensure that you have MySQL set up with the appropriate database (depression). Update the DATABASES settings in settings.py if needed.
4. **Run the project:**: You need to install the required Python libraries
   ```bash
   python manage.py runserver



