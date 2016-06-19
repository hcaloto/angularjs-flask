# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    app/auth/controllers
#

from flask import redirect, url_for
from flask import Blueprint

server = Blueprint('server', __name__)

@server.route('/', endpoint="index_html")
@server.route('/index.html')
#@authentication.login_required
def index():
    return redirect(url_for('static', filename='index.html'))
