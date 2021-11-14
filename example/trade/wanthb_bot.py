#!/usr/bin/env python
import ccxt
import config
import schedule
import time
import pandas as pd
import pandas_ta as ta
import logging
import tempfile
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
import cal_aroon_adx5_kdj9t as cal

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
#    markett = 'WAN' 
    unit_avl = data[markett]['available']
    
    data_hold = {
        'sym': 'THB_WAN',
        'lmt':2,
        'ts': ts,
    }
    signature_hold = sign(data_hold)
    data_hold['sig'] = signature_hold

    #print('Payload with signature: ' + json_encode(data_hold))
    response_hold = requests.post(API_HOST + '/api/market/my-order-history', headers=header, data=json_encode(data_hold))

    #print('Response: ' + response_hold.text)
    data_hold = response_hold.json()
    data_r = data_hold['result']

    #rates = data['rate']
    for d in data_r: 
        #print(d['ts'],d['side'],d['rate'])
        if (d['side']== 'buy'): 
            sale_price = d['rate']*1.05
            #print(sale_price)
            if (unit_avl > 0):
                order_data = {
                    'sym': 'THB_WAN',
                    'amt': unit_avl, # amount you want to sell
                    'rat': sale_price,
                    'typ': 'limit',
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
    unit_avl = data[markett]['available']

    if (unit_avl < 0.1):
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
            'sym': 'THB_WAN',
            'amt': 200, # THB amount you want to spend
            'rat': 0,
            'typ': 'market',
            'ts': ts,
        }
        signature = sign(buy_data)
        buy_data['sig'] = signature

        print('Payload with signature: ' + json_encode(buy_data))
        #if (res_val== 3):
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


def supertrend(df, period=7, atr_multiplier=4):
    #hl2 = (df['high'] + df['low']) / 2
    wmah = df.ta.vwma(close=df['high'])
    wmal = df.ta.vwma(close=df['low'])
    df['atr'] = atr(df, period)
    df['upperband'] = wmah + (atr_multiplier * df['atr'])
    df['lowerband'] = wmal - (atr_multiplier * df['atr'])
    df['in_uptrend'] = True
    df['in_uptrendADX'] = True
    df['in_uptrendAll'] = 0

    adx = df.ta.adx()
    df = pd.concat([df,adx],axis=1)
    for current in range(1, len(df.index)):
        previous = current - 1

        if df['close'][current] > df['upperband'][previous]:
            df['in_uptrend'][current] = True
        elif df['close'][current] < df['lowerband'][previous]:
            df['in_uptrend'][current] = False
        else:
            df['in_uptrend'][current] = df['in_uptrend'][previous]

            if df['in_uptrend'][current] and df['lowerband'][current] < df['lowerband'][previous]:
                df['lowerband'][current] = df['lowerband'][previous]

            if not df['in_uptrend'][current] and df['upperband'][current] > df['upperband'][previous]:
                df['upperband'][current] = df['upperband'][previous]
        if df['ADX_14'][current] >= 14 : 
            if df['DMP_14'][current] > df['DMN_14'][current]: 
                df['in_uptrendADX'][current]= True      
            elif df['DMP_14'][current] < df['DMN_14'][current]:
                df['in_uptrendADX'][current]= False
            else:
                df['in_uptrendADX'][current]= None
        else:
            df['in_uptrendADX'][current]= None
            
        if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
            df['in_uptrendAll'][current]=3
            #df['close_order'][current]=False
        elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
            df['in_uptrendAll'][current]=11
            #df['close_order'][current]=True
        elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
            #df['close_order'][current]=False
            df['in_uptrendAll'][current]=8
        elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
            #df['close_order'][current]=False
            df['in_uptrendAll'][current]=1        
        elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
            #df['close_order'][current]=True  
            df['in_uptrendAll'][current]=6
        elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
            #df['close_order'][current]=True
            df['in_uptrendAll'][current]=4                 
    return df


in_position = False


    
def check_buy_sell_signals(df):
    global in_position
    self=None
    print("checking for buy and sell signals")
    print(df.tail(5))
    #print(df)
    last_row_index = len(df.index) - 1
    previous_row_index = last_row_index - 1

  
    if df['in_uptrendAll'][last_row_index] == 8:
        print("changed to uptrend, buy")
        if not in_position:
        
            if (df['in_uptrendAll'][previous_row_index] != 8):# or df['in_uptrendAll'][previous_row_index] == 11 or df['in_uptrendAll'][previous_row_index] == 4 or df['in_uptrendAll'][previous_row_index] == 0 or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 1):
            #order = exchange.create_market_buy_order('WAN/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)

                order = take_order_buy_coin_perp_p('WAN')

                print(order)
                in_position = True
                message = f"BUY THB_WAN"

                payload = {
                    "username": "TBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("already in position, nothing to do")
            
    elif (df['in_uptrendAll'][last_row_index] == 22):# or df['in_uptrendAll'][last_row_index] == 6 or df['in_uptrendAll'][last_row_index] == 4):
        if in_position:
            print("changed to downtrend, sell")
            if (df['in_uptrendAll'][previous_row_index] != 22):# or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 3 or df['in_uptrendAll'][previous_row_index] == 0 or df['in_uptrendAll'][previous_row_index] == 6 or df['in_uptrendAll'][previous_row_index] == 4):

                order = take_order_sell_coin_perp_p('WAN')

                print(order)
                in_position = False
                message = f"SELL THB_WAN"

                payload = {
                    "username": "TBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("You aren't in position, nothing to sell")
    # if (not df['in_uptrendAll'][previous_row_index] and df['in_uptrendAll'][last_row_index]) and  df['in_uptrendAll'][last_row_index] != 0 :
    #     print("changed to uptrend, buy")
    #     if not in_position:
    #         #order = exchange.create_market_buy_order('WAN/USD', 0.05)
    #         #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         markett = "WANUSDT"
    #         take_order_coin_perp.close_order_sell_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = True
    #         message = f"LONG WANUSDT"

    #         payload = {
    #             "username": "TBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("already in position, nothing to do")
    
    # if (df['in_uptrendAll'][previous_row_index] and not df['in_uptrendAll'][last_row_index]) and  df['in_uptrendAll'][last_row_index] != 0 :
    #     if in_position:
    #         print("changed to downtrend, sell")
    #         markett = "WANUSDT"
    #         take_order_coin_perp.close_order_buy_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = False
    #         message = f"SHORT WANUSDT"

    #         payload = {
    #             "username": "TBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("You aren't in position, nothing to sell")

def run_bot():
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv('WAN/USDT', timeframe='3m', limit=100)
    print("THB_WAN")
    #bars = sub_client.subscribe_candlestick_event("bnbusdt", CandlestickInterval.MIN30, callback, error)
    df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')


    supertrend_data = cal.calculate_signal.supertrend(df)
    
    check_buy_sell_signals(supertrend_data)
    temp = tempfile.TemporaryFile()
    tempdir = tempfile.gettempdir()
    print(f"tempdir: {tempdir}")
    print(f"temp : {temp}")
    print(f"temp name : {temp.name}")
    temp.close()
    time.sleep(1)
    print("in position",in_position)
    time.sleep(1)

schedule.every(10).seconds.do(run_bot)


WEBHOOK_URL = "https://discord.com/api/webhooks/897716599119818812/isrG3N97QYHplgp3VxEmSQLyg82i_3j1KuqcApSKfTMORh-kEgqiidCfy6hwcj0jzIOs"


while True:
    schedule.run_pending()
    time.sleep(1)