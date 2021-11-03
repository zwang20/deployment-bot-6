"""
server.py

contains functions related to the server
"""

import os
import flask
import flask_cors
import jwt
import env

APP = flask.Flask(__name__)
flask_cors.CORS(APP)

@APP.route('/', methods=['GET'])
def ping():
    """
    ping
    """
    data = flask.request.get_json()
    if jwt.decode(
        data["token"],
        env.secret,
        "HS256"
    )["request"] == "get":
        return {"status": "ok"}
    else:
        flask.abort(403)

@APP.route('/<path:path>', methods=['GET', 'PUT', 'DELETE'])
def handle_request(path):
    """
    handle_request
    """

    # if method is GET
    if flask.request.method == 'GET':

        # verify token
        data = jwt.decode(
            flask.request.get_json()["token"],
            env.secret,
            "HS256",
        )
        if not all([
            data["request"] == "get",
            data["path"] == path,
        ]):
            flask.abort(403)

        # split path into list
        path = path.split('/')

        # read file from path
        with open(os.path.join("db-database", *path), 'r', encoding="utf-8") as file:
            data = file.read()

        # return data
        return {"data": data}

    # if method is PUT
    if flask.request.method == 'PUT':

        # verify token
        data = jwt.decode(
            flask.request.get_json()["token"],
            env.secret,
            "HS256",
        )
        if not all([
            data["request"] == "put",
            data["path"] == path,
            data["data"] == flask.request.get_json()["data"],
        ]):
            flask.abort(403)

        # split path into list
        path = path.split('/')

        # write data to path
        with open(os.path.join("db-database", *path), 'w', encoding="utf-8") as file:
            file.write(flask.request.get_json()["data"])

        # return output
        return {}

if __name__=="__main__":
    APP.run(port=env.port)
