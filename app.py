from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import time
import utilities as ut

app = Flask(__name__)
api = Api(app)

class Times(Resource):
    def post(self):
        data = pd.read_csv('Transit-Info.csv', header = 0, index_col=0, squeeze=True).to_dict()
        parse = reqparse.RequestParser()
        
        parse.add_argument('Time', required=True, help="Need to specify train time")
        args = parse.parse_args()
        given_time = args['Time']

        if not ut.validate_time_format([given_time]) :
            return {
                'message': f"' Please make sure '{given_time}' is in correct HH:MM 24 hr format."
            }, 400
        
        mapping_times = {} 
        for train, times in data.items():
            converted = ut.convert_str_to_list(times)
            for time_val in converted:
                if time_val in mapping_times:
                    mapping_times[time_val].append(train)
                else:
                    mapping_times[time_val] = [train]
        greater_list = [i for i in sorted(mapping_times.keys()) if i >= given_time]
        lesser_list = [i for i in sorted(mapping_times.keys()) if i < given_time]
        for time_value in greater_list:
            if len(mapping_times[time_value])>=2:
                return f"'{time_value}','{mapping_times[time_value]}'", 200

        for time_value in lesser_list:
            if len(mapping_times[time_value])>=2:
                return f"'{time_value}','{mapping_times[time_value]}'", 200
        
        return f"'No instances when multiple trains are in the station at this time'", 200

class Trains(Resource):
    def get(self):
        data = pd.read_csv('Transit-Info.csv', header=0, index_col=0, squeeze=True).to_dict()
        return data, 200

    def post(self):
        data = pd.read_csv('Transit-Info.csv', header=0, index_col=0, squeeze=True)
        parse = reqparse.RequestParser()
        
        parse.add_argument('Train', required=True, help="Need to specify Train name")
        parse.add_argument('Times', required=True, help="Need to specify Train times")
        
        args = parse.parse_args()
        new_train = args['Train'].upper()
        new_times = args['Times']
        times_list = ut.convert_str_to_list(new_times)
        converted_list = '[%s]' % ", ".join(map(str, times_list))

        if new_train in list(data.keys()):
            return {
                'message': f"'{new_train}' already exists."
            }, 400
        if not new_train.isalnum() or len(new_train) != 4:
            return {
                'message': f"'{new_train}' needs to be 4 characters and alphanumeric"
            }, 400
        if not ut.valid_timelist_format(new_times) or not ut.validate_time_format(times_list):
            return {
                'message': "Please make sure time entry is in [] and in HH:MM 24 hour format. Ex: [08:00, 09:30, 16:00, 18:00]"
            }, 400
        else:
            new_data = pd.DataFrame({
                'Trains': new_train,
                'Times': [converted_list]
            })
        new_data.to_csv('Transit-Info.csv', mode='a', index=False, header=False)
        return pd.read_csv('Transit-Info.csv', header = 0, index_col=0, squeeze=True).to_dict(), 200


api.add_resource(Trains, '/trains') 
api.add_resource(Times, '/times') 

if __name__ == '__main__':
    app.run()  # run our Flask app