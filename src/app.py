from flask import Flask
from flask_restful import Resource, Api, reqparse
import db_func as db
import utilities as ut

app = Flask(__name__)
api = Api(app)

class Trains(Resource):
    def get(self):
        """
        Returns trains schedules
            Train (Dict): Train names and associated time values
        """
        data = ut.return_dict()
        return data, 200

    def post(self):
        """
        Add new train name and times to existing database

            Parameters:
                Train (string): Name of train
                Time (list): Given time values

            Returns:
                Train list (dict): Updated dict of trains and times
        """
        parse = reqparse.RequestParser()

        parse.add_argument('Train', required=True, help="Need to specify Train name (Train : NYC1)")
        parse.add_argument('Times', required=True, help="Need to specify Train times (Times: [08:00, 17:00])")

        args = parse.parse_args()

        new_train = args['Train'].upper()
        new_times = args['Times']
        times_list = ut.convert_str_to_list(new_times)
        times_list_str = '[%s]' % ", ".join(map(str, times_list))

        if new_train in db.keys():
            return {
                'message': f"'{new_train}' already exists."
            }, 400
        if not new_train.isalnum() or len(new_train) != 4:
            return {
                'message': f"'{new_train}' needs to be 4 characters and alphanumeric"
            }, 400
        if not ut.valid_timelist_format(new_times) or not ut.validate_time_format(times_list):
            return {
                'message': "Please make sure time entry is in [] and a valid HH:MM 24 hour format. Ex: [08:00, 09:30, 16:00, 18:00]"
            }, 400
        else:
            db.set(new_train, times_list_str)
            return ut.return_dict(), 200

class Times(Resource):
    def post(self):
        """
        Returns trains based on given time input

            Parameters:
                Time (string): Given time value

            Returns:
                Train (list): Train names associated with next time value
        """
        parse = reqparse.RequestParser()

        parse.add_argument('Time', required=True, help="Need to specify train time (Time: 16:00)")
        args = parse.parse_args()
        given_time = args['Time']

        if not ut.validate_time_format([given_time]) :
            return {
                'message': f"' Please make sure '{given_time}' is a valid HH:MM 24 hr format."
            }, 400

        mapping_times = {}
        for train in db.keys():
            list_of_times = ut.convert_str_to_list(db.fetch(train))
            for time_val in list_of_times:
                if time_val in mapping_times:
                    mapping_times[time_val].append(train)
                else:
                    mapping_times[time_val] = [train]

        sorted_keys = sorted(mapping_times.keys())

        greater_list = [i for i in sorted_keys if i >= given_time]
        lesser_list = [i for i in sorted_keys if i < given_time]

        for time_value in greater_list:
            if len(mapping_times[time_value])>=2:
                return f"'{time_value}','{mapping_times[time_value]}'", 200

        for time_value in lesser_list:
            if len(mapping_times[time_value])>=2:
                return f"'{time_value}','{mapping_times[time_value]}'", 200

        return f"No instances when multiple trains are in the station at {given_time}", 200

api.add_resource(Trains, '/trains')
api.add_resource(Times, '/times')

if __name__ == '__main__':
    app.run()
