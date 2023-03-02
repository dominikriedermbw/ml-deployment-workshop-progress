# save this as app.py
import os
from flask import Flask, Response
from flask import request as flask_request

import sys
sys.path.append("..")

from trained_models import iris_classifier

FLASK_API_KEY = os.getenv("FLASK_API_KEY")
app = Flask(__name__)


"""@app.before_request
def check_api_key():
    pass
"""

@app.route("/")
def api_info():
    #TODO: return a basic description of the endpoints you want to make available
    pass


@app.route("/predict_iris_species", methods=["POST"])
def predict_iris_species():
    #TODO: extract request data and return the model prediction
    pass

if __name__ == "__main__":
    app.run(host="localhost", port=8000)