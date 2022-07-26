from crypt import methods
from flask import Flask, request, session
import time, base64, hmac, hashlib, json, requests
api_key = "api_key"
api_secret = "api_secret"
api_passphrase = "api_passphrase"

now = int(time.time() * 1000)
passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())



# Get account information
url_get_account = 'https://api.kucoin.com/api/v1/accounts'
str_to_sign = str(now) + 'GET' + '/api/v1/accounts'
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())

response = requests.request('get', url, headers=headers)


app = Flask(__name__)


@app.route("/api/signup", methods=['POST'])
def signup():
    session.clear()
    # Sign into account
    data = {"type": "main",
            "currency": "BTC"}
    data_json = json.dumps(data)
    url_sign_in = 'https://api.kucoin.com/api/v1/accounts'
    str_to_sign = str(int(time.time() * 1000)) + 'POST' + '/api/v1/accounts'
    signature = base64.b64encode(hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
    headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": passphrase,
    "KC-API-KEY-VERSION": "2"
    }

    response = requests.request('get', url_sign_in, headers=headers)
    print(response.text)
