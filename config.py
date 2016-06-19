# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    config.py
#

class Config:
    SECRET_KEY = '... draft ...'
    
    # MYSQL 
    MYSQL_DATABASE_HOST = "localhost"
    MYSQL_DATABASE_USER = "developer"
    MYSQL_DATABASE_PASSWORD = "default"
    MYSQL_DATABASE_DB = "test"
    MYSQL_USE_UNICODE = False    

    DEBUG=False
    
class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass



config = {
    'development' : DevConfig,
    'production' : ProdConfig
}
