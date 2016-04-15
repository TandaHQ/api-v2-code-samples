#Tanda API Methods with HTTParty
require 'httparty'

def authenticate(username, password, scope)
  base_url = "https://my.tanda.co/api/oauth/token"
  body = {username: username, password: password, scope: scope, grant_type: "password"}
  headers = {"Cache-Control" => "no-cache"}

  data = HTTParty.post(base_url, :headers => headers, :query => body).parsed_response

  token = data["access_token"]

end

def query(extension, token)
  base_url = "https://my.tanda.co/api/v2/"
  auth = "Bearer " + token
  headers = {"Cache-Control"=> "no-cache", "Authorization"=> auth}

  data = HTTParty.get(base_url + extension, :headers => headers).parsed_response
end

def post(extension, body, token)
  base_url = "https://my.tanda.co/api/v2/"
  auth = "Bearer " + token
  headers = {"Content-Type"=> "application/json", "Authorization"=> auth}

  HTTParty.post(base_url + extension, :headers => headers, :query => body)

end

def update(extension, body, token)
  base_url = "https://my.tanda.co/api/v2/"
  auth = "Bearer " + token
  headers = {"Content-Type"=> "application/json", "Authorization"=> auth}

  HTTParty.put(base_url + extension, :headers => headers, :query => body)

end