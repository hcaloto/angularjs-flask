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

@attr('users')
class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""
    
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_users_get_all(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}
        response = tester.get('/users/',
                                data=json.dumps(payload),
                                headers=headers)
        self.assertEqual(response.status_code, 501)


    def test_users_get_someone(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}
        response = tester.get('/users/1',
                                data=json.dumps(payload),
                                headers=headers)
        self.assertEqual(response.status_code, 404)


    def test_users_get_unexistent(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}
        response = tester.get('/users/100000',
                                data=json.dumps(payload),
                                headers=headers)
        self.assertEqual(response.status_code, 404)


    def test_users_edit_someone(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}
        response = tester.put('/users/1',
                                data=json.dumps(payload),
                                headers=headers)
        self.assertEqual(response.status_code, 501)


    def test_users_delete_someone(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}
        
        
    def test_users_create_and_delete_someone(self):
        payload = {'username': 'hcaloto_test5', 'password': 'mypass'}
        response = tester.post('/users/',
                                 data=json.dumps(payload),
                                 headers=headers)
        self.assertEqual(response.status_code, 201)

        jdata = json.loads(response.data)        
        new_id = jdata["id"]
        response = tester.delete('/users/{}'.format(new_id),
                                data=json.dumps(payload),
                                headers=headers)
        self.assertEqual(response.status_code, 200)

        
    def test_users_create_nojson(self):
        payload = {'username': 'hcaloto', 'password': 'mypass'}
        response = tester.post('/users/',
                                      data=payload)
        self.assertEqual(response.status_code, 400)

 
