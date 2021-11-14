#!/usr/bin/env python
import ccxt
import config
import schedule
import time
import pandas as pd
import pandas_ta as ta
import logging
import requests
import tempfile

from datetime import datetime
from binance.client import Client


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

#from example.trade.bakeusdt_bot import make_profit_long


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
#    markett = 'BNB' 
#    markett = 'BNB' 
    unit_avl = data[markett]['available']
    
    data_hold = {
        'sym': 'THB_BNB',
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
                    'sym': 'THB_BNB',
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
            'sym': 'THB_BNB',
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


def take_order_buy_ethusdt():
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='ETHUSDT',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.004)
    PrintBasic.print_obj(order)

def take_order_sell_ethusdt():
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='ETHUSDT',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.004)
    PrintBasic.print_obj(order)
    

def take_order_buy_bnbusdt():
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    #order = client.create_order(symbol='BNBUSDT',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.02)
    order = client.get_my_trades('BNBUSDT')
    PrintBasic.print_obj(order)

def take_order_sell_bnbusdt():
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    
    order = client.create_order(symbol='BNBUSDT',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.02)
    PrintBasic.print_obj(order)   

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
    df['upperband'] = ta.vwma(hl2 + (atr_multiplier * df['atr']),df['volume'],length=3)
    df['lowerband'] = ta.vwma(hl2 - (atr_multiplier * df['atr']),df['volume'],length=3)
    #df['meantrend'] = (df['upperband']+df['lowerband'])/2
    #df['meantrendHMA'] = (df['upperbandHMA']+df['lowerbandHMA'])/2
    df['in_uptrend'] = True
    df['in_uptrendADX'] = True
    #df['in_uptrendHMA'] = True
    supertest = df.ta.supertrend(length=7,multiplier=3.5)
    adx = df.ta.adx()
    df = pd.concat([df,supertest['SUPERTd_7_3.5'],adx],axis=1)

    for current in range(1, len(df.index)):
        if df['ADX_14'][current] >= 30: 
            if df['DMP_14'][current] > df['DMN_14'][current]: 
                df['in_uptrendADX'][current]=True        
            if df['DMP_14'][current] < df['DMN_14'][current]:
                df['in_uptrendADX'][current]=False
        if df['SUPERTd_7_3.5'][current] == 1: 
            df['in_uptrend'][current]=True
        else: 
            df['in_uptrend'][current]=False
        if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
            df['in_uptrend'][current]=True
        else: 
            df['in_uptrend'][current]=False   
        # previous = current - 1

        # if (df['close'][current] > (df['upperband'][previous]+df['meantrend'][previous])/2):
        #     df['in_uptrend'][current] = True
        # elif (df['close'][current] < (df['meantrend'][previous]+df['lowerband'][previous])/2):
        #     df['in_uptrend'][current] = False
        # else:
        #     df['in_uptrend'][current] = df['in_uptrend'][previous]

        #     if df['in_uptrend'][current] and (df['lowerband'][current] < df['lowerband'][previous]):
        #         df['lowerband'][current] = df['lowerband'][previous]

        #     if not df['in_uptrend'][current] and (df['upperband'][current] > df['upperband'][previous]):
        #         df['upperband'][current] = df['upperband'][previous]

        # if (df['close'][current] > (df['upperbandHMA'][previous]+df['meantrendHMA'][previous])/2):
        #     df['in_uptrendHMA'][current] = True
        # elif (df['close'][current] < (df['meantrendHMA'][previous]+df['lowerbandHMA'][previous])/2):
        #     df['in_uptrendHMA'][current] = False
        # else:
        #     df['in_uptrendHMA'][current] = df['in_uptrendHMA'][previous]

        #     if df['in_uptrendHMA'][current] and (df['lowerbandHMA'][current] < df['lowerbandHMA'][previous]):
        #         df['lowerbandHMA'][current] = df['lowerbandHMA'][previous]

        #     if not df['in_uptrendHMA'][current] and (df['upperbandHMA'][current] > df['upperbandHMA'][previous]):
        #         df['upperbandHMA'][current] = df['upperbandHMA'][previous]      
        
        
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
            #order = exchange.create_market_buy_order('BNB/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
            #close_order_sell_coin_usdt(self,'ADAUSDT')
            order = take_order_buy_bnbusdt()
            print(order)
            message = f"SELL BNB/USDT"

            payload = {
                "username": "SignalBot",
                "content": message
            }

            requests.post(WEBHOOK_URL, json=payload)
            in_position = True
        else:
            print("already in position, nothing to do")
    
    if df['in_uptrend'][previous_row_index] and not df['in_uptrend'][last_row_index]:
        if in_position:
            print("changed to downtrend, sell")
            #close_order_buy_coin_usdt(self,'ADAUSDT')
            order = take_order_sell_bnbusdt()
            print(order)
            message = f"BUY BNB/USDT"

            payload = {
                "username": "SignalBot",
                "content": message
            }

            requests.post(WEBHOOK_URL, json=payload)
            in_position = False
        else:
            print("You aren't in position, nothing to sell")

def run_bot():
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv('BNB/USDT', timeframe='5m', limit=50)
    print("SPOT BNB/USDT")
    #bars = sub_client.subscribe_candlestick_event("bnbusdt", CandlestickInterval.MIN30, callback, error)
    df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')


    supertrend_data = supertrend(df)
    
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
WEBHOOK_URL = "https://discord.com/api/webhooks/897722855448530974/xm9DeP4PM4vlcUpv95b5aiZ7iqIapi1uSryTbxh1vOR5IVHhl6YPQFFCI51ulycBlIDC"

api_key = config.BINANCE_API_KEY 
api_secret = config.BINANCE_SECRET_KEY
client = Client(api_key, api_secret)
self = None
#order = client.create_order(symbol='BNBUSDT',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.02)
my_trades = client.get_asset_balance(asset='BNB')
print(my_trades['free'])
unit_avl = my_trades['free']
my_trades = client.get_my_trades(symbol='BNBUSDT',limit=2)

for trade in my_trades:
    if trade['isBuyer']==True:
        print(trade['price'])
        sell_price = round(float(trade['price'])*1.05,2)
        print(sell_price)
# while True:
#     schedule.run_pending()
#     time.sleep(1)