'''
Python methods for Tanda API.  You will need to install Requests: HTTP for Humans
pip install requests
http://docs.python-requests.org/en/master/
'''
import requests

# Creates new token based on Tandau sername, password and scope
# You can view your tokens here https://my.tanda.co/api/oauth/access_tokens
# View available scopes https://my.tanda.co/api/v2/documentation#header-scopes
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


#Get a Token which you will use to authenticate yourself
#Seperate scopes with spaces or leave blank for default scope
token = authenticate(USERNAME,PASSWORD,"user me")

#Use token to get information about your user.
user = get("users/me",token)

#Print the content of the request i.e. user details
print user.content