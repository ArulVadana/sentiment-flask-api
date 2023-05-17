from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
import pickle
import json

app=Flask(__name__)
api=Api(app)
CORS(app)

model=pickle.load(open('sa.pkl','rb'))
vector=pickle.load(open('vect.pkl','rb'))



class Predict(Resource):
    def get(self):
        return "Welcome to sentiment analysis api"

    def post(self):
        data=request.json
        text=json.dumps(data)
        test_text=vector.transform([text])
        prediction=model.predict(test_text)
        return prediction[0]

api.add_resource(Predict,'/')
app.run(debug=True)