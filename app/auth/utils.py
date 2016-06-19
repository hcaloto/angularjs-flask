# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    app/auth/utils.py
#

from functools import wraps
from flask import request, Response, jsonify
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

from app import app
from app.utils import dbutils

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        username = None
        password = None        
        token = None

        # Look for a token
        if request.headers.has_key('Authorization'):
            token = request.headers['Authorization']
            if check_token(token):
                return f(*args, **kwargs)

        # If not token is given, look for username and password
        if not token:
            if not hasattr(request, 'json') or not request.json:
                return unauthorized()
            
            username = request.json.get('username')
            password = request.json.get('password')

            if username and password and check_auth(username, password):
                return f(*args, **kwargs)

        return unauthorized()

    return decorated


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    r = dbutils.execute_query("SELECT * FROM user WHERE username='"+ username +"' AND (password='"+ password +"')")

    return r if r else False


def check_token(token):
    r = dbutils.execute_query("SELECT * FROM user WHERE token='"+ token +"'")

    return r if r else False
    

def update_token(username, token):

    conn = dbutils.get_connection()
    cursor = conn.cursor()
    try:
        # Create the new user
        affected_rows = cursor.execute("UPDATE user SET token='{}' WHERE username='{}'".format(token, username))
        conn.commit()
        
    except Exception as exc:
        return Response("Error trying to update the token: {}".format(exc), 406)
    
    finally:
        conn.close()

    return True


def fetchoneDict(cursor):
    row = cursor.fetchone()

    if row is None: return None
    cols = [ d[0] for d in cursor.description ]
    return dict(zip(cols, row))
    
def generate_auth_token(self, id=None, expiration=600):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': id})


def unauthorized():
    """Sends a 401 response that enables basic auth"""
    return Response("Unautorized", 401)

def bad_request(msg):
    """Sends a 400 response that enables basic auth"""
    return Response(msg, 400)


