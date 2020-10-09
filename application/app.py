from flask import Flask, jsonify, request
from joblib import load

app = Flask(__file__)


@app.route('/')
def index():
    if 'query' not in request.args:
        return jsonify({'prediction': None, 'message': 'sendme a text'})

    query = request.args('query')
    model = load('./model/model.joblib')
    lables = ['carros', 'economia', 'educação',
              'esporte', 'musica', 'política']

    predict = model.predict([query])

    prediction = lables[predict[0]]
