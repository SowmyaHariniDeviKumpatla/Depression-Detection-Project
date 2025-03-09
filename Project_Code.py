from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import datetime
import pymysql
import joblib
import PIL.Image
import pytesseract
import matplotlib.pyplot as plt
import re
import numpy as np
import speech_recognition as sr

# Load the SVM model
svm_classifier = joblib.load('svmClassifier.pkl')

# Views
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})

def UploadPost(request):
    if request.method == 'GET':
        return render(request, 'UploadPost.html', {})

def Register(request):
    if request.method == 'GET':
        return render(request, 'Register.html', {})

def Admin(request):
    if request.method == 'GET':
        return render(request, 'Admin.html', {})

def Login(request):
    if request.method == 'GET':
        return render(request, 'Login.html', {})

def SendMotivatedPost(request):
    if request.method == 'GET':
        return render(request, 'SendMotivatedPost.html', {})

def predict(textdata, classifier):
    text_processed = textdata
    X = [text_processed]
    sentiment = classifier.predict(X)
    return sentiment[0]

def predictSentiment(textdata):
    result = predict(textdata, svm_classifier)
    predicts = ""
    if result == 0:
        predicts = "Negative"
    if result == 1:
        predicts = "Positive"
    return predicts

def SendMotivatedPostData(request):
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        time = request.POST.get('t2', False)
        text = request.POST.get('t3', False)

        db_connection = pymysql.connect(host='127.0.0.1', port=3308, user='root', password='root', database='depression', charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "UPDATE postdata SET motivate_post=%s WHERE username=%s AND post_time=%s AND motivate_post='Pending'"
        db_cursor.execute(student_sql_query, (text, username, time))
        db_connection.commit()

        context = {'data': f'Your motivated text sent to user {username}'}
        return render(request, 'SendMotivatedPost.html', context)

def UploadPostData(request):
    if request.method == 'POST' and request.FILES['t1']:
        output = ''
        myfile = request.FILES['t1']
        fs = FileSystemStorage()
        name = str(myfile)

        if name.lower().endswith('.txt'):
            name = 'text.txt'
        elif name.lower().endswith(('.png', '.jpg', '.jpeg', 'gif')):
            name = 'img.jpg'

        filename = fs.save(name, myfile)

        if name.lower().endswith('.txt'):
            with open("text.txt", "r") as file:
                for line in file:
                    line = line.strip('\n')
                    output += line + ' '
        elif name.lower().endswith(('.png', '.jpg', '.jpeg', 'gif')):
            output = pytesseract.image_to_string(PIL.Image.open(name))
            output = output.replace('\n', ' ')
        elif name.lower().endswith('.wav'):
            r = sr.Recognizer()
            with sr.AudioFile(name) as source:
                audio = r.record(source)
            try:
                output = r.recognize_google(audio)
            except:
                pass

        user = ''
        with open("session.txt", "r") as file:
            user = file.strip('\n')

        now = datetime.datetime.now()
        option = 'Pending'
        output = re.sub('\W+', ' ', output)
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        sentiment = predictSentiment(output.lower())

        db_connection = pymysql.connect(host='127.0.0.1', port=3308, user='root', password='root', database='depression', charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO postdata(username, post_data, post_time, depression, motivate_post) VALUES(%s, %s, %s, %s, %s)"
        db_cursor.execute(student_sql_query, (user, output, current_time, sentiment, option))
        db_connection.commit()

        if db_cursor.rowcount == 1:
            context = {'data': f'Detected Depression From Uploaded File: {sentiment}'}
        else:
            context = {'data': 'Error in signup process'}

        return render(request, 'UploadPost.html', context)

# Admin and User views
def ViewUsers(request):
    if request.method == 'GET':
        strdata = '<table border=1 align=center width=100%><tr><th>Username</th><th>Password</th><th>Contact No</th><th>Email ID</th><th>Address</th></tr><tr>'
        con = pymysql.connect(host='127.0.0.1', port=3308, user='root', password='root', database='depression', charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                strdata += f'<td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{str(row[3])}</td><td>{str(row[4])}</td></tr>'
        context = {'data': strdata}
        return render(request, 'ViewUsers.html', context)

def ViewPosts(request):
    if request.method == 'GET':
        positive = 0
        negative = 0
        strdata = '<table border=1 align=center width=100%><tr><th>Username</th><th>Post Data</th><th>Post Time</th><th>Depression</th><th>Motivated Post</th></tr><tr>'
        con = pymysql.connect(host='127.0.0.1', port=3308, user='root', password='root', database='depression', charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM postdata")
            rows = cur.fetchall()
            for row in rows:
                if row[3] == 'Negative':
                    negative += 1
                else:
                    positive += 1

                strdata += f'<td>{row[0]}</td><td>{row[1]}</td><td>{str(row[2])}</td><td>{str(row[3])}</td><td>{str(row[4])}</td></tr>'

        height = [positive, negative]
        bars = ('Depression Posts', 'Non Depression Post')
        y_pos = np.arange(len(bars))
        plt.bar(y_pos, height)
        plt.xticks(y_pos, bars)
        plt.show()

        context = {'data': strdata}
        return render(request, 'ViewPosts.html', context)

# Main Django run command
#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Depression.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
