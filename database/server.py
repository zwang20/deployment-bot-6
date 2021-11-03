"""
server.py

contains functions related to the server
"""

import os
import flask
import flask_cors

APP = flask.Flask(__name__)
flask_cors.CORS(APP)

@APP.route('/', methods=['GET'])
def ping():
    """
    ping
    """
    return {"status": "ok"}

@APP.route('/<path:path>', methods=['GET', 'PUT', 'DELETE'])
def handle_request(path):
    """
    handle_request
    """
    print(path)
    # split path into list
    path = path.split('/')

    # if method is GET
    if flask.request.method == 'GET':

        # read file from path
        with open(os.path.join("db-database", *path), 'r', encoding="utf-8") as file:
            data = file.read()

        # return data
        return {"data": data}

    # else
    else:

        return {}

if __name__=="__main__":
    APP.run(port=12345)
