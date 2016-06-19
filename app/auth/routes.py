# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    app/auth/routes
#

from app.auth.utils import bad_request, unauthorized
from app.auth.utils import check_auth, generate_auth_token, update_token

from flask import Blueprint
from flask import request, jsonify
from flask import Response

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    if not hasattr(request, 'json') or not request.json:
        return bad_request("JSON required")

    username = request.json.get('username')
    password_or_token = request.json.get('password')

    if not username or not password_or_token:
        return unauthorized()
    
    user = check_auth(username, password_or_token)
    if not user:
        return unauthorized()

    token = generate_auth_token(30000)
    update_token(username, token)
    
    return jsonify({'username': user["username"], 'token': token.decode('ascii'), 'duration': 600})



@auth.route('/logout', methods=['POST'])
def logout():
    return Response("OK", 200)


# @auth.route('/token', methods=['GET', 'POST'])
# @requires_auth
# def get_auth_token():
#     token = g.user.generate_auth_token(600)
#     return jsonify({'token': token.decode('ascii'), 'duration': 600})


