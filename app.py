# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from joblib import load

app = Flask(__name__)


@app.route('/')
def index():
    if 'query' not in request.args:
        return jsonify({'prediction': None, 'message': 'sendme a text'})

    query = request.args('query')
    model = load('./model/model.joblib')
    lables = ['carros', 'economia', 'educacao',
              'esporte', 'musica', 'politica']

    predict = model.predict([query])

    prediction = lables[predict[0]]
