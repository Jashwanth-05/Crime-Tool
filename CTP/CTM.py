import pickle
import numpy as np

with open('Crime Prediction\Chennai CIty\Chennai City Model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

def predict(db):
    my_prediction=loaded_model.predict(db)
    if my_prediction[0][0] == 1:
        my_prediction='Predicted crime : Act 379-Robbery'
    elif my_prediction[0][1] == 1:
        my_prediction='Predicted crime : Act 13-Gambling'
    elif my_prediction[0][2] == 1:
        my_prediction='Predicted crime : Act 279-Accident'
    elif my_prediction[0][3] == 1:
        my_prediction='Predicted crime : Act 323-Violence'
    elif my_prediction[0][4] == 1:
        my_prediction='Predicted crime : Act 302-Murder'
    elif my_prediction[0][5] == 1:
        my_prediction='Predicted crime : Act 363-kidnapping'
    else:
        my_prediction='Place is safe no crime expected at that timestamp.'
    return my_prediction