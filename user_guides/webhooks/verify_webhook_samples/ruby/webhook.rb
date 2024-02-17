#
# gem install sinatra awesome_print
# ruby webhook.rb
#

require "sinatra"
require "awesome_print" # pretty printing using `ap` instead of `puts`

post '/' do
  # return response success with no content
  status 204

  signature = request.env["HTTP_X_WEBHOOK_SIGNATURE"]
  payload = request.body.read
  security_token = "tandawebhooktest"
  actual_signature = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new("sha1"), security_token, payload)

  ap "Signature: #{signature}"
  ap "Actual Signature: #{actual_signature}"

  # Pretty print webhook payload
  ap payload
end
