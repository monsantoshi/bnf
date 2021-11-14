#!/usr/bin/env python3
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
from pymongo import MongoClient
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


detach_dir = 'c:\db'

class Bin33(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting: 33 " + self.name + "\n") 
        b33 = CountCandle(market)
        b33.take_order_point()
        #b33.take_order_point_mon()
        print("Exiting: 33 " + self.name + "\n")
class Bin333(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting: 333 " + self.name + "\n") 
        b33 = CountCandle(market)
        #b33.take_order_point()
        b33.take_order_point_new()
        print("Exiting: 333 " + self.name + "\n")

class CountCandle:
    Down = False
    Up = False
    def __init__(self,market):
        self.market = market
    def take_order_point(self):
        global dark_ltc
        global obv_ltc
        global sweat_ltc
        global dark_yfi
        global obv_yfi
        global sweat_yfi
        global dark_btc
        global obv_btc
        global sweat_btc
        global dark_bch
        global obv_bch
        global sweat_bch
        global dark_bnb
        global obv_bnb
        global sweat_bnb
        global dark_eth
        global obv_eth
        global sweat_eth

        client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")
        db = client.Binance
        collection_cound = db["count"]
        btc_c_data = collection_cound.find_one({"market": 'BTCUSDT'})
        yfi_c_data = collection_cound.find_one({"market": 'YFIUSDT'})
        ltc_c_data = collection_cound.find_one({"market": 'LTCUSDT'})
        bch_c_data = collection_cound.find_one({"market": 'BCHUSDT'})
        bnb_c_data = collection_cound.find_one({"market": 'BNBUSDT'})
        eth_c_data = collection_cound.find_one({"market": 'ETHUSDT'})
        #bnbu_c_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})
        dark_ltc = ltc_c_data["dark"]
        obv_ltc = ltc_c_data["obv"]
        sweat_ltc = ltc_c_data["sweat"]
        dark_yfi = yfi_c_data["dark"]
        obv_yfi = yfi_c_data["obv"]
        sweat_yfi = yfi_c_data["sweat"]
        dark_bch = bch_c_data["dark"]
        obv_bch = bch_c_data["obv"]
        sweat_bch = bch_c_data["sweat"]
        dark_btc = btc_c_data["dark"]
        obv_btc = btc_c_data["obv"]
        sweat_btc = btc_c_data["sweat"]
        dark_bnb = bnb_c_data["dark"]
        obv_bnb = bnb_c_data["obv"]
        sweat_bnb = bnb_c_data["sweat"]
        dark_eth = eth_c_data["dark"]
        obv_eth = eth_c_data["obv"]
        sweat_eth = eth_c_data["sweat"]

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

        result = request_client.get_position()

        time.sleep(1)
        object_list = []

        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            d['positionSide'] = res.positionSide
            object_list.append(d)


        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "LTCUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.045* float(priceIn))/20),5))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),5))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
        
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_ltc ==1 and obv_ltc ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="LTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if  (((dark_ltc+obv_ltc+sweat_ltc) < 3)):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="LTCUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2
                        time.sleep(1)
                    elif ((dark_ltc+obv_ltc+sweat_ltc) ==3 and (float(a) < float(step_two_unitb))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="LTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitb)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_ltc ==1 and obv_ltc ==1 and sweat_ltc ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="LTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unitb)) and (float(positionAmtLong) < float(step_three_unitb)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_ltc ==1 and obv_ltc ==1 and sweat_ltc ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="LTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2
                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "LTCUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))



                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_ltc ==0 and obv_ltc ==0 and sweat_ltc ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="LTCUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_btc+obv_btc+sweat_btc) > 0):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="LTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2

                        time.sleep(1)
                    elif ((dark_ltc+obv_ltc+sweat_ltc) == 0 and (float(ass) < float(step_two_unitb))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="LTCUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitb) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_ltc ==0 and obv_ltc ==0 and sweat_ltc ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="LTCUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unitb) and float(positionAmtShort) < float(step_three_unitb) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_ltc ==0 and obv_ltc ==0 and sweat_ltc ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="LTCUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_ltc = 2
                        # obv_ltc = 2
                        # sweat_ltc = 2

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BTCUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.045* float(priceIn))/20),4))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),4))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
            
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_btc = db["count"]
                    # btc_data = collection_btc.find_one({"market": 'BTCUSDT'})   
                    # dark = btc_data["dark"]
                    # obv = btc_data["obv"]
                    # sweat = btc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_btc ==1 and obv_btc ==1 and sweat_btc ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_btc+obv_btc+sweat_btc) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                    elif ((dark_btc+obv_btc+sweat_btc) ==3 and (float(a) < float(step_two_unitc))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitc)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_btc ==1 and obv_btc ==1 and sweat_btc ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unitc)) and (float(positionAmtLong) < float(step_three_unitc)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_btc ==1 and obv_btc ==1 and sweat_btc ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BTCUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                ass = str(round(float(positionAmtShort),3))
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),4))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),4))

                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_btc = db["count"]

                    # btc_data = collection_btc.find_one({"market": 'BTCUSDT'})   
                    # dark = btc_data["dark"]
                    # obv = btc_data["obv"]
                    # sweat = btc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_btc ==0 and obv_btc ==0 and sweat_btc ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BTCUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ( (dark_btc+obv_btc+sweat_btc) > 0):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                    elif ( (dark_btc+obv_btc+sweat_btc) ==0 and (float(ass) < float(step_two_unitc))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitc) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_btc ==0 and obv_btc ==0 and sweat_btc ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BTCUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
                elif ( float(positionAmtShort) >= float(step_two_unitc) and float(positionAmtShort) < float(step_three_unitc) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_btc ==0 and obv_btc ==0 and sweat_btc ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BTCUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_btc = 2
                        # obv_btc = 2
                        # sweat_btc = 2

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BCHUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),2))
                p = str(round(float(priceIn) +((0.045* float(priceIn))/20),5))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),5))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
            
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_btc = db["count"]
                    # btc_data = collection_btc.find_one({"market": 'BCHUSDT'})   
                    # dark = btc_data["dark"]
                    # obv = btc_data["obv"]
                    # sweat = btc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bch ==1 and obv_bch ==1 and sweat_bch ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BCHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BCHUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bch+ obv_bch+sweat_bch) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BCHUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)                    
                    elif ((dark_bch+ obv_bch+sweat_bch) ==3 and (float(a) < float(step_two_unite))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BCHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BCHUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bch ==1 and obv_bch ==1 and sweat_bch ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BCHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unite)) and (float(positionAmtLong) < float(step_three_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BCHUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bch ==1 and obv_bch ==1 and sweat_bch ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BCHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BCHUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                #ass = str(round(float(positionAmtShort),2))
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),2))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))

                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_btc = db["count"]

                    # btc_data = collection_btc.find_one({"market": 'BCHUSDT'})   
                    # dark = btc_data["dark"]
                    # obv = btc_data["obv"]
                    # sweat = btc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bch ==0 and obv_bch ==0 and sweat_bch ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BCHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BCHUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bch+ obv_bch+sweat_bch) > 0):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BCHUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
                    elif ((dark_bch+ obv_bch+sweat_bch) == 0 and (float(ass) < float(step_two_unite))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BCHUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unite)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BCHUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bch ==0 and obv_bch ==0 and sweat_bch ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BCHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unite) and float(positionAmtShort) < float(step_three_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BCHUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bch ==0 and obv_bch ==0 and sweat_bch ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BCHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_bch = 2
                        # obv_bch = 2
                        # sweat_bch = 2

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "YFIUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.045* float(priceIn))/20),5))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),5))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
        
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_yfi ==1 and obv_yfi ==1 and sweat_yfi ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="YFIUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ( (dark_yfi+ obv_yfi+sweat_yfi) <3):
                    
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="YFIUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                    elif ( (dark_yfi+ obv_yfi+sweat_yfi) ==3 and (float(a) < float(step_two_unitc))):
                        
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="YFIUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitc)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_yfi ==1 and obv_yfi ==1 and sweat_yfi ==1)):

                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="YFIUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unitc)) and (float(positionAmtLong) < float(step_three_unitc)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_yfi ==1 and obv_yfi ==1 and sweat_yfi ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="YFIUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitc)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "YFIUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))



                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_yfi ==0 and obv_yfi ==0 and sweat_yfi ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="YFIUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_yfi+ obv_yfi+sweat_yfi) > 0):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="YFIUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                    elif ((dark_yfi+ obv_yfi+sweat_yfi) == 0 and (float(ass) < float(step_two_unitc))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="YFIUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitc) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_yfi ==0 and obv_yfi ==0 and sweat_yfi ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="YFIUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unitc) and float(positionAmtShort) < float(step_three_unitc) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'YFIUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_yfi ==0 and obv_yfi ==0 and sweat_yfi ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="YFIUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitc)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'YFIUSDT')
                        # update_dark("2",'YFIUSDT')
                        # update_sweat("2",'YFIUSDT')
                        # dark_yfi = 2
                        # obv_yfi = 2
                        # sweat_yfi = 2

                        time.sleep(1)       
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ETHUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),2))
                p = str(round(float(priceIn) +((0.045* float(priceIn))/20),2))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),2))
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_btc = db["count"]
                    # btc_data = collection_btc.find_one({"market": 'BTCUSDT'})   
                    # dark = btc_data["dark"]
                    # obv = btc_data["obv"]
                    # sweat = btc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_eth+obv_eth+sweat_eth) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                    elif ((dark_eth+obv_eth+sweat_eth) ==3 and (float(a) < float(step_two_unite))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unite)) and (float(positionAmtLong) < float(step_three_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ETHUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1

                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),2))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),2))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),2))

                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_btc = db["count"]

                    # btc_data = collection_btc.find_one({"market": 'BTCUSDT'})   
                    # dark = btc_data["dark"]
                    # obv = btc_data["obv"]
                    # sweat = btc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ( (dark_eth+obv_eth+sweat_eth) > 0 ):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth= 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                    elif ( (dark_eth+obv_eth+sweat_eth) ==0 and (float(ass) < float(step_two_unite))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ( float(positionAmtShort) >= float(step_two_unite) and float(positionAmtShort) < float(step_three_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'BTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'BTCUSDT')
                        #update_dark("2",'BTCUSDT')
                        #update_sweat("2",'BTCUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                        
        # for key in object_list:
        #     if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BNBUSD_PERP")):
        #         positionAmtLong = key.get('positionAmt')
        #         priceIn = key.get('entryPrice')
        #         mPrice = key.get('markPrice')
        #         a = str(round(float(positionAmtLong),0))
        #         p = str(round(float(priceIn) +((0.055* float(priceIn))/20),2))
        #         pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),2))
        #         if (float(positionAmtLong) == 0):
        
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_bnb+obv_bnb+sweat_bnb) <3):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        #             elif ((dark_bnb+obv_bnb+sweat_bnb) ==3 and (a < step_two_unitbc)):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb= 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < step_two_unitbc) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) >= step_two_unitbc) and (float(positionAmtLong) < step_three_unitbc) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        # for keys in object_list:
        #     if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BNBUSD_PERP")):

        #         positionAmtShort = keys.get('positionAmt')*-1
        #         mPrices = keys.get('markPrice')
        #         priceIns = keys.get('entryPrice')
        #         ass = str(round(float(positionAmtShort),0))
        #         ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),2))
        #         pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),2))
        #         if (float(positionAmtShort) == 0):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_bnb+obv_bnb+sweat_bnb) > 0):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #             elif ((dark_bnb+obv_bnb+sweat_bnb) == 0 and (ass < step_two_unitbc)):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and float(positionAmtShort) < step_two_unitbc and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) >= step_two_unitbc and float(positionAmtShort) < step_three_unitbc and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'LTCUSDT')
        #                 # update_dark("2",'LTCUSDT')
        #                 # update_sweat("2",'LTCUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BNBUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),2))
                p = str(round(float(priceIn) +((0.055* float(priceIn))/20),2))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),2))
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) ==3 and (a < step_two_unitb)):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb= 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < step_two_unitb) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) >= step_two_unitb) and (float(positionAmtLong) < step_three_unitb) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitb)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BNBUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),2))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),2))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),2))
                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) > 0):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) == 0 and (ass <step_two_unitb)):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < step_two_unitb and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= step_two_unitb and float(positionAmtShort) < step_three_unitb and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitb)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'LTCUSDT')
                        # update_dark("2",'LTCUSDT')
                        # update_sweat("2",'LTCUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
         
        return


if __name__ == '__main__':

    o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    g_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    g_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
 
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_cutloss = db["cut_loss"]
    collection_cound = db["count"]
    btc_c_data = collection_cound.find_one({"market": 'BTCUSDT'})
    yfi_c_data = collection_cound.find_one({"market": 'YFIUSDT'})
    ltc_c_data = collection_cound.find_one({"market": 'LTCUSDT'})
    bch_c_data = collection_cound.find_one({"market": 'BCHUSDT'})
    bnb_c_data = collection_cound.find_one({"market": 'BNBUSDT'})
    eth_c_data = collection_cound.find_one({"market": 'ETHUSDT'})
    bnb_con_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})

    
    
    
    btc_data = collection_cutloss.find_one({"market": 'BTCUSDT'})
    eth_data = collection_cutloss.find_one({"market": 'ETHUSDT'})
    bnb_data = collection_cutloss.find_one({"market": 'BNBUSDT'})
    bnbc_data  = collection_cutloss.find_one({"market": 'BNBUSD_PERP'})
  
    
    market ='BNBUSDT'
    dark_ltc = ltc_c_data["dark"]
    obv_ltc = ltc_c_data["obv"]
    sweat_ltc = ltc_c_data["sweat"]
    dark_yfi = yfi_c_data["dark"]
    obv_yfi = yfi_c_data["obv"]
    sweat_yfi = yfi_c_data["sweat"]
    dark_bch = bch_c_data["dark"]
    obv_bch = bch_c_data["obv"]
    sweat_bch = bch_c_data["sweat"]
    dark_btc = btc_c_data["dark"]
    obv_btc = btc_c_data["obv"]
    sweat_btc = btc_c_data["sweat"]
    dark_bnb = bnb_c_data["dark"]
    obv_bnb = bnb_c_data["obv"]
    sweat_bnb = bnb_c_data["sweat"]
    dark_eth = eth_c_data["dark"]
    obv_eth = eth_c_data["obv"]
    sweat_eth = eth_c_data["sweat"]


    buy_unitbc = bnbc_data["buy"]
    sale_unitbc = bnbc_data["sale"]
    step_one_unitbc = bnbc_data["step_one_unit"]
    step_two_unitbc = bnbc_data["step_two_unit"]
    step_three_unitbc = bnbc_data["step_three_unit"]
    step_four_unitbc = bnbc_data["step_four_unit"]
    
      
    buy_unitb = bnb_data["buy"]
    sale_unitb = bnb_data["sale"]
    step_one_unitb = bnb_data["step_one_unit"]
    step_two_unitb = bnb_data["step_two_unit"]
    step_three_unitb = bnb_data["step_three_unit"]
    step_four_unitb = bnb_data["step_four_unit"]

    buy_unitc = btc_data["buy"]
    sale_unitc = btc_data["sale"]
    step_one_unitc = btc_data["step_one_unit"]
    step_two_unitc = btc_data["step_two_unit"]
    step_three_unitc = btc_data["step_three_unit"]
    step_four_unitc = btc_data["step_four_unit"]


    buy_unite = eth_data["buy"]
    sale_unite = eth_data["sale"]
    step_one_unite = eth_data["step_one_unit"]
    step_two_unite = eth_data["step_two_unit"]
    step_three_unite = eth_data["step_three_unit"]
    step_four_unite = eth_data["step_four_unit"]

    try:
        while True:
            thread1 = Bin33(1,"Count Candle")
            #thread2 = Bin333(2,"Count Candle")
            #thread3 = Bin333(3,"Count Candle")
            thread1.start()
            #thread2.start()
            #thread3.start()
            thread1.join()
            #thread2.join()
            #thread3.join()
            time.sleep(1)
    except IndexError as error:
        print("Exiting: with error" + "\n")
    except Exception as exception:
        print("Exiting: Exception error" +  "\n")

