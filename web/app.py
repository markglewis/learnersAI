from flask import Flask, render_template, request, url_for, redirect, jsonify

import pandas as pd
import pickle
import numpy as np

#model = load_model('deployment_28042020')
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    #prediction = predict_model(model, data=final, round = 0)
    return render_template('index.html',pred='output={}'.format(final))