# Impoering required files
from flask import Flask, request,render_template
import numpy as np
import pickle
import pandas as pd
import random
import json

# Loading pickle files for ML model
depressionModel = pickle.load(open("./pickle files/depression.pkl", "rb"))
covidModel = pickle.load(open("./pickle files/covid.pkl", "rb"))

# Setting up flask 
app = Flask(__name__,template_folder='templates')

# Home route
@app.route("/")
def home():
    return render_template('home.html')

# Route for documentation
@app.route("/api/documentation")
def doc():
    return render_template('index.html')

# Depression detection API
@app.route("/api/depression-detection",methods=["POST"])
def depression():
    form_data = json.loads((((request.data).decode("utf-8"))).split("'")[0])
    data = {}
    try:
        sm = int(form_data['sm'])
        person = int(form_data['person'])
        issue = int(form_data['issues'])
        sc = int(form_data['sc'])
        life = int(form_data['life'])
        depression = int(form_data['depression'])
        arr = np.array([[sm,person,issue,sc,life,depression]])
        predection = depressionModel.predict(arr)
        data['predection'] = int(predection)
        data['response'] = 200
        data['status'] = "success"
        return data
    except:
            data['predection'] = -1
            data['response'] = 400
            data['status'] = "Server error"
            return data

# Covid detection API
@app.route("/api/covid-detection",methods=["POST"])
def covid():
    form_data = json.loads((((request.data).decode("utf-8"))).split("'")[0])
    data = {}
    try:
        breathing_problem = int(form_data['breathing_problem'])
        fever = int(form_data['fever'])
        dry_cough = int(form_data['dry_cough'])
        sore_throat = int(form_data['sore_throat'])
        running_nose = int(form_data['running_nose'])
        headache = int(form_data['headache'])
        abroad= int(form_data['abroad'])
        covid_contact = int(form_data['covid_contact'])
        arr = np.array([[breathing_problem,fever,dry_cough,sore_throat,running_nose,headache,abroad,covid_contact]])
        predection = covidModel.predict(arr)
        data['predection'] = int(predection)
        data['response'] = 200
        data['status'] = "success"
        return data
    except:
        data['predection'] = -1
        data['response'] = 400
        data['status'] = "Server error"
    return data

# API for jokes
@app.route("/api/jokes")
def jokes():
    data = {}
    try:
        jokes = pd.read_csv('./datasets/shortjokes.csv')
        count = len(jokes)
        rand_index = random.randint(0,count)
        data['joke'] = jokes['Joke'][rand_index]
        data['response'] = 200
        data['status'] = "success"
    except:
        data['joke'] = -1
        data['response'] = 400
        data['status'] = "Server error"
    return data

# API for facts
@app.route("/api/facts")
def facts():
    data = {}
    try:
        fact = open('./text files/facts.txt').readlines(  )
        count = len(fact)
        rand_index = random.randint(0,count)
        data['fact'] = fact[rand_index][:-1]
        data['response'] = 200
        data['status'] = "success"
    except:
        data['joke'] = -1
        data['response'] = 400
        data['status'] = "Server error"
    return data