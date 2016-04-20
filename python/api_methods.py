### Methods for API using Python

import requests

def authenticate(username, password, scope = 'me'):
  url = 'https://my.tanda.co/api/oauth/token'
  body = {'username': username, 'password': password, 'scope': scope, 'grant_type': 'password'}
  headers = {'Cache-Control': 'no-cache'}
  data  = requests.post(url, params=body, headers=headers)
  token = eval(data.content).get('access_token')
  return token

token = authenticate(USERNAME, PASSWORD)
print token