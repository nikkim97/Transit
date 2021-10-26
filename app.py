from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import time
import ast

app = Flask(__name__)
api = Api(app)

class Trains(Resource):
    def get(self):
        data = pd.read_csv('Transit-Info.csv')
        data = data.to_dict()
        return {'data': data}, 200
    
    def post(self):
        reqparse = RequestParser()
        
        reqparser.add_argument('Train', required=True, help="Need to specify Train name")
        reqparser.add_argument('Times', required=True, help="Need to specify Train times")
        
        args = reqparser.parse_args()
        new_train = args['Train'].upper()
        
        if new_train in list(data['Train']):
            return {
                'message': f"{new_train}' already exists."
            }, 401
        if not new_train.isalnum() and new_train.length != 4:
            return {
                'message': f"'{new_train}' needs to be 4 characters and alphanumeric"
            }, 401
        if is_time_formatted(args['Times']) not True:
            return {
                'message': "All time values need to be in H:M format"
            }, 401
        else:
            new_data = pd.DataFrame({
                'Train': new_train,
                'Times': args['Times']
            })

        data = pd.read_csv('Transit-Info.csv')
        data = data.append(new_data)
        data.to_csv('Transit-Info.csv')
        return {'data': data.to_dict()}, 200  # return data with 200 OK
    
    def is_time_formatted(input):
        for x in input:
            if time.strptime(x, '%H:%M'):
                return True
            else:
                return False

api.add_resource(Trains, '/trains') 

if __name__ == '__main__':
    app.run()  # run our Flask app