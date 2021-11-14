#!/usr/bin/env python
from datetime import datetime


from decimal import *

import collections
import os
import time
import array as arr

import json
  
import hashlib
import hmac
import json
import requests
from pprint import pprint
API_HOST = 'https://api.bitkub.com'
API_KEY = '678e6fcb5522750ab8584593ea047d8a'
API_SECRET = b'0caba33e0fa3d46eda43f7c29560724b'
def json_encode(data):
	return json.dumps(data, separators=(',', ':'), sort_keys=True)

def sign(data):
	j = json_encode(data)
	#print('Signing payload: ' + j)
	h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
	return h.hexdigest()

# check server time
response = requests.get(API_HOST + '/api/servertime')
ts = int(response.text)
print('Server time: ' + response.text)

# check balances
header = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'X-BTK-APIKEY': API_KEY,
}
data = {
    'sym':'THB_ETH',
	'ts': ts,
}
signature = sign(data)
data['sig'] = signature

print('Payload with signature: ' + json_encode(data))
response = requests.post(API_HOST + '/api/market/my-open-orders', headers=header, data=json_encode(data))

print('my-open-orders: ' + response.text)

data = response.json()
data = data['result']  

for d in data: 
    print(d['hash'])
    data = {
    'hash':d['hash'],
	'ts': ts,
	}
    signature = sign(data)
    data['sig'] = signature
    print('Payload with signature: ' + json_encode(data))
    response = requests.post(API_HOST + '/api/market/cancel-order', headers=header, data=json_encode(data))
    #print(response)