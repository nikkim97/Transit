from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
#import ast

app = Flask(__name__)
api = Api(app)

class Trains(Resource):
    def get(self):
        data = pd.read_csv('Transit-Info.csv')
        data = data.to_dict()
        return {'data': data}, 200
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('Train', required=True)
        parser.add_argument('Times', required=True)
        
        args = parser.parse_args()
        
        if args['Train'] in list(data['Train']):
            return {
                'message': f"'{args['Train']}' already exists."
            }, 401
        if args['Train'] not in list:
            return {
                'message': f"'{args['Train']}' needs to be an len = 4 and alphanumeric"
            }, 401
        else:
            new_data = pd.DataFrame({
                'Train': args['Train'],
                'Times': args['Times']
            })

        data = pd.read_csv('Transit-Info.csv')
        data = data.append(new_data)
        data.to_csv('Transit-Info.csv')
        return {'data': data.to_dict()}, 200  # return data with 200 OK
    
api.add_resource(Trains, '/trains') 

if __name__ == '__main__':
    app.run()  # run our Flask app