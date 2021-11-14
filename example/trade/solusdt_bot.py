#!/usr/bin/env python
import config
import schedule
import time
import pandas as pd
import pandas_ta as ta
import logging
import requests
import tempfile
from binance_f import RequestClient

from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *



from datetime import datetime
from binance.client import Client


from decimal import *
import email
import imaplib
import collections
import os

import array as arr
import threading

import math
import json


import logging
import cal_aroon_adx5_kdj9 as cal



pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np
in_position = False
strategy = 0
count_lost = 0
count_win = 0

def close_order_sell_coin_usdt(self,markett):
   
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

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



            if (float(ass) >  0) and (float(mPrices) < float(priceIns)):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=ass)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return


    return
def close_order_buy_coin_usdt(self,markett):

    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)
 
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


            if (float(a) > 0)  and (float(mPrice) > float(priceIn)):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=a)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return

    return

def take_order_sell_coin_adausdt(self,markett,coin):
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)


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
            plostsf =  str(round(float(priceIns) +((3.00*float(priceIns))/20),3))

            if ((float(ass) <  0.1)):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
            if ((float(ass) >=  1) and float(ass) < 2 and float(mPrices) > float(plostsf) ):
                
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)

    return
def take_order_buy_coin_adausdt(self,markett,coin):
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

 
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
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})
            plostf =  str(round(float(priceIn) +((-3.00*float(priceIn))/20),3))

            if ((float(a) < 0.1) ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
            if ((float(a) >= 1 )  and float(a) < 2 and float(mPrice) < float(plostf)):
            
    
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
    return

    
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
            #order = exchange.create_market_buy_order('ETH/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
                markett = "SOLUSDT"
                close_order_sell_coin_usdt(self,markett)

                order = take_order_buy_coin_adausdt(self,markett,1)
                print(order)
                in_position = True
                message = f"LONG SOLUSDT"

                payload = {
                    "username": "SignalBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("already in position, nothing to do")
        
    if df['in_uptrendAll'][last_row_index] == 22:
        if in_position:
            print("changed to downtrend, sell")
            if (df['in_uptrendAll'][previous_row_index] != 22):# or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 3 or df['in_uptrendAll'][previous_row_index] == 0 or df['in_uptrendAll'][previous_row_index] == 6 or df['in_uptrendAll'][previous_row_index] == 4):

                markett = "SOLUSDT"
                close_order_buy_coin_usdt(self,markett)

                order = take_order_sell_coin_adausdt(self,markett,1)
                print(order)
                in_position = False
                message = f"SHORT SOLUSDT"

                payload = {
                    "username": "SignalBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("You aren't in position, nothing to sell")



def run_bot():

    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

    bars = request_client.get_candlestick_data(symbol="SOLUSDT", interval=CandlestickInterval.MIN3,startTime=None, endTime=None, limit=100)

    object_list_open = []
    for reso in bars:
        c = collections.defaultdict()
        c['timestamp'] = float(reso.openTime)
        c['open'] = float(reso.open)
        c['high'] = float(reso.high)
        c['low'] = float(reso.low)
        c['close'] = float(reso.close)
        c['volume'] = float(reso.volume)
        object_list_open.append(c)
    df = pd.DataFrame(object_list_open[:-1])
    df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')    
    print(f"Fetching new bars for {datetime.now().isoformat()}")
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