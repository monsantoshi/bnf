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
from binance_f import RequestClient

from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
#from make_order_coin_bnb import take_order_coin_perp
#from make_order_coin_bitkub import take_order_bitkub


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

# from binance_f import SubscriptionClient
# from binance_f.constant.test import *
# from binance_f.model import *
# from binance_f.exception.binanceapiexception import BinanceApiException

#from binance_f.base.printobject import *
pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np
# #from datetime import datetime
# #import time


# logger = logging.getLogger("binance-futures")
# logger.setLevel(level=logging.INFO)
# handler = logging.StreamHandler()
# handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# logger.addHandler(handler)

# sub_client = SubscriptionClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)


# def callback(data_type: 'SubscribeMessageType', event: 'any'):
#     if data_type == SubscribeMessageType.RESPONSE:
#         print("Event ID: ", event)
#     elif  data_type == SubscribeMessageType.PAYLOAD:
#         print("Event type: ", event.eventType)
#         print("Event time: ", event.eventTime)
#         print("Symbol: ", event.symbol)
#         print("Data:")
#         PrintBasic.print_obj(event.data)
#         sub_client.unsubscribe_all()
#     else:
#         print("Unknown Data:")
#     print()


# def error(e: 'BinanceApiException'):
#     print(e.error_code + e.error_message)

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



            if (float(ass) >  0 and float(mPrices) < float(priceIns)):

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


            if (float(a) > 0 and float(mPrice) > float(priceIn)):

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
            if ((float(ass) >=  0.1)  and float(ass) <0.2 and float(mPrices) > float(plostsf) ):
                
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
            plostf =  str(round(float(priceIn) +((-3.00*float(priceIn))/20),2))

            if ((float(a) < 0.1) ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
            if ((float(a) >= 0.1 )  and float(a) < 0.2 and float(mPrice) < float(plostf)):
        
    
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
    return

exchange = ccxt.binanceusdm({
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

def supertrend(df, period=7, atr_multiplier=4):
    hl2 = (df['high'] + df['low']) / 2
    calVwma = ta.vwma(hl2,df['volume'])
    wmah = df.ta.vwma(close=df['high'])
    wmal = df.ta.vwma(close=df['low'])
    df['atr'] = atr(df, period)
    df['upperband'] = calVwma + (atr_multiplier * df['atr'])
    df['lowerband'] = calVwma - (atr_multiplier * df['atr'])
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

    # if (df['in_uptrendAll'][last_row_index] != 8) :
    #     if (df['in_uptrendAll'][previous_row_index] == 8):        #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         #order = exchange.create_market_buy_order('ETH/USD', 0.05)
    #     #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         close_order_buy_coin_usdt(self,'BNBUSDT')  
    #         in_position = False
    #         message = f"CLOSE POSITION LONG BNBUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("already close position, nothing to do")
    # if (df['in_uptrendAll'][last_row_index] != 22) :   
    #     if (df['in_uptrendAll'][previous_row_index] ==22):
    #          #order = exchange.create_market_buy_order('ETH/USD', 0.05)
    #     #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         close_order_sell_coin_usdt(self,'BNBUSDT')  
    #         in_position = False
    #         message = f"CLOSE POSITION SHORT BNBUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("already close position, nothing to do")

  
    if df['in_uptrendAll'][last_row_index] == 8:
        print("changed to uptrend, buy")
        if not in_position:
            
            if (df['in_uptrendAll'][previous_row_index]  != 8):
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
                markett = "BNBUSDT"
                close_order_sell_coin_usdt(self,markett)

                order = take_order_buy_coin_adausdt(self,markett,0.1)
                print(order)
                in_position = True
                message = f"LONG BNBUSDT"

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
            if (df['in_uptrendAll'][previous_row_index] != 22):

                markett = "BNBUSDT"
                close_order_buy_coin_usdt(self,markett)

                order = take_order_sell_coin_adausdt(self,markett,0.1)
                print(order)
                in_position = False
                message = f"SHORT BNBUSDT"

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
    #         markett = "BNBUSDT"
    #         take_order_coin_perp.close_order_sell_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = True
    #         message = f"LONG BNBUSDT"

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
    #         markett = "BNBUSDT"
    #         take_order_coin_perp.close_order_buy_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = False
    #         message = f"SHORT BNBUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("You aren't in position, nothing to sell")

def run_bot():
    # print(f"Fetching new bars for {datetime.now().isoformat()}")
    # bars = exchange.fetch_ohlcv('BNBUSDT', timeframe='5m', limit=140)
    # #bars = sub_client.subscribe_candlestick_event("bnbusdt", CandlestickInterval.MIN30, callback, error)
    # df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    # df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')

    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

    bars = request_client.get_candlestick_data(symbol="BNBUSDT", interval=CandlestickInterval.MIN3,startTime=None, endTime=None, limit=100)

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