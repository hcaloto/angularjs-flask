# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    app/__init__.py
#

import unittest
import requests
import json

from nose.plugins.attrib import attr
from app import app

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
tester = app.test_client()

@attr('auth')
class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""
    
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_auth_login(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}

        # Authenticate using username and password
        response = tester.post('/auth/login',
                                 data=json.dumps(payload),
                                 headers=headers)

        jdata = json.loads(response.data)
        username = jdata["username"]
        token = json.loads(response.data)['token']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(username, 'hcaloto')

        # Authenticate using token
        headers_full = dict(headers)
        headers_full.update({'Authorization': '{}'.format(token)})
        response = tester.get('/users/1',
                                 headers=headers_full)

        self.assertEqual(response.status_code, 404)


    def test_auth_logout(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}

        # Authenticate using username and password
        response = tester.post('/auth/logout',
                               data=json.dumps(payload),
                               headers=headers)

        self.assertEqual(response.status_code, 200)

        
    def test_auth_erroneous(self):
        payload = {'username': 'hcaloto', 'password': 'erroneous'}

        # Authenticate using username and password
        response = tester.post('/auth/login',
                                 data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 401)
 

    def test_auth_no_json(self):
        payload = {'username': 'hugo', 'password': 'python'}

        # Authenticate using username and password
        response = tester.post('/auth/login',
                               data=payload,
                               headers=headers)

        self.assertEqual(response.status_code, 400)


    def test_auth_no_username(self):
        payload = {'': 'hugo', 'password': 'python'}

        # Authenticate using username and password
        response = tester.post('/auth/login',
                               data=json.dumps(payload),
                               headers=headers)

        self.assertEqual(response.status_code, 401)

        # Authenticate using username and password
        payload = {'username': '', 'password': 'python'}
        response = tester.post('/auth/login',
                               data=json.dumps(payload),
                               headers=headers)

        self.assertEqual(response.status_code, 401)
