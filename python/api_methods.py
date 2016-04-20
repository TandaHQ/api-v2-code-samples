### Methods for API using Python

import requests

def authenticate(username, password, scope = 'me'):
  url = 'https://my.tanda.co/api/oauth/token'
  body = {'username': username, 'password': password, 'scope': scope, 'grant_type': 'password'}
  headers = {'Cache-Control': 'no-cache'}
  data  = requests.post(url, params=body, headers=headers)
  token = eval(data.content).get('access_token')
  return token

def get(extension, token):
  base_url = 'https://my.tanda.co/api/v2/'
  auth = 'Bearer ' + token
  headers = {'Cache-Control': 'no-cache', 'Authorization': auth}
  data = requests.get(base_url + extension, headers=headers)
  return data

def post(extension, params, token):
  base_url = 'https://my.tanda.co/api/v2/'
  auth = 'Bearer ' + token
  headers = {'Content-Type': 'application/json', 'Authorization': auth}
  requests.post(base_url + extension, params=params, headers=headers)

def put(extension, params, token):
  base_url = 'https://my.tanda.co/api/v2/'
  auth = 'Bearer ' + token
  headers = {'Content-Type': 'application/json', 'Authorization': auth}
  requests.put(base_url + extension, params=params, headers=headers)

def delete(extension, token):
  base_url = 'https://my.tanda.co/api/v2/'
  auth = 'Bearer ' + token
  headers = {'Content-Type': 'application/json', 'Authorization': auth}
  requests.delete(base_url + extension, headers=headers)


token = authenticate(USERNAME, PASSWORD)
print token