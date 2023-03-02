import os.path
import pandas as pd

from joblib import load

path = os.path.dirname(os.path.abspath(__file__))

#TODO: Load the model.joblib file and assign it to a variable

def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width) -> str:
    #TODO: Use the loaded model to make predictions based on parameters.
    pass

print(predict_iris_species(
    sepal_length=1.0,
    sepal_width=1.0,
    petal_length=1.0,
    petal_width=1.0
))