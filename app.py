from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

pickle_in = open('classifier.pkl','rb') # Opening the pickle file in read bytes mode
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome to Machine Learning app with Docker deployment"


if __name__ == "__main__":
    app.run()
