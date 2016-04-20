# Tanda API Methods with HTTParty
# You will need to install HTTParty. `gem install httparty`
require 'httparty'

# Creates new token based on Tanda username, password and scope
# You can view your tokens here https://my.tanda.co/api/oauth/access_tokens
# View available scopes https://my.tanda.co/api/v2/documentation#header-scopes
def authenticate(username, password, scope)
  base_url = "https://my.tanda.co/api/oauth/token"
  body = {username: username, password: password, scope: scope, grant_type: "password"}
  headers = {"Cache-Control" => "no-cache"}

  data = HTTParty.post(base_url, :headers => headers, :query => body).parsed_response

  data["access_token"]
end


def get(extension, token)
  base_url = "https://my.tanda.co/api/v2/"
  auth = "Bearer " + token
  headers = {"Cache-Control"=> "no-cache", "Authorization"=> auth}

  HTTParty.get(base_url + extension, :headers => headers).parsed_response
end

def post(extension, body, token)
  base_url = "https://my.tanda.co/api/v2/"
  auth = "Bearer " + token
  headers = {"Content-Type"=> "application/json", "Authorization"=> auth}
  
  HTTParty.post(base_url + extension, :headers => headers, :query => body)
end

def put(extension, body, token)
  base_url = "https://my.tanda.co/api/v2/"
  auth = "Bearer " + token
  headers = {"Content-Type"=> "application/json", "Authorization"=> auth}

  HTTParty.put(base_url + extension, :headers => headers, :query => body)
end

def delete(extension, token)
  base_url = "https://my.tanda.co/api/v2/"
  auth = "Bearer " + token
  headers = {"Content-Type"=> "application/json", "Authorization"=> auth}

  HTTParty.delete(base_url + extension, :headers => headers)
end

#Get a token which you will use to authenticate yourself
#Seperate scopes with spaces
token = authenticate(USERNAME, PASSWORD, "user me")

#Use token to get information about your user.
user = get("users/me", token)

puts user
