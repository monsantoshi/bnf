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

class take_order_bitkub:
    
    def __init__(self,markett):
        self.markett = markett
    
    
    def take_order_sell_coin_perp_p(self,markett):
        


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

        # data = response.json()
        # data = data['result']
        # if markett == "THB_BNB":
        #     markett = 'BNB'
        # elif markett == "THB_ADA":
        #     markett = 'ADA'
        # elif markett == "THB_DOGE":
        #     markett = 'DOGE'        
        # elif markett == "THB_KUB":
        #     markett = 'KUB'   
        # elif markett == "THB_XLM":
        #     markett = 'XLM'  
        # elif markett == "THB_ZIL":
        #     markett = 'ZIL'  
        # elif markett == "THB_IOST":
        #     markett = 'IOST'  
        # elif markett == "THB_JFIN":
        #     markett = 'JFIN' 
        # elif markett == "THB_CVC":
        #     markett = 'CVC'   
        # elif markett == "THB_XRP":
        #     markett = 'XRP' 
        # elif markett == "THB_USDT":
        #     markett = 'USDT' 
        # elif markett == "THB_USDC":
        #     markett = 'USDC' 
        # elif markett == "THB_BAT":
        #     markett = 'BAT' 
        # elif markett == "THB_POW":
        #     markett = 'POW' 
        # elif markett == "THB_ABT":
        #     markett = 'ABT' 
        # elif markett == "THB_ALPHA":
        #     markett = 'ALPHA' 
        # elif markett == "THB_SNT":
        #     markett = 'SNT' 
        # elif markett == "THB_ETH":
        #     markett = 'ETH' 
        # elif markett == "THB_BTC":
        #     markett = 'BTC' 
        # elif markett == "THB_BAND":
        #     markett = 'BAND' 
        # elif markett == "THB_NEAR":
        #     markett = 'NEAR' 
        # unit_avl = data[markett]['available']

        # if (markett == "ADA" and unit_avl < 1):
        #     f = open ('adathb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['ADA']['LONG'] + data['ADA']['long']
        #     f.close() 

        #     # check server time
        #     response = requests.get(API_HOST + '/api/servertime')
        #     ts = int(response.text)
        #     print('Server time: ' + response.text)

        #     # check balances
        #     header = {
        #         'Accept': 'application/json',
        #         'Content-Type': 'application/json',
        #         'X-BTK-APIKEY': API_KEY,
        #     }
        #     buy_data = {
        #         'sym': 'THB_ADA',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "BNB" and unit_avl < 0.01):
        #     f = open ('bnbthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['BNB']['LONG'] + data['BNB']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_BNB',
        #         'amt': 2000, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "DOGE" and unit_avl < 20):
        #     f = open ('dogethb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['DOGE']['LONG'] + data['DOGE']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_DOGE',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)

        # elif (markett == "KUB" and unit_avl < 1):
        #     f = open ('kubthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['KUB']['LONG'] + data['KUB']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_KUB',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "XLM" and unit_avl < 1):
        #     f = open ('xlmthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['XLM']['LONG'] + data['XLM']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_XLM',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "XRP" and unit_avl < 1):
        #     f = open ('xrpthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['XRP']['LONG'] + data['XRP']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_XRP',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "BAT" and unit_avl < 1):
        #     f = open ('batthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['BAT']['LONG'] + data['BAT']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_BAT',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "CVC" and unit_avl < 1):
        #     f = open ('cvcthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['CVC']['LONG'] + data['CVC']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_CVC',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "IOST" and unit_avl < 1):
        #     f = open ('iostthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['IOST']['LONG'] + data['IOST']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_IOST',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "JFIN" and unit_avl < 1):
        #     f = open ('jfinthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['JFIN']['LONG'] + data['JFIN']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_JFIN',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "POW" and unit_avl < 1):
        #     f = open ('powthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['POW']['LONG'] + data['POW']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_POW',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "USDT" and unit_avl < 1):
        #     f = open ('usdtthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['USDT']['LONG'] + data['USDT']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_USDT',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "USDC" and unit_avl < 1):
        #     f = open ('usdcthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['USDC']['LONG'] + data['USDC']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_USDC',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "ABT" and unit_avl < 1):
        #     f = open ('abtthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['ABT']['LONG'] + data['ABT']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_ABT',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "ALPHA" and unit_avl < 1):
        #     f = open ('alphathb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['ALPHA']['LONG'] + data['ALPHA']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_ALPHA',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "ZIL" and unit_avl < 1):
        #     f = open ('zilthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['ZIL']['LONG'] + data['ZIL']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_ZIL',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "SNT" and unit_avl < 1):
        #     f = open ('sntthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['SNT']['LONG'] + data['SNT']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_SNT',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "ETH" and unit_avl < 0.001):
        #     f = open ('eththb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['ETH']['LONG'] + data['ETH']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_ETH',
        #         'amt': 1000, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "BTC" and unit_avl < 0.0001):
        #     f = open ('btcthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['BTC']['LONG'] + data['BTC']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_BTC',
        #         'amt': 2000, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "BAND" and unit_avl < 0.5):
        #     f = open ('bandthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['BAND']['LONG'] + data['BAND']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_BAND',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)
        # elif (markett == "NEAR" and unit_avl < 0.5):
        #     f = open ('nearthb.json', "r")

        #     data = json.loads(f.read())
        #     res_val = data['NEAR']['LONG'] + data['NEAR']['long']
        #     f.close() 
        #     buy_data = {
        #         'sym': 'THB_NEAR',
        #         'amt': 200, # THB amount you want to spend
        #         'rat': 0,
        #         'typ': 'market',
        #         'ts': ts,
        #     }
        #     signature = sign(buy_data)
        #     buy_data['sig'] = signature

        #     print('Payload with signature: ' + json_encode(buy_data))
        #     if (res_val== 3):
        #         response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(buy_data))

        #         print('Response: ' + response.text)

        return