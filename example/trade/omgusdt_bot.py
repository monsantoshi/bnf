
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
            ass = str(round(float(positionAmtShort)*-1,4))
            print("ass" ,ass)


            if ((float(ass) <  1)):
            
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
            a = str(round(float(positionAmtLong),4))
            print("a" ,a)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})


            if ((float(a) < 1) ):

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

def make_profit_long():
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)  
    result_open_order = request_client.get_open_orders()
    time.sleep(1)
    conts =  0
    object_list_open = []
    for reso in result_open_order:
        c = collections.defaultdict()
        #c['index'] = t
        c['symbol'] = reso.symbol
        c['orderId'] = reso.orderId
        c['side'] = reso.side
        c['origQty'] = reso.origQty
        c['positionSide'] = reso.positionSide
        c['status'] = reso.status
        c['type'] = reso.type
        #d['unRealizedProfit'] = res.unRealizedProfit
        #t = t+1
        object_list_open.append(c)
    time.sleep(1)
    for keys in object_list_open:
        #cont = 0
        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "OMGUSDT")  and (keys.get('type')=="LIMIT") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            conts = keys.get('origQty')
            print("market",markets)
            print("orderId",orderIds)
            print("origQty",conts)
    for keys in object_list_open:
        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "OMGUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            
            print("market",markets)
            print("orderId",orderIds)

            #time.sleep(1)
            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)
    result = request_client.get_position()

    time.sleep(1)

    object_list = []
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

        f = open ('profit.json', "r")

        data = json.loads(f.read())
        p = data['LONG']['p'] 
        pf = data['LONG']['pf'] 
        pff = data['LONG']['pff'] 
        puffs = data['LONG']['pfff'] 
        pffff = data['LONG']['pffff'] 
        plost = data['LONG']['plost'] 
        plostf = data['LONG']['plostf'] 
        plostl = data['LONG']['plostl'] 
        f.close()
        if (key.get('positionSide') =='LONG' and key.get('symbol') =='OMGUSDT' and key.get('positionAmt') > 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            a = str(round(float(positionAmtLong),0))
            try:
                p = str(round(float(priceIn) +((p* float(priceIn))/20),4))
                pf = str(round(float(priceIn) +((0.05* float(priceIn))/20),4))
                pff = str(round(float(priceIn) +((pff* float(priceIn))/20),4))
                puffs = str(round(float(priceIn) +((puffs* float(priceIn))/20),4))
                pffff = str(round(float(priceIn) +((pffff* float(priceIn))/20),4))
                ploss =  str(round(float(priceIn) +((plost*float(priceIn))/20),4))
                plostf =  str(round(float(priceIn) +((plostf*float(priceIn))/20),4))
                plostl =  str(round(float(priceIn) +((plostl*float(priceIn))/20),4))
                try:
                    cut_loss_long = request_client.post_order(symbol=sym, side=OrderSide.SELL,positionSide=PositionSide.LONG,stopPrice=plostl, ordertype=OrderType.STOP_MARKET,closePosition='True') 
                except IndexError as error:
                    print("Exiting: with error in try" + "\n")
                except Exception as exception:
                    print("Exiting: Exception error in try" +  "\n")                        
                if (mPrice >= Decimal(ploss) ):
                    try:
                        if float(conts) == 0:
                            take_profit_long = request_client.post_order(symbol=sym, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=pf, quantity=a,timeInForce='GTC')
                            #time.sleep(1)
                            conts = 0
                        if float(a) > float(conts):
                            print("conts",conts)
                            rest = float(a) - float(conts)
                            take_profit_long = request_client.post_order(symbol=sym, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=pf, quantity=str(round(rest,4)),timeInForce='GTC')
                            #time.sleep(1) 
                            conts = 0
                    except IndexError as error:
                        print("Exiting: with error in try" + "\n")
                    except Exception as exception:
                        print("Exiting: Exception error in try" +  "\n")
            except IndexError as error:
                print("Exiting: with error in try" + "\n")
            except Exception as exception:
                print("Exiting: Exception error in try" +  "\n")
    return

def make_profit_short():
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)  
    result_open_order = request_client.get_open_orders()
    time.sleep(1)
    conts = 0
    object_list_open = []
    stop_threads = False
    #t = 0
    for reso in result_open_order:
        c = collections.defaultdict()
        #c['index'] = t
        c['symbol'] = reso.symbol
        c['orderId'] = reso.orderId
        c['origQty'] = reso.origQty
        c['side'] = reso.side
        c['positionSide'] = reso.positionSide
        c['status'] = reso.status
        c['type'] = reso.type
        #d['unRealizedProfit'] = res.unRealizedProfit
        #t = t+1
        object_list_open.append(c)
        #time.sleep(1)                       



    for keys in object_list_open:
        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "OMGUSDT") and (keys.get('type')=="LIMIT") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            conts = keys.get('origQty')
            print("market",markets)
            print("orderId",orderIds)
            print("origQty",conts)
            #conts = keys.get('origQty')
            #print("origQty",conts)
            # conts = conts+conts
            #time.sleep(1)
    #         result_for_cancel_s = request_client.cancel_order(symbol=markets, orderId=orderIds)
        
    for keys in object_list_open:
        #cont = 0
        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "OMGUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            
            print("market",markets)
            print("orderId",orderIds)

            #time.sleep(1)
            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
###########################
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
        f = open ('profit.json', "r")

        data = json.loads(f.read())

        first_p = data['PROFIT']['first_profit'] 
        sec_p = data['PROFIT']['sec_profit'] 
        thr_p = data['PROFIT']['thr_profit'] 
        ps = data['SHORT']['ps'] 
        psf = data['SHORT']['psf'] 
        psff = data['SHORT']['psff'] 
        psfff = data['SHORT']['psfff'] 
        psffff = data['SHORT']['psffff'] 
        pslost = data['SHORT']['pslost'] 
        pslostf = data['SHORT']['pslostf'] 
        pslostl = data['SHORT']['pslostl'] 
        f.close()
        if (key.get('positionSide') =='SHORT' and key.get('symbol') =='OMGUSDT' and key.get('positionAmt') < 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(mPrices,'',priceIns,'',syms,'',positionAmtShort)
            #d = Decimal(str(mPrices))

            #pres = (d.as_tuple().exponent)*-1
            ass = str(round(float(positionAmtShort)*-1,0))
            time.sleep(1)
                
            try:
                psl=[]

                ps = str(round(float(priceIns) -((ps* float(priceIns))/20),4))

                psf = str(round(float(priceIns) -((0.05* float(priceIns))/20),4))
                psff = str(round(float(priceIns) -((psff* float(priceIns))/20),4))
                psfff = str(round(float(priceIns) -((psfff* float(priceIns))/20),4))
                psffff = str(round(float(priceIns) -((psffff* float(priceIns))/20),4))
                psloss = str(round(float(priceIns) +((pslost*float(priceIns))/20),4))
                pslostf = str(round(float(priceIns) +((pslostf*float(priceIns))/20),4))
                pslostl = str(round(float(priceIns) +((pslostl*float(priceIns))/20),4))
                try:
                    cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT,stopPrice=pslostl,  ordertype=OrderType.STOP_MARKET, closePosition='True')
                except IndexError as error:
                    print("Exiting: with error in try" + "\n")
                except Exception as exception:
                    print("Exiting: Exception error in try" +  "\n")      

                if (mPrices <= Decimal(psloss)  and float(ass) > 0 ):
                    try:
                        if float(conts) == 0:
                            ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=psf, quantity=ass,timeInForce='GTC')
                            #ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.TRAILING_STOP_MARKET , price=psfff, quantity=ass,timeInForce='GTC')
                            #time.sleep(1)
                            conts = 0
                        if float(ass) > float(conts):
                            print("conts",conts)
                            rest = float(ass) - float(conts)
                            ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=psf, quantity=str(round(rest,4)),timeInForce='GTC')
                            #time.sleep(1)
                            conts = 0
                    except IndexError as error:
                        print("Exiting: with error in try" + "\n")
                    except Exception as exception:
                        print("Exiting: Exception error in try" +  "\n") 
            except IndexError as error:
                print("Exiting: with error in try" + "\n")
            except Exception as exception:
                print("Exiting: Exception error in try" +  "\n")
    return


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
            close_order_sell_coin_usdt(self,'OMGUSDT')
            order = take_order_buy_coin_adausdt(self,'OMGUSDT',1)
            print(order)
            in_position = True
            message = f"LONG OMGUSDT"

            payload = {
                "username": "SignalBot",
                "content": message
            }

            requests.post(WEBHOOK_URL, json=payload)
            time.sleep(3)
            make_profit_long() 
            time.sleep(2)
        else:
            print("already in position, nothing to do")
   
    if df['in_uptrend'][previous_row_index] and not df['in_uptrend'][last_row_index]:
        if in_position:
            print("changed to downtrend, sell")
            close_order_buy_coin_usdt(self,'OMGUSDT')
            order = take_order_sell_coin_adausdt(self,'OMGUSDT',1)
            print(order)
            in_position = False
            message = f"SHORT OMGUSDT"

            payload = {
                "username": "SignalBot",
                "content": message
            }

            requests.post(WEBHOOK_URL, json=payload)
            time.sleep(3)
            make_profit_short() 
            time.sleep(2)
        else:
            print("You aren't in position, nothing to sell")

def run_bot():
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv('OMGUSDT', timeframe='5m', limit=50)
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


while True:
    schedule.run_pending()
    time.sleep(1)