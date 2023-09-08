# 1. Library imports
import uvicorn
from fastapi import FastAPI
from SpamMessages import SpamMessage
import numpy as np
import joblib
import pandas as pd

# 2. Create the app object
app = FastAPI()

# Load the model
model_path = "models/spam-detection-model.pkl"
spam_classifier = joblib.load(model_path)

# pickle_in = open(model_path,"rb")
# spam_classifier = pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, Friend !'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To SPAM MESSAGE DETECTIVE': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Spam Message with the confidence
@app.post('/predict')
def predict_spammessage(data:SpamMessage):
    data = data.dict()
    # message = data['message']
    length = data['length']
    punct = data['punct']

    prediction = spam_classifier.predict([[length, punct]])
    if(prediction[0]>0.5):
        prediction="Spam Message"
    else:
        prediction="Its a Ham Message"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload