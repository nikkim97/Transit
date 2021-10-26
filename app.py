from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import time
import utilities as ut

app = Flask(__name__)
api = Api(app)

class Trains(Resource):
    def get(self):
        data = pd.read_csv('Transit-Info.csv', header=0, index_col=0, squeeze=True).to_dict()
        return data, 200
    
    def post(self):
        data = pd.read_csv('Transit-Info.csv', header = 0, index_col=0, squeeze=True)
        parse = reqparse.RequestParser()
        
        parse.add_argument('Train_name', required=True, help="Need to specify Train name")
        parse.add_argument('Times', required=True, help="Need to specify Train times")
        
        args = parse.parse_args()
        new_train = args['Train_name'].upper()
        new_times = args['Times']
        times_list = ut.convert_str_to_list(new_times)
        
        if new_train in list(data.keys()):
            return {
                'message': f"{new_train}' already exists."
            }, 401
        if not new_train.isalnum() or len(new_train) != 4:
            return {
                'message': f"'{new_train}' needs to be 4 characters and alphanumeric"
            }, 401
        if not ut.valid_timelist_format(new_times) or not ut.validate_time_format(times_list):
            return {
                'message': "Please make sure time entry is in [] and in HH:MM 24 hour format. Ex: [08:00, 09:30, 16:00, 18:00]"
            }, 401
        else:
            new_data = pd.DataFrame({
                "Trains": new_train,
                "Times": [new_times]
            })
        new_data.to_csv('Transit-Info.csv', mode='a', index=False, header=False)
        return pd.read_csv('Transit-Info.csv', header = 0, index_col=0, squeeze=True).to_dict(), 200

api.add_resource(Trains, '/trains') 

if __name__ == '__main__':
    app.run()  # run our Flask app