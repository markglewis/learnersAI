from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
from random import randrange


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
        "data": [randrange(10),randrange(10),randrange(10)]
        }],
        "options": {}}
    }
    return jsonify(data)

@app.route('/model', methods=['GET', 'POST'])
def model():
    load_model = pickle.load(open('static/bayes_count.sav','rb'))
    count_vect = pickle.load(open('static/count_vect.sav','rb'))
    int_features = [x for x in request.form.values()]


    testheadlines = ['TSLA - Cybertruck expected to hit the market strong']

    testheadlines = int_features
    nr = len(testheadlines)
    dftest = pd.DataFrame(columns=['headline','clean_headline'],index=np.arange(nr))
    for ii in np.arange(nr):
    	txt = testheadlines[ii]
    	dftest.iloc[ii]['clean_headline'] = txt
    print(dftest.head())
    ser = dftest['clean_headline']
    for val in ser.values[0:4]:
    	print(val)
    ser_count =  count_vect.transform(ser)
    predictions = load_model.predict(ser_count)
    ii=0
    #for val in ser.values:
    returnvalue = []
    for ii in np.arange(nr):
    	print('\n tweet, sentiment = ',testheadlines[ii],predictions[ii])
    	returnvalue = str(testheadlines[ii]) + " " + str(predictions[ii])
    	returnvalue = [str(testheadlines[ii]),str(predictions[ii])]
    	ii += 1
    return jsonify(returnvalue)

if __name__ == '__main__':
	app.run()