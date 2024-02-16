#
# pip3 install Flask
# python3 webhook.py
#

from flask import Flask, request, jsonify
import hashlib
import hmac
import json

app = Flask(__name__)
security_token = 'tandawebhooktest'

@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data()

    signature = request.headers.get('X-Webhook-Signature')
    computed_signature = hmac.new(security_token.encode(), payload.encode(), hashlib.sha1).hexdigest()

    print("Signature: ", signature)
    print("Actual Signature: ", computed_signature)

    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=3000)
