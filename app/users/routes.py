# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    app/users/controllers
#

from app.utils import dbutils
from app.auth.utils import requires_auth, bad_request

from flask import Blueprint
from flask import abort, request, jsonify, Response

users = Blueprint('users', __name__)


# ------ / ------
@users.route('/', methods=['GET'])
@requires_auth
def list_users():
    return "Not Implemented", 501


@users.route('/', methods=['POST'])
def create_user():
    if not request.json:
        return bad_request("JSON required")

    username = request.json.get('username')
    password = request.json.get('password')
    
    if username is None or password is None:
        abort(400)
        
    # Check if the username already exists
    user = dbutils.execute_query("SELECT username FROM user WHERE username = '{}'".format(username))

    if user:
        return Response("User already exists", 409)    # existing user

    
    conn = dbutils.get_connection()
    cursor = conn.cursor()
    try:
        # Create the new user
        affected_rows =cursor.execute("INSERT INTO user (username, password) VALUES ('{}', '{}')".format(username, password))
        conn.commit()
        
        # If success
        if affected_rows:
            # Get the user
            user = dbutils.execute_query("SELECT id, username FROM user WHERE username = '{}'".format(username))

    except Exception as exc:
        conn.close()
        return Response("Error trying to create the user: {}".format(exc), 406)
    
    finally:
        conn.close()
        
    return (jsonify({'username': user["username"],'id': user["id"]}), 201)


# ------ /<int:id> ------
@users.route('/<int:id>', methods=['GET'])
#@requires_auth
def get_user(id):
    r = dbutils.execute_query("SELECT * FROM user WHERE id='"+ str(id) + "'")
    if r:
        return jsonify(r)
    else:
        return Response("User not found", 404)


@users.route('/<int:id>', methods=['PUT'])
def edit_user(id):
    return "Not Implemented", 501


@users.route('/<int:id>', methods=['DELETE'])
@requires_auth
def delete_user(id):
    conn = dbutils.get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM user WHERE id={}".format(id))
        conn.commit()
        
    except Exception as exc:
        conn.close()
        return Response("Error trying to delete the user: {}".format(exc), 406)

    finally:
        conn.close()
    
    return Response("User deleted", 200)
