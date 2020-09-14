from flask import Flask, render_template, request, url_for, redirect, jsonify
import json

import pandas as pd
import pickle
import numpy as np

#model = load_model('deployment_28042020')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route('/response', methods=['GET', 'POST'])
def response():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    #prediction = predict_model(model, data=final, round = 0)
    data = {
        "type": "line",
        "data": {"labels":["1st","2nd", "3rd"],
        "datasets": [{
        "label": "My First dataset",
        "backgroundColor": "rgb(255, 99, 132)",
        "borderColor": "rgb(255, 99, 132)",
        "data": [20,10,15]
        }],
        "options": {}}
    }
    return jsonify(data)




    

   