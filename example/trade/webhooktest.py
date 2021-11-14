#!/usr/bin/env python
from flask import Flask, request, abort

from binance_f import RequestClient

from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
from make_order_coin_bnb import take_order_coin_perp
#from make_order_coin_bitkub import take_order_bitkub


from datetime import datetime
from binance.client import Client


from decimal import *
import email
import imaplib
import collections
import os
import time
import array as arr
import threading
import datetime
import math
import json


import logging
import argparse
import subprocess
  
  
import hashlib
import hmac
import json
import requests
from pprint import pprint

detach_dir = 'c:\db'
# class take_order_bitkub:
    
#     def __init__(self,markett):
#         self.markett = markett
    

def take_order_sell_coin_perp_p(self,markett):



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
    #print('Server time: ' + response.text)

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

    #print('Payload with signature: ' + json_encode(data))
    response = requests.post(API_HOST + '/api/market/balances', headers=header, data=json_encode(data))

    #print('Balances: ' + response.text)

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


def take_order_buy_coin_perp_p(self,markett):



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

def update_long1(p1,markett):

    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['LONG'] = p1 
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['LONG'] = p1 
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['LONG'] = p1 
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['LONG'] = p1 
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['LONG'] = p1 
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['LONG'] = p1 
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['LONG'] = p1 
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['LONG'] = p1 
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['LONG'] = p1 
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['LONG'] = p1 
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['LONG'] = p1 
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['LONG'] = p1 
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['LONG'] = p1 
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['LONG'] = p1 
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['LONG'] = p1 
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['LONG'] = p1 
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['LONG'] = p1 
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['LONG'] = p1 
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['LONG'] = p1 
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['LONG'] = p1 
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['LONG'] = p1 
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['LONG'] = p1 
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ATOMUSDT"):
        with open("atom.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ATOM']['LONG'] = p1
        with open("atom.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ICPUSDT"):
        with open("icp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ICP']['LONG'] = p1
        with open("icp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOTUSDT"):
        with open("dot.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOT']['LONG'] = p1
        with open("dot.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSDT"):
        with open("doge.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['LONG'] = p1
        with open("doge.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "WAVESUSDT"):
        with open("waves.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['WAVES']['LONG'] = p1
        with open("waves.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['LONG'] = p1
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSD_PERP"):
        with open("adausd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['LONG'] = p1
        with open("adausd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "BNBUSD_PERP"):
        with open("bnbusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['LONG'] = p1
        with open("bnbusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSD_PERP"):
        with open("dogeusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['LONG'] = p1
        with open("dogeusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_ADA"):
        with open("adathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['LONG'] = p1
        with open("adathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_BNB"):
        with open("bnbthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['LONG'] = p1
        with open("bnbthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_DOGE"):
        with open("dogethb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['LONG'] = p1
        with open("dogethb.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    elif markett == "THB_KUB":
        with open("kubthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['KUB']['LONG'] = p1
        with open("kubthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XLM":
        with open("xlmthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XLM']['LONG'] = p1
        with open("xlmthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)     
    elif markett == "THB_ZIL":
        with open("zilthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZIL']['LONG'] = p1
        with open("zilthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_IOST":
        with open("iostthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['IOST']['LONG'] = p1
        with open("iostthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_JFIN":
        with open("jfinthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['JFIN']['LONG'] = p1
        with open("jfinthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_SNT":
        with open("sntthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SNT']['LONG'] = p1
        with open("sntthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XRP":
        with open("xrpthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['LONG'] = p1
        with open("xrpthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_CVC":
        with open("cvcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['CVC']['LONG'] = p1
        with open("cvcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ABT":
        with open("abtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ABT']['LONG'] = p1
        with open("abtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_POW":
        with open("powthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['POW']['LONG'] = p1
        with open("powthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_BAT":
        with open("batthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAT']['LONG'] = p1
        with open("batthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDT":
        with open("usdtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDT']['LONG'] = p1
        with open("usdtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDC":
        with open("usdcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDC']['LONG'] = p1
        with open("usdcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_ALPHA":
        with open("alphathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ALPHA']['LONG'] = p1
        with open("alphathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ETH":
        with open("eththb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['LONG'] = p1
        with open("eththb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BTC":
        with open("btcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['LONG'] = p1
        with open("btcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BAND":
        with open("bandthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAND']['LONG'] = p1
        with open("bandthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_NEAR":
        with open("nearthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEAR']['LONG'] = p1
        with open("nearthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    return

def update_long2(p2,markett):
    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['long'] = p2
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['long'] = p2
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['long'] = p2
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['long'] = p2
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['long'] = p2
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['long'] = p2
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['long'] = p2
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['long'] = p2
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['long'] = p2
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['long'] = p2
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['long'] = p2
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['long'] = p2
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['long'] = p2
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['long'] = p2
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['long'] = p2
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['long'] = p2
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['long'] = p2
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['long'] = p2
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['long'] = p2
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['long'] = p2
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['long'] = p2
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['long'] = p2
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ATOMUSDT"):
        with open("atom.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ATOM']['long'] = p2
        with open("atom.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ICPUSDT"):
        with open("icp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ICP']['long'] = p2
        with open("icp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOTUSDT"):
        with open("dot.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOT']['long'] = p2
        with open("dot.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSDT"):
        with open("doge.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['long'] = p2
        with open("doge.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "WAVESUSDT"):
        with open("waves.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['WAVES']['long'] = p2
        with open("waves.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['long'] = p2
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSD_PERP"):
        with open("adausd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['long'] = p2
        with open("adausd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "BNBUSD_PERP"):
        with open("bnbusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['long'] = p2
        with open("bnbusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSD_PERP"):
        with open("dogeusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['long'] = p2
        with open("dogeusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_ADA"):
        with open("adathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['long'] = p2
        with open("adathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_BNB"):
        with open("bnbthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['long'] = p2
        with open("bnbthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_DOGE"):
        with open("dogethb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['long'] = p2
        with open("dogethb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif markett == "THB_KUB":
        with open("kubthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['KUB']['long'] = p2
        with open("kubthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XLM":
        with open("xlmthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XLM']['long'] = p2
        with open("xlmthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)     
    elif markett == "THB_ZIL":
        with open("zilthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZIL']['long'] = p2
        with open("zilthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_IOST":
        with open("iostthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['IOST']['long'] = p2
        with open("iostthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_JFIN":
        with open("jfinthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['JFIN']['long'] = p2
        with open("jfinthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_SNT":
        with open("sntthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SNT']['long'] = p2
        with open("sntthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XRP":
        with open("xrpthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['long'] = p2
        with open("xrpthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_CVC":
        with open("cvcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['CVC']['long'] = p2
        with open("cvcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ABT":
        with open("abtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ABT']['long'] = p2
        with open("abtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_POW":
        with open("powthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['POW']['long'] = p2
        with open("powthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_BAT":
        with open("batthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAT']['long'] = p2
        with open("batthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDT":
        with open("usdtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDT']['long'] = p2
        with open("usdtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDC":
        with open("usdcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDC']['long'] = p2
        with open("usdcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_ALPHA":
        with open("alphathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ALPHA']['long'] = p2
        with open("alphathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ETH":
        with open("eththb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['long'] = p2
        with open("eththb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BTC":
        with open("btcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['long'] = p2
        with open("btcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BAND":
        with open("bandthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAND']['long'] = p2
        with open("bandthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_NEAR":
        with open("nearthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEAR']['long'] = p2
        with open("nearthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    return

def update_short1(p3,markett):
    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['SHORT'] = p3
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['SHORT'] = p3
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['SHORT'] = p3
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['SHORT'] = p3
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['SHORT'] = p3
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['SHORT'] = p3
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['SHORT'] = p3
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['SHORT'] = p3 
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['SHORT'] = p3
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['SHORT'] = p3 
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['SHORT'] = p3
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['SHORT'] = p3
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['SHORT'] = p3
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['SHORT'] = p3
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['SHORT'] = p3 
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['SHORT'] = p3
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['SHORT'] = p3
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['SHORT'] = p3
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['SHORT'] = p3
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['SHORT'] = p3 
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['SHORT'] = p3
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['SHORT'] = p3 
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ATOMUSDT"):
        with open("atom.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ATOM']['SHORT'] = p3
        with open("atom.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ICPUSDT"):
        with open("icp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ICP']['SHORT'] = p3
        with open("icp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOTUSDT"):
        with open("dot.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOT']['SHORT'] = p3
        with open("dot.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSDT"):
        with open("doge.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['SHORT'] = p3
        with open("doge.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "WAVESUSDT"):
        with open("waves.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['WAVES']['SHORT'] = p3
        with open("waves.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['SHORT'] = p3
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSD_PERP"):
        with open("adausd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['SHORT'] = p3
        with open("adausd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "BNBUSD_PERP"):
        with open("bnbusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['SHORT'] = p3
        with open("bnbusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSD_PERP"):
        with open("dogeusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['SHORT'] = p3
        with open("dogeusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_ADA"):
        with open("adathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['SHORT'] = p3
        with open("adathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_BNB"):
        with open("bnbthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['SHORT'] = p3
        with open("bnbthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_DOGE"):
        with open("dogethb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['SHORT'] = p3
        with open("dogethb.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    elif markett == "THB_KUB":
        with open("kubthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['KUB']['SHORT'] = p3
        with open("kubthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XLM":
        with open("xlmthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XLM']['SHORT'] = p3
        with open("xlmthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)     
    elif markett == "THB_ZIL":
        with open("zilthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZIL']['SHORT'] = p3
        with open("zilthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_IOST":
        with open("iostthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['IOST']['SHORT'] = p3
        with open("iostthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_JFIN":
        with open("jfinthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['JFIN']['SHORT'] = p3
        with open("jfinthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_SNT":
        with open("sntthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SNT']['SHORT'] = p3
        with open("sntthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XRP":
        with open("xrpthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['SHORT'] = p3
        with open("xrpthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_CVC":
        with open("cvcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['CVC']['SHORT'] = p3
        with open("cvcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ABT":
        with open("abtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ABT']['SHORT'] = p3
        with open("abtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_POW":
        with open("powthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['POW']['SHORT'] = p3
        with open("powthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_BAT":
        with open("batthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAT']['SHORT'] = p3
        with open("batthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDT":
        with open("usdtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDT']['SHORT'] = p3
        with open("usdtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDC":
        with open("usdcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDC']['SHORT'] = p3
        with open("usdcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_ALPHA":
        with open("alphathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ALPHA']['SHORT'] = p3
        with open("alphathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ETH":
        with open("eththb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['SHORT'] = p3
        with open("eththb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BTC":
        with open("btcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['SHORT'] = p3
        with open("btcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BAND":
        with open("bandthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAND']['SHORT'] = p3
        with open("bandthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_NEAR":
        with open("nearthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEAR']['SHORT'] = p3
        with open("nearthb.json", "w") as jsonFile:
            json.dump(data, jsonFile) 


    return

def update_short2(p4,markett):

    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['short'] = p4
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['short'] = p4
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['short'] = p4
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['short'] = p4
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['short'] = p4
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['short'] = p4
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['short'] = p4
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['short'] = p4
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['short'] = p4
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['short'] = p4
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['short'] = p4
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['short'] = p4
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['short'] = p4
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['short'] = p4
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['short'] = p4 
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['short'] = p4
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['short'] = p4
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['short'] = p4
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['short'] = p4
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['short'] = p4 
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['short'] = p4
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['short'] = p4
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            
    elif (markett == "ATOMUSDT"):
        with open("atom.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ATOM']['short'] = p4
        with open("atom.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ICPUSDT"):
        with open("icp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ICP']['short'] = p4
        with open("icp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOTUSDT"):
        with open("dot.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOT']['short'] = p4
        with open("dot.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSDT"):
        with open("doge.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['short'] = p4
        with open("doge.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "WAVESUSDT"):
        with open("waves.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['WAVES']['short'] = p4
        with open("waves.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['short'] = p4
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "ADAUSD_PERP"):
        with open("adausd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['short'] = p4
        with open("adausd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "BNBUSD_PERP"):
        with open("bnbusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['short'] = p4
        with open("bnbusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "DOGEUSD_PERP"):
        with open("dogeusd.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['short'] = p4
        with open("dogeusd.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_ADA"):
        with open("adathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['short'] = p4
        with open("adathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_BNB"):
        with open("bnbthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['short'] = p4
        with open("bnbthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    elif (markett == "THB_DOGE"):
        with open("dogethb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DOGE']['short'] = p4
        with open("dogethb.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    elif markett == "THB_KUB":
        with open("kubthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['KUB']['short'] = p4
        with open("kubthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XLM":
        with open("xlmthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XLM']['short'] = p4
        with open("xlmthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)     
    elif markett == "THB_ZIL":
        with open("zilthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZIL']['short'] = p4
        with open("zilthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_IOST":
        with open("iostthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['IOST']['short'] = p4
        with open("iostthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_JFIN":
        with open("jfinthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['JFIN']['short'] = p4
        with open("jfinthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_SNT":
        with open("sntthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SNT']['short'] = p4
        with open("sntthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_XRP":
        with open("xrpthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['short'] = p4
        with open("xrpthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_CVC":
        with open("cvcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['CVC']['short'] = p4
        with open("cvcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ABT":
        with open("abtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ABT']['short'] = p4
        with open("abtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_POW":
        with open("powthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['POW']['short'] = p4
        with open("powthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_BAT":
        with open("batthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAT']['short'] = p4
        with open("batthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDT":
        with open("usdtthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDT']['short'] = p4
        with open("usdtthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_USDC":
        with open("usdcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['USDC']['short'] = p4
        with open("usdcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_ALPHA":
        with open("alphathb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ALPHA']['short'] = p4
        with open("alphathb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_ETH":
        with open("eththb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['short'] = p4
        with open("eththb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BTC":
        with open("btcthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['short'] = p4
        with open("btcthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)   
    elif markett == "THB_BAND":
        with open("bandthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BAND']['short'] = p4
        with open("bandthb.json", "w") as jsonFile:
            json.dump(data, jsonFile)  
    elif markett == "THB_NEAR":
        with open("nearthb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEAR']['short'] = p4
        with open("nearthb.json", "w") as jsonFile:
            json.dump(data, jsonFile) 

    return



def take_order_sell_coin_ethusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,2))
            print("ass" ,ass)

        
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 

            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['SHORT'] + data['WAVES']['short']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['SHORT'] + data['DOT']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['SHORT'] + data['ICP']['short']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['SHORT'] + data['ATOM']['short']
                f.close() 
            if (float(ass) < 0.01 and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)


    return
def take_order_buy_coin_ethusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

 
    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),2))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 


            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['LONG'] + data['WAVES']['long']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['LONG'] + data['DOT']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['LONG'] + data['DOGE']['long']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['LONG'] + data['ICP']['long']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['LONG'] + data['ATOM']['long']
                f.close() 
            if (float(a) < 0.01 and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)

    return


def take_order_sell_coin_btcusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,3))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 

            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['SHORT'] + data['WAVES']['short']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['SHORT'] + data['DOT']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['SHORT'] + data['ICP']['short']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['SHORT'] + data['ATOM']['short']
                f.close() 
            if (float(ass) < 0.001 and res_val == 11 ):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)


    return
def take_order_buy_coin_btcusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

 
    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),3))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close()           


            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['LONG'] + data['WAVES']['long']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['LONG'] + data['DOT']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['LONG'] + data['DOGE']['long']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['LONG'] + data['ICP']['long']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['LONG'] + data['ATOM']['long']
                f.close() 
            if (float(a) < 0.001 and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)

    return


def take_order_sell_coin_bnbusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,2))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close()        

            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['SHORT'] + data['WAVES']['short']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['SHORT'] + data['DOT']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['SHORT'] + data['ICP']['short']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['SHORT'] + data['ATOM']['short']
                f.close() 

            if (float(ass) < 0.1 and res_val == 11 ):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)


    return
def take_order_buy_coin_bnbusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

 
    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),2))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 


            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['LONG'] + data['WAVES']['long']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['LONG'] + data['DOT']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['LONG'] + data['DOGE']['long']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['LONG'] + data['ICP']['long']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['LONG'] + data['ATOM']['long']
                f.close() 
            if (float(a) < 0.1 and res_val == 3):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)

    return



def take_order_sell_coin_linkusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 

            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['SHORT'] + data['WAVES']['short']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['SHORT'] + data['DOT']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['SHORT'] + data['ICP']['short']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['SHORT'] + data['ATOM']['short']
                f.close() 

            if (float(ass) <  1 and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)

    return
def take_order_buy_coin_linkusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

 
    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close()          


            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['LONG'] + data['WAVES']['long']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['LONG'] + data['DOT']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['LONG'] + data['DOGE']['long']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['LONG'] + data['ICP']['long']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['LONG'] + data['ATOM']['long']
                f.close() 
            if (float(a) < 1 and res_val == 3):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)

    return


def take_order_sell_coin_adausdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 

            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['SHORT'] + data['WAVES']['short']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['SHORT'] + data['DOT']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['SHORT'] + data['ICP']['short']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['SHORT'] + data['ATOM']['short']
                f.close() 


            if (float(ass) <  20 and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)


    return
def take_order_buy_coin_adausdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

 
    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})


            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 


            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['LONG'] + data['WAVES']['long']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['LONG'] + data['DOT']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['LONG'] + data['DOGE']['long']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['LONG'] + data['ICP']['long']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['LONG'] + data['ATOM']['long']
                f.close() 
            if (float(a) < 20 and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)

    return



def take_order_sell_coin_xrpusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
           # time.sleep(5)

            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 


            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['SHORT'] + data['WAVES']['short']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['SHORT'] + data['DOT']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['SHORT'] + data['ICP']['short']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['SHORT'] + data['ATOM']['short']
                f.close() 
            elif (markett == "XLMUSDT"):
                f = open ('xlm.json', "r")

                data = json.loads(f.read())
                res_val = data['XLM']['SHORT'] + data['XLM']['short']
                f.close() 
            if (float(ass) <  20 and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)


    return
def take_order_buy_coin_xrpusdt(self,markett,coin):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

 
    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close()
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 


            elif (markett == "WAVESUSDT"):
                f = open ('waves.json', "r")

                data = json.loads(f.read())
                res_val = data['WAVES']['LONG'] + data['WAVES']['long']
                f.close() 

            elif (markett == "DOTUSDT"):
                f = open ('dot.json', "r")

                data = json.loads(f.read())
                res_val = data['DOT']['LONG'] + data['DOT']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "DOGEUSDT"):
                f = open ('doge.json', "r")

                data = json.loads(f.read())
                res_val = data['DOGE']['LONG'] + data['DOGE']['long']
                f.close() 
            elif (markett == "ICPUSDT"):
                f = open ('icp.json', "r")

                data = json.loads(f.read())
                res_val = data['ICP']['LONG'] + data['ICP']['long']
                f.close() 
            elif (markett == "ATOMUSDT"):
                f = open ('atom.json', "r")

                data = json.loads(f.read())
                res_val = data['ATOM']['LONG'] + data['ATOM']['long']
                f.close() 
            elif (markett == "XLMUSDT"):
                f = open ('xlm.json', "r")

                data = json.loads(f.read())
                res_val = data['XLM']['LONG'] + data['XLM']['long']
                f.close() 

            if (float(a) < 20 and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)

    return


def close_order_sell_coin_usdt(self,markett):
   
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') < 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,3))
            print("ass" ,ass)



            if (float(ass) >  0):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=ass)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return


    return
def close_order_buy_coin_usdt(self,markett):

    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
 
    result = request_client.get_position()

    time.sleep(1)
    object_list = []
    #i = 0
    for res in result:
        d = collections.defaultdict()
        #d['index'] = i
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        d['positionSide'] = res.positionSide
        #d['unRealizedProfit'] = res.unRealizedProfit
    # i = i+1
        object_list.append(d)

    for key in object_list:
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') > 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),3))
            print("a" ,a)


            if (float(a) > 0):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=a)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return

    return


def take_order_buy_bnbusdt(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    f = open ('bnbusdt.json', "r")

    data = json.loads(f.read())
    res_val = data['BNBUSDT']['LONG'] + data['BNBUSDT']['long']
    f.close() 
    if (res_val== 3):
        order = client.create_order(symbol='BNBUSDT',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.05)
        PrintBasic.print_obj(order)
    return

def take_order_sell_bnbusdt(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='BNBUSDT',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.05)
    PrintBasic.print_obj(order)

def take_order_buy_adabnb(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    f = open ('adabnb.json', "r")

    data = json.loads(f.read())
    res_val = data['ADABNB']['LONG'] + data['ADABNB']['long']
    f.close() 
    if (res_val== 3):
        order = client.create_order(symbol='ADABNB',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=10)
        PrintBasic.print_obj(order)
    return

def take_order_sell_adabnb(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='ADABNB',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=10)
    PrintBasic.print_obj(order)
def take_order_buy_xrpbnb(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    f = open ('xrpbnb.json', "r")

    data = json.loads(f.read())
    res_val = data['XRPBNB']['LONG'] + data['XRPBNB']['long']
    f.close() 
    if (res_val== 3):
        order = client.create_order(symbol='XRPBNB',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=20)
        PrintBasic.print_obj(order)
    return

def take_order_sell_xrpbnb(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='XRPBNB',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=20)
    PrintBasic.print_obj(order)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    self = None
    if request.method == 'POST':
        s1 = request.data
        rt = s1.decode("utf-8")

        if (rt.find('LONGADA') != -1):
            print ("Contains BUY  substring ")

            markett = "ADAUSDT"
            update_long1(1,markett)
#
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_adausdt(self,markett,20)
            #update_short1(0,markett)

        elif (rt.find('longada') != -1):
            print ("Contains BUY  substring ")

            markett = "ADAUSDT"
            update_long2(2,markett)
            update_short2(0,markett)

            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_adausdt(self,markett,20)


        elif (rt.find('SHORTADA') != -1):
            print ("Contains SELL substring ")

            markett = "ADAUSDT"
            update_short1(4,markett)
            update_long1(0,markett)

            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_adausdt(self,markett,20)


        elif (rt.find('shortada') != -1):
            print ("Contains SELL substring ")

            markett = "ADAUSDT"
            update_long2(0,markett)
            update_short2(7,markett)
            #close_order_sell_coin_usdt(self,markett)
            #update_long2(0,markett)

            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_adausdt(self,markett,20)


        elif (rt.find('LONGXRP') != -1):
            print ("Contains BUY  substring ")

            markett = "XRPUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_xrpusdt(self,markett,20)
            #update_short1(0,markett)

        elif (rt.find('longxrp') != -1):
            print ("Contains BUY  substring ")

            markett = "XRPUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_xrpusdt(self,markett,20)


        elif (rt.find('SHORTXRP') != -1):
            print ("Contains SELL substring ")

            markett = "XRPUSDT"

            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_xrpusdt(self,markett,20)


        elif (rt.find('shortxrp') != -1):
            print ("Contains SELL substring ")

            markett = "XRPUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            #close_order_sell_coin_usdt(self,markett)
            #update_long2(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_xrpusdt(self,markett,20)


            
            
            
            
        elif (rt.find('LONGXMR') != -1):
            print ("Contains BUY  substring ")

            markett = "XMRUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.1)
            #update_short1(0,markett)

        elif (rt.find('longxmr') != -1):
            print ("Contains BUY  substring ")

            markett = "XMRUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('SHORTXMR') != -1):
            print ("Contains SELL substring ")

            markett = "XMRUSDT"

            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('shortxmr') != -1):
            print ("Contains SELL substring ")

            markett = "XMRUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            #close_order_sell_coin_usdt(self,markett)
            #update_long2(0,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.1)



        elif (rt.find('LONGBCH') != -1):
            print ("Contains BUY  substring ")

            markett = "BCHUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.1)
            #update_short1(0,markett)

        elif (rt.find('longbch') != -1):
            print ("Contains BUY  substring ")

            markett = "BCHUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('SHORTBCH') != -1):
            print ("Contains SELL substring ")

            markett = "BCHUSDT"

            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('shortbch') != -1):
            print ("Contains SELL substring ")

            markett = "BCHUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            #close_order_sell_coin_usdt(self,markett)
            #update_long2(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)
            #update_bch_short2(0)
            update_long2(0,markett)
                        
            
        elif (rt.find('LONGETH') != -1):
            print ("Contains BUY  substring ")

            markett = "ETHUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_ethusdt(self,markett,0.01)
            #update_short1(0,markett)

        elif (rt.find('longeth') != -1):
            print ("Contains BUY  substring ")

            markett = "ETHUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_ethusdt(self,markett,0.01)


        elif (rt.find('SHORTETH') != -1):
            print ("Contains SELL substring ")

            markett = "ETHUSDT"

            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_ethusdt(self,markett,0.01)


        elif (rt.find('shorteth') != -1):
            print ("Contains SELL substring ")

            markett = "ETHUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            #close_order_sell_coin_usdt(self,markett)
            #update_long2(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_ethusdt(self,markett,0.01)

                           
            
        elif (rt.find('LONGAAVE') != -1):
            print ("Contains BUY  substring ")

            markett = "AAVEUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.1)
            #update_short1(0,markett)

        elif (rt.find('longaave') != -1):
            print ("Contains BUY  substring ")

            markett = "AAVEUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('SHORTAAVE') != -1):
            print ("Contains SELL substring ")

            markett = "AAVEUSDT"

            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('shortaave') != -1):
            print ("Contains SELL substring ")

            markett = "AAVEUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.1)

                           


        elif (rt.find('LONGAXS') != -1):
            print ("Contains BUY  substring ")

            markett = "AXSUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longaxs') != -1):
            print ("Contains BUY  substring ")

            markett = "AXSUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTAXS') != -1):
            print ("Contains SELL substring ")

            markett = "AXSUSDT"

            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortaxs') != -1):
            print ("Contains SELL substring ")

            markett = "AXSUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

    

        elif (rt.find('LONGBTC') != -1):
            print ("Contains BUY  substring ")

            markett = "BTCUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_btcusdt(self,markett,0.001)
            #update_short1(0,markett)

        elif (rt.find('longbtc') != -1):
            print ("Contains BUY  substring ")

            markett = "BTCUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_btcusdt(self,markett,0.001)


        elif (rt.find('SHORTBTC') != -1):
            print ("Contains SELL substring ")

            markett = "BTCUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_btcusdt(self,markett,0.001)


        elif (rt.find('shortbtc') != -1):
            print ("Contains SELL substring ")

            markett = "BTCUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_btcusdt(self,markett,0.001)

  

        elif (rt.find('LONGBNB') != -1):
            print ("Contains BUY  substring ")

            markett = "BNBUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.1)
            #update_short1(0,markett)

        elif (rt.find('longbnb') != -1):
            print ("Contains BUY  substring ")

            markett = "BNBUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('SHORTBNB') != -1):
            print ("Contains SELL substring ")

            markett = "BNBUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('shortbnb') != -1):
            print ("Contains SELL substring ")

            markett = "BNBUSDT"

            update_short2(7,markett)
            update_long2(0,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.1)

 
            
            

        elif (rt.find('LONGETC') != -1):
            print ("Contains BUY  substring ")

            markett = "ETCUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longetc') != -1):
            print ("Contains BUY  substring ")

            markett = "ETCUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTETC') != -1):
            print ("Contains SELL substring ")

            markett = "ETCUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortetc') != -1):
            print ("Contains SELL substring ")

            markett = "ETCUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

 

        elif (rt.find('LONGLINK') != -1):
            print ("Contains BUY  substring ")

            markett = "LINKUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longlink') != -1):
            print ("Contains BUY  substring ")

            markett = "LINKUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTLINK') != -1):
            print ("Contains SELL substring ")

            markett = "LINKUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortlink') != -1):
            print ("Contains SELL substring ")

            markett = "LINKUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

 

        elif (rt.find('LONGLTC') != -1):
            print ("Contains BUY  substring ")

            markett = "LTCUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.1)
            #update_short1(0,markett)

        elif (rt.find('longltc') != -1):
            print ("Contains BUY  substring ")

            markett = "LTCUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('SHORTLTC') != -1):
            print ("Contains SELL substring ")

            markett = "LTCUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('shortltc') != -1):
            print ("Contains SELL substring ")

            markett = "LTCUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.1)

 

        elif (rt.find('LONGMKR') != -1):
            print ("Contains BUY  substring ")

            markett = "MKRUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_ethusdt(self,markett,0.01)
            #update_short1(0,markett)

        elif (rt.find('longmkr') != -1):
            print ("Contains BUY  substring ")

            markett = "MKRUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_ethusdt(self,markett,0.01)


        elif (rt.find('SHORTMKR') != -1):
            print ("Contains SELL substring ")

            markett = "MKRUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_ethusdt(self,markett,0.01)


        elif (rt.find('shortmkr') != -1):
            print ("Contains SELL substring ")

            markett = "MKRUSDT"

            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_ethusdt(self,markett,0.01)

 
            

        elif (rt.find('LONGNEO') != -1):
            print ("Contains BUY  substring ")

            markett = "NEOUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longneo') != -1):
            print ("Contains BUY  substring ")

            markett = "NEOUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTNEO') != -1):
            print ("Contains SELL substring ")

            markett = "NEOUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortneo') != -1):
            print ("Contains SELL substring ")

            markett = "NEOUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

 

        elif (rt.find('LONGQTUM') != -1):
            print ("Contains BUY  substring ")

            markett = "QTUMUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longqtum') != -1):
            print ("Contains BUY  substring ")

            markett = "QTUMUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTQTUM') != -1):
            print ("Contains SELL substring ")

            markett = "QTUMUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortqtum') != -1):
            print ("Contains SELL substring ")

            markett = "QTUMUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

 

        elif (rt.find('LONGSOL') != -1):
            print ("Contains BUY  substring ")

            markett = "SOLUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longsol') != -1):
            print ("Contains BUY  substring ")

            markett = "SOLUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTSOL') != -1):
            print ("Contains SELL substring ")

            markett = "SOLUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortsol') != -1):
            print ("Contains SELL substring ")

            markett = "SOLUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

 

        elif (rt.find('LONGUNI') != -1):
            print ("Contains BUY  substring ")

            markett = "UNiUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longuni') != -1):
            print ("Contains BUY  substring ")

            markett = "UNIUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTUNI') != -1):
            print ("Contains SELL substring ")

            markett = "UNIUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortuni') != -1):
            print ("Contains SELL substring ")

            markett = "UNIUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

            
        elif (rt.find('LONGYFIT') != -1):
            print ("Contains BUY  substring ")

            markett = "YFIUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_btcusdt(self,markett,0.001)
            #update_short1(0,markett)

        elif (rt.find('longyfit') != -1):
            print ("Contains BUY  substring ")

            markett = "YFIUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_btcusdt(self,markett,0.001)


        elif (rt.find('SHORTYFIT') != -1):
            print ("Contains SELL substring ")

            markett = "YFIUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_btcusdt(self,markett,0.001)

        elif (rt.find('shortyfit') != -1):
            print ("Contains SELL substring ")

            markett = "YFIUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_btcusdt(self,markett,0.001)



        elif (rt.find('LONGYFII') != -1):
            print ("Contains BUY  substring ")

            markett = "YFIIUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_ethusdt(self,markett,0.01)
            #update_short1(0,markett)

        elif (rt.find('longyfii') != -1):
            print ("Contains BUY  substring ")

            markett = "YFIIUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_ethusdt(self,markett,0.01)


        elif (rt.find('SHORTYFII') != -1):
            print ("Contains SELL substring ")

            markett = "YFIIUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_ethusdt(self,markett,0.01)


        elif (rt.find('shortyfii') != -1):
            print ("Contains SELL substring ")

            markett = "YFIIUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_ethusdt(self,markett,0.01)

 

        elif (rt.find('LONGZEC') != -1):
            print ("Contains BUY  substring ")

            markett = "ZECUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.1)
            #update_short1(0,markett)

        elif (rt.find('longzec') != -1):
            print ("Contains BUY  substring ")

            markett = "ZECUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('SHORTZEC') != -1):
            print ("Contains SELL substring ")

            markett = "ZECUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('shortzec') != -1):
            print ("Contains SELL substring ")

            markett = "ZECUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.1)

 

        elif (rt.find('LONGCOMP') != -1):
            print ("Contains BUY  substring ")

            markett = "COMPUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.1)
            #update_short1(0,markett)

        elif (rt.find('longcomp') != -1):
            print ("Contains BUY  substring ")

            markett = "COMPUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('SHORTCOMP') != -1):
            print ("Contains SELL substring ")

            markett = "COMPUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.1)


        elif (rt.find('shortcomp') != -1):
            print ("Contains SELL substring ")

            markett = "COMPUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.1)

 

        elif (rt.find('LONGDOT') != -1):
            print ("Contains BUY  substring ")

            markett = "DOTUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longdot') != -1):
            print ("Contains BUY  substring ")

            markett = "DOTUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTDOT') != -1):
            print ("Contains SELL substring ")

            markett = "DOTUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortdot') != -1):
            print ("Contains SELL substring ")

            markett = "DOTUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

 
                        

        elif (rt.find('LONGWAVES') != -1):
            print ("Contains BUY  substring ")

            markett = "WAVESUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longwaves') != -1):
            print ("Contains BUY  substring ")

            markett = "WAVESUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTWAVES') != -1):
            print ("Contains SELL substring ")

            markett = "WAVESUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortwaves') != -1):
            print ("Contains SELL substring ")

            markett = "WAVESUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

 
                    

        elif (rt.find('LONGXLM') != -1):
            print ("Contains BUY  substring ")

            markett = "XLMUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_xrpusdt(self,markett,30)
            #update_short1(0,markett)

        elif (rt.find('longxlm') != -1):
            print ("Contains BUY  substring ")

            markett = "XLMUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_xrpusdt(self,markett,30)


        elif (rt.find('SHORTXLM') != -1):
            print ("Contains SELL substring ")

            markett = "XLMUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_xrpusdt(self,markett,30)


        elif (rt.find('shortxlm') != -1):
            print ("Contains SELL substring ")

            markett = "XLMUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_xrpusdt(self,markett,30)

                    

        elif (rt.find('LONGDOGE') != -1):
            print ("Contains BUY  substring ")

            markett = "DOGEUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_xrpusdt(self,markett,30)
            #update_short1(0,markett)

        elif (rt.find('longdoge') != -1):
            print ("Contains BUY  substring ")

            markett = "DOGEUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_xrpusdt(self,markett,30)


        elif (rt.find('SHORTDOGE') != -1):
            print ("Contains SELL substring ")

            markett = "DOGEUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_xrpusdt(self,markett,30)


        elif (rt.find('shortdoge') != -1):
            print ("Contains SELL substring ")

            markett = "DOGEUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_xrpusdt(self,markett,30)

 



        elif (rt.find('LONGDASH') != -1):
            print ("Contains BUY  substring ")

            markett = "DASHUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.2)
            #update_short1(0,markett)

        elif (rt.find('longdash') != -1):
            print ("Contains BUY  substring ")

            markett = "DASHUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.2)


        elif (rt.find('SHORTDASH') != -1):
            print ("Contains SELL substring ")

            markett = "DASHUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.2)


        elif (rt.find('shortdash') != -1):
            print ("Contains SELL substring ")

            markett = "DASHUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.2)

                  
        


        elif (rt.find('LONGICP') != -1):
            print ("Contains BUY  substring ")

            markett = "ICPUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_bnbusdt(self,markett,0.5)
            #update_short1(0,markett)

        elif (rt.find('longicp') != -1):
            print ("Contains BUY  substring ")

            markett = "ICPUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_bnbusdt(self,markett,0.5)


        elif (rt.find('SHORTICP') != -1):
            print ("Contains SELL substring ")

            markett = "ICPUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_bnbusdt(self,markett,0.5)


        elif (rt.find('shorticp') != -1):
            print ("Contains SELL substring ")

            markett = "ICPUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_bnbusdt(self,markett,0.5)

                  


        elif (rt.find('LONGATOM') != -1):
            print ("Contains BUY  substring ")

            markett = "ATOMUSDT"
            update_long1(1,markett)
            update_short1(0,markett)
            close_order_sell_coin_usdt(self,markett)
            take_order_buy_coin_linkusdt(self,markett,1)
            #update_short1(0,markett)

        elif (rt.find('longatom') != -1):
            print ("Contains BUY  substring ")

            markett = "ATOMUSDT"
            update_long2(2,markett)
            update_short2(0,markett)
            close_order_sell_coin_usdt(self,markett)
            
            take_order_buy_coin_linkusdt(self,markett,1)


        elif (rt.find('SHORTATOM') != -1):
            print ("Contains SELL substring ")

            markett = "ATOMUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_short1(4,markett)
            update_long1(0,markett)
            close_order_buy_coin_usdt(self,markett)
            take_order_sell_coin_linkusdt(self,markett,1)


        elif (rt.find('shortatom') != -1):
            print ("Contains SELL substring ")

            markett = "ATOMUSDT"
            #close_order_buy_coin_usdt(self,markett)
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)

            take_order_sell_coin_linkusdt(self,markett,1)

                  
    
        elif (rt.find('BUYADA') != -1):
            
            print ("Contains BUY  substring ")
            markett = "ADAUSD_PERP"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            take_order_coin_perp.close_order_sell_coin_perp(self,markett)
            take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)


        elif (rt.find('buyada') != -1):
            
            print ("Contains BUY  substring ")
            markett = "ADAUSD_PERP"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_coin_perp.close_order_sell_coin_perp(self,markett)
            take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)


        elif (rt.find('SELLADA') != -1):
            print ("Contains SELL substring ")


            markett = "ADAUSD_PERP"
            update_short1(4,markett)
            update_long1(0,markett)

            take_order_coin_perp.close_order_buy_coin_perp(self,markett)
            take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)

        elif (rt.find('sellada') != -1):
            print ("Contains SELL substring ")


            markett = "ADAUSD_PERP"
            update_long2(0,markett)
            update_short2(7,markett)

            take_order_coin_perp.close_order_buy_coin_perp(self,markett)
            take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
                
        elif (rt.find('BUYBNB') != -1):
            
            print ("Contains BUY  substring ")
            markett = "BNBUSD_PERP"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            take_order_coin_perp.close_order_sell_coin_perp(self,markett)
            take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)


        elif (rt.find('buybnb') != -1):
            
            print ("Contains BUY  substring ")
            markett = "BNBUSD_PERP"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_coin_perp.close_order_sell_coin_perp(self,markett)
            take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)


        elif (rt.find('SELLBNB') != -1):
            print ("Contains SELL substring ")


            markett = "BNBUSD_PERP"
            update_short1(4,markett)
            update_long1(0,markett)

            take_order_coin_perp.close_order_buy_coin_perp(self,markett)
            take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)

        elif (rt.find('sellbnb') != -1):
            print ("Contains SELL substring ")


            markett = "BNBUSD_PERP"
            update_long2(0,markett)
            update_short2(7,markett)

            take_order_coin_perp.close_order_buy_coin_perp(self,markett)
            take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
                
        elif (rt.find('BUYDOGE') != -1):
            
            print ("Contains BUY  substring ")
            markett = "DOGEUSD_PERP"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            take_order_coin_perp.close_order_sell_coin_perp(self,markett)
            take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,1)


        elif (rt.find('buydoge') != -1):
            
            print ("Contains BUY  substring ")
            markett = "DOGEUSD_PERP"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_coin_perp.close_order_sell_coin_perp(self,markett)
            take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,1)


        elif (rt.find('SELLDOGE') != -1):
            print ("Contains SELL substring ")


            markett = "DOGEUSD_PERP"
            update_short1(4,markett)
            update_long1(0,markett)

            take_order_coin_perp.close_order_buy_coin_perp(self,markett)
            take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,1)

        elif (rt.find('selldoge') != -1):
            print ("Contains SELL substring ")


            markett = "DOGEUSD_PERP"
            update_long2(0,markett)
            update_short2(7,markett)

            take_order_coin_perp.close_order_buy_coin_perp(self,markett)
            take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,1)

        elif (rt.find('BUYTHBDOGE') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_DOGE"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbdoge') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_DOGE"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBDOGE') != -1):
            print ("Contains SELL substring ")


            markett = "THB_DOGE"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbdoge') != -1):
            print ("Contains SELL substring ")


            markett = "THB_DOGE"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
    
        elif (rt.find('BUYTHBADA') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ADA"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbada') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ADA"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBADA') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ADA"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbada') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ADA"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
    
        elif (rt.find('BUYTHBBNB') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BNB"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbbnb') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BNB"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBBNB') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BNB"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbbnb') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BNB"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBKUB') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_KUB"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbkub') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_KUB"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBKUB') != -1):
            print ("Contains SELL substring ")


            markett = "THB_KUB"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbkub') != -1):
            print ("Contains SELL substring ")


            markett = "THB_KUB"
            update_long2(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBXLM') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_XLM"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbxlm') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_XLM"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBXLM') != -1):
            print ("Contains SELL substring ")


            markett = "THB_XLM"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbxlm') != -1):
            print ("Contains SELL substring ")


            markett = "THB_XLM"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBXRP') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_XRP"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbxrp') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_XRP"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBXRP') != -1):
            print ("Contains SELL substring ")


            markett = "THB_XRP"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbxrp') != -1):
            print ("Contains SELL substring ")      

            markett = "THB_XRP"
            update_long2(0,markett)
            update_short2(7,markett)
            close_order_buy_coin_usdt(self,markett)


            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBCVC') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_CVC"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbcvc') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_CVC"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBCVC') != -1):
            print ("Contains SELL substring ")


            markett = "THB_CVC"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbcvc') != -1):
            print ("Contains SELL substring ")


            markett = "THB_CVC"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBBAT') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BAT"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbbat') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BAT"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBBAT') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BAT"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbbat') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BAT"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBIOST') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_IOST"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbiost') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_IOST"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBIOST') != -1):
            print ("Contains SELL substring ")


            markett = "THB_IOST"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbiost') != -1):
            print ("Contains SELL substring ")


            markett = "THB_IOST"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBJFIN') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_JFIN"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbjfin') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_JFIN"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBJFIN') != -1):
            print ("Contains SELL substring ")


            markett = "THB_JFIN"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbjfin') != -1):
            print ("Contains SELL substring ")


            markett = "THB_JFIN"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBPOW') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_POW"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbpow') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_POW"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBPOW') != -1):
            print ("Contains SELL substring ")


            markett = "THB_POW"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbpow') != -1):
            print ("Contains SELL substring ")


            markett = "THB_POW"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBUSDT') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_USDT"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbusdt') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_USDT"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBUSDT') != -1):
            print ("Contains SELL substring ")


            markett = "THB_USDT"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbusdt') != -1):
            print ("Contains SELL substring ")


            markett = "THB_USDT"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBUSDC') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_USDC"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbusdc') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_USDC"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBUSDC') != -1):
            print ("Contains SELL substring ")


            markett = "THB_USDC"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbusdc') != -1):
            print ("Contains SELL substring ")


            markett = "THB_USDC"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBABT') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ABT"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbabt') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ABT"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBABT') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ABT"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbabt') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ABT"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBALPHA') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ALPHA"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbalpha') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ALPHA"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBALPHA') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ALPHA"
            update_short1(4,markett)
            update_long1(0,markett)
            update_long1(0,markett)
            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbalpha') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ALPHA"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBZIL') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ZIL"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbzil') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ZIL"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBZIL') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ZIL"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbzil') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ZIL"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBSNT') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_SNT"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbsnt') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_SNT"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBSNT') != -1):
            print ("Contains SELL substring ")


            markett = "THB_SNT"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbsnt') != -1):
            print ("Contains SELL substring ")


            markett = "THB_SNT"
            update_long2(0,markett)
            update_short2(7,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('BUYTHBETH') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ETH"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbeth') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_ETH"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBETH') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ETH"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbeth') != -1):
            print ("Contains SELL substring ")


            markett = "THB_ETH"
            update_long2(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBBTC') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BTC"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbbtc') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BTC"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBBTC') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BTC"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbbtc') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BTC"
            update_long2(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBBAND') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BAND"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbband') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_BAND"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBBAND') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BAND"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbband') != -1):
            print ("Contains SELL substring ")


            markett = "THB_BAND"
            update_long2(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        elif (rt.find('BUYTHBNEAR') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_NEAR"

            update_long1(1,markett)
            update_short1(0,markett)
            #update_short1(0,markett)
            
            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('buythbnear') != -1):
            
            print ("Contains BUY  substring ")
            markett = "THB_NEAR"
            update_long2(2,markett)
            update_short2(0,markett)


            take_order_buy_coin_perp_p(self,markett)


        elif (rt.find('SELLTHBNEAR') != -1):
            print ("Contains SELL substring ")


            markett = "THB_NEAR"
            update_short1(4,markett)
            update_long1(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)

        elif (rt.find('sellthbnear') != -1):
            print ("Contains SELL substring ")


            markett = "THB_NEAR"
            update_long2(0,markett)

            
            take_order_sell_coin_perp_p(self,markett)
        else:
            print ("Doesn't contains given substring")
            #take_order_buy()
            time.sleep(1)

            
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    g_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    g_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    o_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    o_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    #request_client_mon = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    market = "BNBUSDT"
    app.run(host = '127.0.0.1',port = 80)

