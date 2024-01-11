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
    payload = request.json.get('payload')

    # the payload includes whitespace, so we need to remove it for the signatures to match up
    formatted_payload = json.dumps(payload, separators=(',', ':'))

    signature = request.headers.get('X-Hook-Signature')
    computed_signature = hmac.new(security_token.encode(), formatted_payload.encode(), hashlib.sha1).hexdigest()

    print("Signature: ", signature)
    print("Actual Signature: ", computed_signature)
    print("Payload: ", json.dumps(payload, indent=4))

    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=3000)
