import os

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, jsonify, make_response
import gpio_calls
import couch_calls


LIGHT_THRESHHOLD=10000 #change if needed in the future


def check_sensors():
    print("checking sensors")
    couch_calls.add_record(gpio_calls.query_light(),'light')
    couch_calls.add_record(gpio_calls.query_water_temp(), 'temp')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    cron = BackgroundScheduler(daemon=True)
    cron.add_job(check_sensors, 'interval', hours=1)
    cron.start()

    #init couch_db connection
    #todo: use env variables to pass url and db name
    couch_calls.init()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/api/temp')
    def get_temp():
        temp = gpio_calls.query_water_temp()
        response_body = {
            "temp": temp
        }
        res = make_response(jsonify(response_body), 200)
        return res

    @app.route('/api/temp-data')
    def get_tables():
        temp_data = couch_calls.get_records_by_key('temp')
        temp_graph = {element['date']: element['value'] for element in temp_data}
        response_body = {
            "temps_graph": temp_graph,
            "temps_table": temp_data
        }
        res = make_response(jsonify(response_body), 200)
        return res

    @app.route('/api/dashboard-data')
    def get_dashboard_data():
        temp_data_as_dict = {element['date']: element['value'] for element in couch_calls.get_records_by_key('temp', False)}
        light_data = couch_calls.get_records_by_key('light', False)
        times_above_threshhold = sum(row['value']['val']> LIGHT_THRESHHOLD for row in light_data)
        light_data_as_dict = {element['date']:element['value']['val'] for element in light_data}
        above = 0
        below = 0
        if light_data:
            above = (times_above_threshhold/len(light_data)) * 100
            below = ((len(light_data) - times_above_threshhold)/len(light_data)) * 100
        response_body = {
            "light_rate": {
                "above": above,
                "below": below
            },
            "temps": temp_data_as_dict,
            "lights": light_data_as_dict
        }
        res = make_response(jsonify(response_body),200)
        return res


    @app.route('/api/light-data')
    def get_light_data():
        light_data = couch_calls.get_records_by_key('light')
        light_data_voltage_dict = {element['date']:element['value']['voltage'] for element in light_data}
        light_data_as_value = {element['date']:element['value']['val'] for element in light_data}
        temp_data_table = [{"date": element['date'], "val":element['value']} for element in light_data]
        response_body  = {
            "lights_voltage": light_data_voltage_dict,
            "lights_vals": light_data_as_value,
            "lights_table_data": temp_data_table
        }
        res = make_response(jsonify(response_body),200)
        return res
    return app
