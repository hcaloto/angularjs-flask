# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    app/__init__.py
#

import os
from flask import Flask
from flask.ext.mysql import MySQL

from config import config


# Initialization
mysql = MySQL()
app = Flask(__name__)


def create_app(config_name='development'):
    # Load config
    app.config.from_object(config[config_name])
    print "Config in use: {}".format(config_name)

    # Register blueprints
    from app.auth.routes import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from app.users.routes import users
    app.register_blueprint(users, url_prefix='/users')

    from app.server.routes import server
    app.register_blueprint(server)

    # Init MySQL app
    mysql.init_app(app)

    # Test MySQL connection
    from app.utils import dbutils
    dbutils.check_connection()
        
    return app


