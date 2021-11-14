#!/usr/bin/env python
import ccxt
import config
import schedule
import time
import pandas as pd
import logging
from datetime import datetime


from decimal import *

import time
import array as arr

  
import hashlib
import hmac
import json
import requests
from pprint import pprint

import collections
import os

import array as arr


import math
import json


import logging


pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np


exchange = ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})

    

def take_order_sell_coin_perp_p(markett):
    


    API_HOST = 'https://api.bitkub.com'
    API_KEY = '678e6fcb5522750ab8584593ea047d8a'
    API_SECRET = b'0caba33e0fa3d46eda43f7c29560724b'

    def json_encode(data):
        return json.dumps(data, separators=(',', ':'), sort_keys=True)

    def sign(data):
        j = json_encode(data)
        print('Signing payload: ' + j)
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
        'ts': ts,
    }
    signature = sign(data)
    data['sig'] = signature

    print('Payload with signature: ' + json_encode(data))
    response = requests.post(API_HOST + '/api/market/balances', headers=header, data=json_encode(data))

    print('Balances: ' + response.text)

    data = response.json()
    data = data['result']
    if markett == "THB_BNB":
        markett = 'BNB'
    elif markett == "THB_ADA":
        markett = 'ADA'
    elif markett == "THB_DOGE":
        markett = 'DOGE'    
    elif markett == "THB_KUB":
        markett = 'KUB'    
    elif markett == "THB_XLM":
        markett = 'XLM'    
    elif markett == "THB_ZIL":
        markett = 'ZIL' 
    elif markett == "THB_IOST":
        markett = 'IOST' 
    elif markett == "THB_JFIN":
        markett = 'JFIN' 
    elif markett == "THB_SNT":
        markett = 'SNT' 
    elif markett == "THB_XRP":
        markett = 'XRP' 
    elif markett == "THB_CVC":
        markett = 'CVC' 
    elif markett == "THB_ABT":
        markett = 'ABT' 
    elif markett == "THB_POW":
        markett = 'POW' 
    elif markett == "THB_BAT":
        markett = 'BAT' 
    elif markett == "THB_USDT":
        markett = 'USDT' 
    elif markett == "THB_USDC":
        markett = 'USDC' 
    elif markett == "THB_ALPHA":
        markett = 'ALPHA' 
    elif markett == "THB_ETH":
        markett = 'ETH' 
    elif markett == "THB_BTC":
        markett = 'BTC' 
    elif markett == "THB_BAND":
        markett = 'BAND' 
    elif markett == "THB_NEAR":
        markett = 'NEAR' 
    unit_avl = data[markett]['available']

    if (markett == "ADA" and unit_avl >= 2):
        # f = open ('adathb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['ADA']['SHORT'] + data['ADA']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_ADA',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature

        print('Payload with signature: ' + json_encode(order_data))
        #if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "BNB" and unit_avl >= 0.01):
        # f = open ('bnbthb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['BNB']['SHORT'] + data['BNB']['short']
        # f.close()             
        order_data = {
            'sym': 'THB_BNB',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature

        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "DOGE" and unit_avl >= 20):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_DOGE',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "KUB" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_KUB',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "XLM" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_XLM',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "ZIL" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_ZIL',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "IOST" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_IOST',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "JFIN" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_JFIN',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "SNT" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_SNT',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "XRP" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_XRP',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "CVC" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_CVC',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "ABT" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_ABT',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "POW" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_POW',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "BAT" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_BAT',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "USDT" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_USDT',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "USDC" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_USDC',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "ALPHA" and unit_avl >= 1):
        # f = open ('dogethb.json', "r")

        # data = json.loads(f.read())
        # res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
        # f.close() 
        order_data = {
            'sym': 'THB_ALPHA',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "ETH" and unit_avl >= 0.001):

        order_data = {
            'sym': 'THB_ETH',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "BTC" and unit_avl >= 0.001):

        order_data = {
            'sym': 'THB_BTC',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "BAND" and unit_avl >= 0.5):

        order_data = {
            'sym': 'THB_BAND',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)
    elif (markett == "NEAR" and unit_avl >= 0.5):

        order_data = {
            'sym': 'THB_NEAR',
            'amt': unit_avl, # amount you want to sell
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        order_signature = sign(order_data)
        order_data['sig'] = order_signature
        print('Payload with signature: ' + json_encode(order_data))
        # if (res_val == 11):
        response_order = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(order_data))


        print('Response Order: ' + response_order.text)

    return


def take_order_buy_coin_perp_p(markett):



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
        'ts': ts,
    }
    signature = sign(data)
    data['sig'] = signature

    print('Payload with signature: ' + json_encode(data))
    response = requests.post(API_HOST + '/api/market/balances', headers=header, data=json_encode(data))

    print('Balances: ' + response.text)

    data = response.json()
    data = data['result']
    if markett == "THB_BNB":
        markett = 'BNB'
    elif markett == "THB_ADA":
        markett = 'ADA'
    elif markett == "THB_DOGE":
        markett = 'DOGE'        
    elif markett == "THB_KUB":
        markett = 'KUB'   
    elif markett == "THB_XLM":
        markett = 'XLM'  
    elif markett == "THB_ZIL":
        markett = 'ZIL'  
    elif markett == "THB_IOST":
        markett = 'IOST'  
    elif markett == "THB_JFIN":
        markett = 'JFIN' 
    elif markett == "THB_CVC":
        markett = 'CVC'   
    elif markett == "THB_XRP":
        markett = 'XRP' 
    elif markett == "THB_USDT":
        markett = 'USDT' 
    elif markett == "THB_USDC":
        markett = 'USDC' 
    elif markett == "THB_BAT":
        markett = 'BAT' 
    elif markett == "THB_POW":
        markett = 'POW' 
    elif markett == "THB_ABT":
        markett = 'ABT' 
    elif markett == "THB_ALPHA":
        markett = 'ALPHA' 
    elif markett == "THB_SNT":
        markett = 'SNT' 
    elif markett == "THB_ETH":
        markett = 'ETH' 
    elif markett == "THB_BTC":
        markett = 'BTC' 
    elif markett == "THB_BAND":
        markett = 'BAND' 
    elif markett == "THB_NEAR":
        markett = 'NEAR' 
    unit_avl = data[markett]['available']

    if (markett == "ADA" and unit_avl < 1):
        f = open ('adathb.json', "r")

        data = json.loads(f.read())
        res_val = data['ADA']['LONG'] + data['ADA']['long']
        f.close() 

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
        buy_data = {
            'sym': 'THB_ADA',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "BNB" and unit_avl < 0.01):
        f = open ('bnbthb.json', "r")

        data = json.loads(f.read())
        res_val = data['BNB']['LONG'] + data['BNB']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_BNB',
            'amt': 2000, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "DOGE" and unit_avl < 20):
        f = open ('dogethb.json', "r")

        data = json.loads(f.read())
        res_val = data['DOGE']['LONG'] + data['DOGE']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_DOGE',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)

    elif (markett == "KUB" and unit_avl < 1):
        f = open ('kubthb.json', "r")

        data = json.loads(f.read())
        res_val = data['KUB']['LONG'] + data['KUB']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_KUB',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "XLM" and unit_avl < 1):
        f = open ('xlmthb.json', "r")

        data = json.loads(f.read())
        res_val = data['XLM']['LONG'] + data['XLM']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_XLM',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "XRP" and unit_avl < 1):
        f = open ('xrpthb.json', "r")

        data = json.loads(f.read())
        res_val = data['XRP']['LONG'] + data['XRP']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_XRP',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "BAT" and unit_avl < 1):
        f = open ('batthb.json', "r")

        data = json.loads(f.read())
        res_val = data['BAT']['LONG'] + data['BAT']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_BAT',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "CVC" and unit_avl < 1):
        f = open ('cvcthb.json', "r")

        data = json.loads(f.read())
        res_val = data['CVC']['LONG'] + data['CVC']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_CVC',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "IOST" and unit_avl < 1):
        f = open ('iostthb.json', "r")

        data = json.loads(f.read())
        res_val = data['IOST']['LONG'] + data['IOST']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_IOST',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "JFIN" and unit_avl < 1):
        f = open ('jfinthb.json', "r")

        data = json.loads(f.read())
        res_val = data['JFIN']['LONG'] + data['JFIN']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_JFIN',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "POW" and unit_avl < 1):
        f = open ('powthb.json', "r")

        data = json.loads(f.read())
        res_val = data['POW']['LONG'] + data['POW']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_POW',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "USDT" and unit_avl < 1):
        f = open ('usdtthb.json', "r")

        data = json.loads(f.read())
        res_val = data['USDT']['LONG'] + data['USDT']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_USDT',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "USDC" and unit_avl < 1):
        f = open ('usdcthb.json', "r")

        data = json.loads(f.read())
        res_val = data['USDC']['LONG'] + data['USDC']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_USDC',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "ABT" and unit_avl < 1):
        f = open ('abtthb.json', "r")

        data = json.loads(f.read())
        res_val = data['ABT']['LONG'] + data['ABT']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_ABT',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "ALPHA" and unit_avl < 1):
        f = open ('alphathb.json', "r")

        data = json.loads(f.read())
        res_val = data['ALPHA']['LONG'] + data['ALPHA']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_ALPHA',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "ZIL" and unit_avl < 1):
        f = open ('zilthb.json', "r")

        data = json.loads(f.read())
        res_val = data['ZIL']['LONG'] + data['ZIL']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_ZIL',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "SNT" and unit_avl < 1):
        f = open ('sntthb.json', "r")

        data = json.loads(f.read())
        res_val = data['SNT']['LONG'] + data['SNT']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_SNT',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "ETH" and unit_avl < 0.001):
        f = open ('eththb.json', "r")

        data = json.loads(f.read())
        res_val = data['ETH']['LONG'] + data['ETH']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_ETH',
            'amt': 1000, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "BTC" and unit_avl < 0.0001):
        f = open ('btcthb.json', "r")

        data = json.loads(f.read())
        res_val = data['BTC']['LONG'] + data['BTC']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_BTC',
            'amt': 2000, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "BAND" and unit_avl < 0.5):
        f = open ('bandthb.json', "r")

        data = json.loads(f.read())
        res_val = data['BAND']['LONG'] + data['BAND']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_BAND',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)
    elif (markett == "NEAR" and unit_avl < 0.5):
        f = open ('nearthb.json', "r")

        data = json.loads(f.read())
        res_val = data['NEAR']['LONG'] + data['NEAR']['long']
        f.close() 
        buy_data = {
            'sym': 'THB_NEAR',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        if (res_val== 3):
            response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

            print('Response: ' + response.text)

    return

def tr(data):
    data['previous_close'] = data['close'].shift(1)
    data['high-low'] = abs(data['high'] - data['low'])
    data['high-pc'] = abs(data['high'] - data['previous_close'])
    data['low-pc'] = abs(data['low'] - data['previous_close'])

    tr = data[['high-low', 'high-pc', 'low-pc']].max(axis=1)

    return tr

def atr(data, period):
    data['tr'] = tr(data)
    atr = data['tr'].rolling(period).mean()

    return atr

def supertrend(df, period=7, atr_multiplier=3.5):
    hl2 = (df['high'] + df['low']) / 2
    df['atr'] = atr(df, period)
    #df['upperbandHMA'] = ta.hma(hl2 + (atr_multiplier * df['atr']),length=5)
    #df['lowerbandHMA'] = ta.hma(hl2 - (atr_multiplier * df['atr']),length=5)
    #df['HMA20'] = ta.hma(df['close'],length=20)
    #df['HMA9'] = ta.hma(df['close'],length=9)
    df['upperband'] = hl2 + (atr_multiplier * df['atr'])
    df['lowerband'] = hl2 - (atr_multiplier * df['atr'])
    #df['meantrend'] = (df['upperband']+df['lowerband'])/2
    #df['meantrendHMA'] = (df['upperbandHMA']+df['lowerbandHMA'])/2
    df['in_uptrend'] = True
    df['in_uptrendADX'] = True
    #df['in_uptrendHMA'] = True
    supertest = df.ta.supertrend(length=7,multiplier=3.5)
    adx = df.ta.adx(length=9)
    df = pd.concat([df,supertest['SUPERTd_7_3.5'],adx],axis=1)

    for current in range(1, len(df.index)):
        # if df['ADX_9'][current] >= 14: 
        #     if df['DMP_9'][current] > df['DMN_9'][current]: 
        #         df['in_uptrendADX'][current]=True        
        #     if df['DMP_9'][current] < df['DMN_9'][current]:
        #         df['in_uptrendADX'][current]=False

        if df['ADX_9'][current] >= 19 and df['ADX_9'][current] <= 41: 
            if df['DMP_9'][current] > df['DMN_9'][current]: 
                df['in_uptrendADX'][current]=True        
            elif df['DMP_9'][current] < df['DMN_9'][current]:
                df['in_uptrendADX'][current]=False
            elif df['DMP_9'][current] > df['ADX_9'][current] and df['DMP_9'][current] > df['DMN_9'][current]: 
                df['in_uptrendADX'][current]=True        
            elif df['DMN_9'][current] > df['ADX_9'][current] and df['DMP_9'][current] < df['DMN_9'][current]:
                    df['in_uptrendADX'][current]=False 

        if df['SUPERTd_7_3.5'][current] == 1: 
            df['in_uptrend'][current]=True
        else: 
            df['in_uptrend'][current]=False
        if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
            df['in_uptrend'][current]=True
        elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
            df['in_uptrend'][current]=False   

        
        
    return df


in_position = False

def check_buy_sell_signals(df):
    global in_position
    self=None
    print("checking for buy and sell signals")
    print(df.tail(5))
    last_row_index = len(df.index) - 1
    previous_row_index = last_row_index - 1

    if not df['in_uptrend'][previous_row_index] and df['in_uptrend'][last_row_index]:
        print("changed to uptrend, buy")
        if not in_position:
            #order = exchange.create_market_buy_order('ETH/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
            #close_order_sell_coin_usdt(self,'ADAUSDT')
            order = take_order_sell_coin_perp_p('THB_POW')
            print(order)
            in_position = True
        else:
            print("already in position, nothing to do")
    
    if df['in_uptrend'][previous_row_index] and not df['in_uptrend'][last_row_index]:
        if in_position:
            print("changed to downtrend, sell")
            #close_order_buy_coin_usdt(self,'ADAUSDT')
            order = take_order_sell_coin_perp_p('THB_POW')
            print(order)
            in_position = False
        else:
            print("You aren't in position, nothing to sell")

def run_bot():
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv('POW/USDT', timeframe='5m', limit=288)
    print("THB_POW")
    #bars = sub_client.subscribe_candlestick_event("bnbusdt", CandlestickInterval.MIN30, callback, error)
    df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')


    supertrend_data = supertrend(df)
    
    check_buy_sell_signals(supertrend_data)


schedule.every(10).seconds.do(run_bot)


while True:
    schedule.run_pending()
    time.sleep(1)