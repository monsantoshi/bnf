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


from make_order_coin_bnb import take_order_coin_perp
#from make_order_coin_bitkub import take_order_bitkub


from datetime import datetime



from decimal import *

import collections


import array as arr



import logging



pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np


exchange = ccxt.binancecoinm({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})

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
        if df['ADX_9'][current] >= 14: 
            if df['DMP_9'][current] > df['DMN_9'][current]: 
                df['in_uptrendADX'][current]=True        
            if df['DMP_9'][current] < df['DMN_9'][current]:
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

def adxStrategy(df):
    df['in_uptrend'] = True
    adx = df.ta.adx(length=9)
    df = pd.concat([df,adx],axis=1)
    for current in range(1, len(df.index)):
        if df['ADX_9'][current] >= 30: 
            if df['DMP_9'][current] > df['DMN_9'][current]: 
                df['in_uptrend'][current]=True        
            if df['DMP_9'][current] < df['DMN_9'][current]:
                df['in_uptrend'][current]=False
    #print(df)
    return df

in_position = True

def check_buy_sell_signals(df):
    global in_position
    self=None
    print("checking for buy and sell signals")
    print(df.tail(5))
    #print(df)
    last_row_index = len(df.index) - 1
    previous_row_index = last_row_index - 1


    if not df['in_uptrend'][previous_row_index] and df['in_uptrend'][last_row_index]:
        print("changed to uptrend, buy")
        #if not in_position:
            #order = exchange.create_market_buy_order('ETH/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
        markett = "ADAUSD_PERP"
        take_order_coin_perp.close_order_sell_coin_perp(self,markett)

        order = take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)
        print(order)
        in_position = True
        message = f"LONG ADAUSD"

        payload = {
            "username": "SignalBot",
            "content": message
        }

        requests.post(WEBHOOK_URL, json=payload)
        # else:
        #     print("already in position, nothing to do")
    
    if df['in_uptrend'][previous_row_index] and not df['in_uptrend'][last_row_index]:
        #if in_position:
        print("changed to downtrend, sell")
        markett = "ADAUSD_PERP"
        take_order_coin_perp.close_order_buy_coin_perp(self,markett)

        order = take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
        print(order)
        in_position = False
        message = f"SHORT ADAUSD"

        payload = {
            "username": "SignalBot",
            "content": message
        }

        requests.post(WEBHOOK_URL, json=payload)
        # else:
        #     print("You aren't in position, nothing to sell")

def run_bot():
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv("ADAUSD_PERP", timeframe='5m', limit=50)
    #bars = sub_client.subscribe_candlestick_event("bnbusdt", CandlestickInterval.MIN30, callback, error)
    df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')


    supertrend_data = adxStrategy(df)

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
     


schedule.every(5).seconds.do(run_bot)
WEBHOOK_URL = "https://discord.com/api/webhooks/897722855448530974/xm9DeP4PM4vlcUpv95b5aiZ7iqIapi1uSryTbxh1vOR5IVHhl6YPQFFCI51ulycBlIDC"


while True:
    schedule.run_pending()
    time.sleep(1)