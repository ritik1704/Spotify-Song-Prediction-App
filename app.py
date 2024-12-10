import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

#Creating the flask app
app = Flask(__name__)

model = pickle.load(open('spotify-recommender.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    num_features = [float(x) for x in request.form.values()]
    final_features = [np.array(num_features)]
    prediction = model.predict(final_features)
    prediction = prediction[0]
    print(prediction)

    if prediction < 0.5:
        return render_template('index.html', prediction_text='Prediction: FLOP')
    else:
        return render_template('index.html', prediction_text='Prediction: HIT')


if __name__ == "__main__":
    app.run(debug=True)
