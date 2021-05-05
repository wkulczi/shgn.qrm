import os

from flask import Flask, jsonify, make_response
import gpio_calls
import couch_calls

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

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
        temp = gpio_calls.query_water_temp_mock()
        response_body = {
            "temp": temp
        }
        res = make_response(jsonify(response_body), 200)
        return res

    @app.route('/api/tables')
    def get_tables():
        temp_data = couch_calls.get_records('temp')
        light_data = couch_calls.get_records('light')
        response_body = {
            "temps": temp_data,
            "lights": light_data
        }
        res = make_response(jsonify(response_body), 200)
        return res
    return app