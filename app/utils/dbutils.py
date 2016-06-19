# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    app/utils/dbutils
#

from app import mysql


def check_connection():
    """ Tests MySQL connection """
    conn = mysql.connect()
    return conn.close()


def get_connection():
    """ Tests MySQL connection """
    return mysql.connect()


def get_cursor():
    """ Get a MySQL cursor """
    cursor = mysql.connect().cursor()
    return cursor
    

def execute_query(query):
    """ Execute a given query """
    data = None
    cursor = get_cursor()

    try:
        cursor.execute(query)
        data = fetchone_as_dict(cursor)
    except Exception as exc:
        print "EXCEPTION on execute_query", exc

    cursor.close()

    return data


def fetchone_as_dict(cursor):
    row = cursor.fetchone()

    if row is None: return None
    cols = [ d[0] for d in cursor.description ]
    return dict(zip(cols, row))


def insert_row(table, **data):
    cursor = get_cursor()
    
    keys = ', '.join(data.keys())
    vals = ', '.join(["%s"] * len(data.values()))
    query = "INSERT INTO %s (%s) VALUES (%s)" % (table, keys, vals)

    try:
        cursor.execute(query, tuple(data.values()))
    except Exception as exc:
        print "EXCEPTION on insert_row", exc
        return None
    
    return cursor.lastrowid


def get_row(table, data):
    cursor = get_cursor()

    keys = ""


    k,v = data.keys()[0], data.values()[0]
    conditions = "{}='{}'".format(k,v)
    keys = keys + k
    data.pop(k, v)
    
    for key, value in data.iteritems():
        keys.append(key)
        conditions = conditions + " AND {}='{}'".format(key, value)
        
    qq = "SELECT %s FROM %s WHERE %s" % (keys, table, conditions)
    cursor.execute(qq, tuple(data.values()+[id]))

    data = fetchone_as_dict(cursor)
    return data
