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
import collections
import math
import decimal
import array as arr
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
import cal_supertrend73_adx14spot as cal
#from example.trade.bakeusdt_bot import make_profit_long


pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np


exchange = ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})
   

def take_order_buy_xrpusdt():
       
    api_key = config.BINANCE_API_KEY 
    api_secret = config.BINANCE_SECRET_KEY
    client = Client(api_key, api_secret)
    my_balance = client.get_asset_balance(asset='XRP')
    unit_avl = float(my_balance['free'])   
    if (unit_avl < 5): 
        order = client.create_order(symbol='XRPUSDT',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=10)
    return
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def take_order_sell_xrpusdt():

    api_key = config.BINANCE_API_KEY 
    api_secret = config.BINANCE_SECRET_KEY
    client = Client(api_key, api_secret)
    my_balance = client.get_asset_balance(asset='XRP')
    unit_avl = truncate(float(my_balance['free']),2)
    #unit_tp = '%.3f'%(round(float(my_balance['free']),5))
    print("unit_avl",unit_avl)
    my_trades = client.get_my_trades(symbol='XRPUSDT',limit=2)

    for trade in my_trades:
        if trade['isBuyer']==True:
            print(trade['price'])
            pl = []
            sell_price = str(round(float(trade['price'])*1.05,4))
            first_price = 0
            pl.append(first_price)
            print(sell_price)

            if (float(sell_price) > pl[-1]):

                pl.append(sell_price)
            
                print("add_last_price" , sell_price)
                    #time.sleep(1)
                print("pl in if",pl)
    pricef = str(round(float(pl[-1]),4))
    print("last_TP_price",pricef)

    if (float(unit_avl) > 0):
        #print("unit_avl", unit_avl)
        order = client.create_order(symbol='XRPUSDT',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_LIMIT,price=pricef,quantity=unit_avl,timeInForce=Client.TIME_IN_FORCE_GTC)
      
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

  
    if df['in_uptrendAll'][last_row_index] == 3:
        print("changed to uptrend, buy")
        if not in_position:
        
            if (df['in_uptrendAll'][previous_row_index] == 6 or df['in_uptrendAll'][previous_row_index] == 11 or df['in_uptrendAll'][previous_row_index] == 4 or df['in_uptrendAll'][previous_row_index] == 0 or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 1):
            #order = exchange.create_market_buy_order('ETH/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)

                order = take_order_buy_xrpusdt()

                print(order)
                in_position = True
                message = f"BUY XRP/USDT"

                payload = {
                    "username": "SignalBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("already in position, nothing to do")
            
    elif (df['in_uptrendAll'][last_row_index] == 11 or df['in_uptrendAll'][last_row_index] == 6 or df['in_uptrendAll'][last_row_index] == 4):
        if in_position:
            print("changed to downtrend, sell")
            if (df['in_uptrendAll'][previous_row_index] == 1 or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 3 or df['in_uptrendAll'][previous_row_index] == 0 or df['in_uptrendAll'][previous_row_index] == 6 or df['in_uptrendAll'][previous_row_index] == 4):

                order = take_order_sell_xrpusdt()

                print(order)
                in_position = False
                message = f"SELL XRP/USDT"

                payload = {
                    "username": "SignalBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("You aren't in position, nothing to sell")
    # if (not df['in_uptrendAll'][previous_row_index] and df['in_uptrendAll'][last_row_index]) and  df['in_uptrendAll'][last_row_index] != 0 :
    #     print("changed to uptrend, buy")
    #     if not in_position:
    #         #order = exchange.create_market_buy_order('ETH/USD', 0.05)
    #         #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         markett = "XRPUSDT"
    #         take_order_coin_perp.close_order_sell_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = True
    #         message = f"LONG XRPUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("already in position, nothing to do")
    
    # if (df['in_uptrendAll'][previous_row_index] and not df['in_uptrendAll'][last_row_index]) and  df['in_uptrendAll'][last_row_index] != 0 :
    #     if in_position:
    #         print("changed to downtrend, sell")
    #         markett = "XRPUSDT"
    #         take_order_coin_perp.close_order_buy_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = False
    #         message = f"SHORT XRPUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("You aren't in position, nothing to sell")

# def check_buy_sell_signals(df):
#     global in_position
#     self=None
#     print("checking for buy and sell signals")
#     print(df.tail(5))
#     last_row_index = len(df.index) - 1
#     previous_row_index = last_row_index - 1

#     if (not df['in_uptrend'][previous_row_index] and df['in_uptrend'][last_row_index]) and df['in_uptrend'][last_row_index]!=None:
#         print("changed to uptrend, buy")
#         if not in_position:
#             #order = exchange.create_market_buy_order('XRP/USD', 0.05)
#             #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
#             #close_order_sell_coin_usdt(self,'ADAUSDT')
#             order = take_order_buy_xrpusdt()
#             #print(order)
#             message = f"BUY XRP/USDT"

#             payload = {
#                 "username": "SignalBot",
#                 "content": message
#             }

#             requests.post(WEBHOOK_URL, json=payload)
#             in_position = True
#         else:
#             print("already in position, nothing to do")
    
#     if (df['in_uptrend'][previous_row_index] and not df['in_uptrend'][last_row_index]) and df['in_uptrend'][last_row_index]!=None:
#         if in_position:
#             print("changed to downtrend, sell")
#             #close_order_buy_coin_usdt(self,'ADAUSDT')
#             order = take_order_sell_xrpusdt()
#             #print(order)
#             message = f"SELL XRP/USDT"

#             payload = {
#                 "username": "SignalBot",
#                 "content": message
#             }

#             requests.post(WEBHOOK_URL, json=payload)
#             in_position = False
#         else:
#             print("You aren't in position, nothing to sell")

def run_bot():
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv('XRP/USDT', timeframe='5m', limit=140)
    print("SPOT XRP/USDT")
    #bars = sub_client.subscribe_candlestick_event("xrpusdt", CandlestickInterval.MIN30, callback, error)
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
WEBHOOK_URL = "https://discord.com/api/webhooks/897722855448530974/xm9DeP4PM4vlcUpv95b5aiZ7iqIapi1uSryTbxh1vOR5IVHhl6YPQFFCI51ulycBlIDC"


while True:
    schedule.run_pending()
    time.sleep(1)