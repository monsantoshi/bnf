#!/usr/bin/env python3
from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *
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

def update_dark(d,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"dark":d} })
def update_obv(o,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"obv":o} })
def update_sweat(s,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"sweat":s} })

def update_guide(g,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"guide":g} })
def update_darkd(d,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"darkd":d} })
def update_obvd(o,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"obvd":o} })
def update_sweatd(s,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"sweatd":s} })
class CountCandle:
    Down = False
    Up = False
    def __init__(self,market):
        self.market = market
    def take_order_point(self):

        global dark_ada
        global obv_ada
        global sweat_ada
        global guide_bnb
        

        global dark_bnb
        global obv_bnb
        global sweat_bnb
        global guide_bnb
        global dark_adad
        global obv_adad
        global sweat_adad

        global dark_bnbd
        global obv_bnbd
        global sweat_bnbd
        positionAmtShort = 0
        positionAmtLong = 0


        client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")
        db = client.Binance
        collection_cound = db["count"]

        ada_c_data = collection_cound.find_one({"market": 'ADAUSD_PERP'})

        bnb_c_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})

        #bnbu_c_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})

        dark_ada = ada_c_data["dark"]
        obv_ada = ada_c_data["obv"]
        sweat_ada= ada_c_data["sweat"]
        guide_ada = ada_c_data["guide"]

        dark_bnb = bnb_c_data["dark"]
        obv_bnb = bnb_c_data["obv"]
        sweat_bnb = bnb_c_data["sweat"]
        guide_bnb = bnb_c_data["guide"]

        dark_adad = ada_c_data["darkd"]
        obv_adad = ada_c_data["obvd"]
        sweat_adad= ada_c_data["sweatd"]

        dark_bnbd = bnb_c_data["darkd"]
        obv_bnbd = bnb_c_data["obvd"]
        sweat_bnbd = bnb_c_data["sweatd"]
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
            if (key.get('positionSide') =='SHORT' and (key.get('symbol') == "BNBUSD_PERP")):
                positionAmtShort = key.get('positionAmt')*-1
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BNBUSD_PERP")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),0))
                p = str(round(float(priceIn) +((0.025* float(priceIn))/20),3))
                pl = str(round(float(priceIn) -((0.35* float(priceIn))/20),3))
                pll = str(round(float(priceIn) -((0.50* float(priceIn))/20),3))
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==2 and obv_bnb ==2 and sweat_bnb ==2 and guide_bnb == 2) and (float(positionAmtShort) >= 0) and (float(positionAmtShort) < 30)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0

                        time.sleep(1)
                    elif ((dark_bnb ==2 and obv_bnb ==2 and sweat_bnb ==2 and guide_bnb == 2) and (float(positionAmtShort) >= 30) ):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc*15)
                        time.sleep(2)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) >= float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) >= 1 and (dark_bnb+obv_bnb+sweat_bnb) < 6 ):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0
                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) ==6 and guide_bnb == 2 and (float(a) < float(step_two_unitbc))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitbc)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0
                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitbc)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==2 and obv_bnb ==2 and sweat_bnb ==2 and guide_bnb==2)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc*2)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0
                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unitbc)) and (float(positionAmtLong) < float(step_three_unitbc)) and  (float(mPrice) <= float(pll))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==2 and obv_bnb ==2 and sweat_bnb ==2 and guide_bnb==2)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc*3)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0
                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='LONG' and (keys.get('symbol') == "BNBUSD_PERP")):

                positionAmtLong = keys.get('positionAmt')
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BNBUSD_PERP")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),0))
                ps = str(round(float(priceIns) -((0.025* float(priceIns))/20),3))
                pss = str(round(float(priceIns) +((0.35* float(priceIns))/20),3))
                psss = str(round(float(priceIns) +((0.50* float(priceIns))/20),3))
                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1 and guide_bnb==1) and (float(positionAmtLong) >= 0) and (float(positionAmtLong) < 30)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0

                        time.sleep(1)
                    elif ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1 and guide_bnb ==1) and (float(positionAmtLong) >= 30)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc*15)
                        time.sleep(2)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) <= float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) >= 3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0

                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) == 3 and guide_bnb == 1 and (float(ass) < float(step_two_unitbc))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitbc)
                        PrintBasic.print_obj(take_order_short)
                       # update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitbc) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1 and guide_bnb==1)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc*2)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unitbc) and float(positionAmtShort) < float(step_three_unitbc) and (float(mPrices) >= float(psss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1 and guide_bnb==1)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc*3)
                        PrintBasic.print_obj(take_order_short)
                       # update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        guide_bnb = 0

                        time.sleep(1)

                        
        # for key in object_list:
        #     if (key.get('positionSide') =='SHORT' and (key.get('symbol') == "ADAUSD_PERP")):
        #         positionAmtShort = key.get('positionAmt')*-1
        #     if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ADAUSD_PERP")):
        #         positionAmtLong = key.get('positionAmt')
        #         priceIn = key.get('entryPrice')
        #         mPrice = key.get('markPrice')
        #         a = str(round(float(positionAmtLong),0))
        #         p = str(round(float(priceIn) +((0.04* float(priceIn))/20),5))
        #         pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),5))
        #         pll = str(round(float(priceIn) -((0.30* float(priceIn))/20),5))
        #         if (float(positionAmtLong) == 0):
        
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_ada ==2 and obv_ada ==2 and sweat_ada ==2) and (float(positionAmtShort) >= 0) and (float(positionAmtShort) < 30)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

        #                 time.sleep(1)
        #             elif ((dark_ada ==2 and obv_ada ==2 and sweat_ada ==2) and (float(positionAmtShort) >= 30) ):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc*15)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and  (float(mPrice) >= float(p))):
            
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_ada+obv_ada+sweat_ada) >3 and (dark_ada+obv_ada+sweat_ada) <6):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0
        #                 time.sleep(1)
        #             elif ((dark_ada+obv_ada+sweat_ada) ==6 and (float(a) < float(step_two_unitbc))):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitbc)) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_ada ==2 and obv_ada ==2 and sweat_ada ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) >= float(step_two_unitbc)) and (float(positionAmtLong) < float(step_three_unitbc)) and  (float(mPrice) <= float(pll))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_ada ==2 and obv_ada ==2 and sweat_ada ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0
        #                 time.sleep(1)
        # for keys in object_list:
        #     if (keys.get('positionSide') =='LONG' and (keys.get('symbol') == "ADAUSD_PERP")):

        #         positionAmtLong = keys.get('positionAmt')
        #     if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ADAUSD_PERP")):

        #         positionAmtShort = keys.get('positionAmt')*-1
        #         mPrices = keys.get('markPrice')
        #         priceIns = keys.get('entryPrice')
        #         ass = str(round(float(positionAmtShort),0))
        #         ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
        #         pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))
        #         psss = str(round(float(priceIns) +((0.30* float(priceIns))/20),5))
        #         if (float(positionAmtShort) == 0):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_ada ==1 and obv_ada ==1 and sweat_ada ==1) and (float(positionAmtLong) >= 0) and (float(positionAmtLong) < 30)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

        #                 time.sleep(1)
        #             elif ((dark_ada ==1 and obv_ada ==1 and sweat_ada ==1) and (float(positionAmtLong) >= 30)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc*15)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

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
        #             if ((dark_ada+obv_ada+sweat_ada) > 3):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

        #                 time.sleep(1)
        #             elif ((dark_ada+obv_ada+sweat_ada) == 3 and (float(ass) < float(step_two_unitbc)) and (float(mPrices) >= float(pss))):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitbc) and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_ada ==1 and obv_ada ==1 and sweat_ada ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) >= float(step_two_unitbc) and float(positionAmtShort) < float(step_three_unitbc) and (float(mPrices) >= float(psss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_ada ==1 and obv_ada ==1 and sweat_ada ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obv(0,'ADAUSD_PERP')
        #                 update_dark(0,'ADAUSD_PERP')
        #                 update_sweat(0,'ADAUSD_PERP')
        #                 dark_ada = 0
        #                 obv_ada = 0
        #                 sweat_ada = 0

        #                 time.sleep(1)




                        
        # for key in object_list:
        #     if (key.get('positionSide') =='SHORT' and (key.get('symbol') == "BNBUSD_PERP")):
        #         positionAmtShort = key.get('positionAmt')*-1
        #     if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BNBUSD_PERP")):
        #         positionAmtLong = key.get('positionAmt')
        #         priceIn = key.get('entryPrice')
        #         mPrice = key.get('markPrice')
        #         a = str(round(float(positionAmtLong),0))
        #         p = str(round(float(priceIn) +((0.04* float(priceIn))/20),3))
        #         pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),3))
        #         pll = str(round(float(priceIn) -((0.30* float(priceIn))/20),3))
        #         if (float(positionAmtLong) == 0):
        
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnbd ==2 and obv_bnbd ==2 and sweat_bnbd ==2) and (float(positionAmtShort) >= 0) and (float(positionAmtShort) < 30)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)
        #             elif ((dark_bnbd ==2 and obv_bnbd ==2 and sweat_bnbd ==2) and (float(positionAmtShort) >= 30)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc*15)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and  (float(mPrice) >= float(p))):
            
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_bnbd+obv_bnbd+sweat_bnbd) > 0 and (dark_bnbd+obv_bnbd+sweat_bnbd) < 6 ):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0
        #                 time.sleep(1)
        #             elif ((dark_bnbd+obv_bnbd+sweat_bnbd) ==6 and (float(a) < float(step_two_unitbc))):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd= 2
        #                 obv_bnbd = 2
        #                 sweat_bnbd = 2
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitbc)) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnbd ==2 and obv_bnbd ==2 and sweat_bnbd ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) >= float(step_two_unitbc)) and (float(positionAmtLong) < float(step_three_unitbc)) and  (float(mPrice) <= float(pll))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnbd ==2 and obv_bnbd ==2 and sweat_bnbd ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0
        #                 time.sleep(1)
        # for keys in object_list:
        #     if (keys.get('positionSide') =='LONG' and (keys.get('symbol') == "BNBUSD_PERP")):

        #         positionAmtLong = keys.get('positionAmt')
        #     if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BNBUSD_PERP")):

        #         positionAmtShort = keys.get('positionAmt')*-1
        #         mPrices = keys.get('markPrice')
        #         priceIns = keys.get('entryPrice')
        #         ass = str(round(float(positionAmtShort),0))
        #         ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),3))
        #         pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),3))
        #         psss = str(round(float(priceIns) +((0.30* float(priceIns))/20),3))
        #         if (float(positionAmtShort) == 0):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnbd ==1 and obv_bnbd ==1 and sweat_bnbd ==1) and (float(positionAmtLong) >= 0) and (float(positionAmtLong) < 30)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)
        #             elif ((dark_bnbd ==1 and obv_bnbd ==1 and sweat_bnbd ==1) and (float(positionAmtLong) >= 30)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc*15)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and  (float(mPrices) <= float(ps))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_bnbd+obv_bnbd+sweat_bnbd) > 3):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)
        #             elif ((dark_bnbd+obv_bnbd+sweat_bnbd) == 3 and (float(ass) < float(step_two_unitbc))):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitbc) and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnbd ==1 and obv_bnbd ==1 and sweat_bnbd ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) >= float(step_two_unitbc) and float(positionAmtShort) < float(step_three_unitbc) and (float(mPrices) >= float(psss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnbd ==1 and obv_bnbd ==1 and sweat_bnbd ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'BNBUSD_PERP')
        #                 update_darkd(0,'BNBUSD_PERP')
        #                 update_sweatd(0,'BNBUSD_PERP')
        #                 dark_bnbd = 0
        #                 obv_bnbd = 0
        #                 sweat_bnbd = 0

        #                 time.sleep(1)

                        
        # for key in object_list:
        #     if (key.get('positionSide') =='SHORT' and (key.get('symbol') == "ADAUSD_PERP")):
        #         positionAmtShort = key.get('positionAmt')*-1
        #     if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ADAUSD_PERP")):
        #         positionAmtLong = key.get('positionAmt')
        #         priceIn = key.get('entryPrice')
        #         mPrice = key.get('markPrice')
        #         a = str(round(float(positionAmtLong),0))
        #         p = str(round(float(priceIn) +((0.04* float(priceIn))/20),5))
        #         pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),5))
        #         pll = str(round(float(priceIn) -((0.30* float(priceIn))/20),5))
        #         if (float(positionAmtLong) == 0):
        
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_adad ==2 and obv_adad ==2 and sweat_adad ==2) and (float(positionAmtShort) >= 0) and (float(positionAmtShort) < 30)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

        #                 time.sleep(1)
        #             elif ((dark_adad ==2 and obv_adad ==2 and sweat_adad ==2) and (float(positionAmtShort) >= 30) ):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc*15)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and  (float(mPrice) >= float(p))):
            
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_adad+obv_adad+sweat_adad) >3 and (dark_adad+obv_adad+sweat_adad) <6):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0
        #                 time.sleep(1)
        #             elif ((dark_adad+obv_adad+sweat_adad) ==6 and (float(a) < float(step_two_unitbc))):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitbc)) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_adad ==2 and obv_adad ==2 and sweat_adad ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) >= float(step_two_unitbc)) and (float(positionAmtLong) < float(step_three_unitbc)) and  (float(mPrice) <= float(pll))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_adad ==2 and obv_adad ==2 and sweat_adad ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0
        #                 time.sleep(1)
        # for keys in object_list:
        #     if (keys.get('positionSide') =='LONG' and (keys.get('symbol') == "ADAUSD_PERP")):

        #         positionAmtLong = keys.get('positionAmt')
        #     if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ADAUSD_PERP")):

        #         positionAmtShort = keys.get('positionAmt')*-1
        #         mPrices = keys.get('markPrice')
        #         priceIns = keys.get('entryPrice')
        #         ass = str(round(float(positionAmtShort),0))
        #         ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
        #         pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))
        #         psss = str(round(float(priceIns) +((0.30* float(priceIns))/20),5))
        #         if (float(positionAmtShort) == 0):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_adad ==1 and obv_adad ==1 and sweat_adad ==1) and (float(positionAmtLong) >= 0) and (float(positionAmtLong) < 30)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

        #                 time.sleep(1)
        #             elif ((dark_adad ==1 and obv_adad ==1 and sweat_adad ==1) and (float(positionAmtLong) >= 30)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc*15)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

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
        #             if ((dark_adad+obv_adad+sweat_adad) > 3):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

        #                 time.sleep(1)
        #             elif ((dark_adad+obv_adad+sweat_adad) == 3 and (float(ass) < float(step_two_unitbc)) and (float(mPrices) >= float(pss))):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitbc) and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_adad ==1 and obv_adad ==1 and sweat_adad ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad= 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) >= float(step_two_unitbc) and float(positionAmtShort) < float(step_three_unitbc) and (float(mPrices) >= float(psss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_adad ==1 and obv_adad ==1 and sweat_adad ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="ADAUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 update_obvd(0,'ADAUSD_PERP')
        #                 update_darkd(0,'ADAUSD_PERP')
        #                 update_sweatd(0,'ADAUSD_PERP')
        #                 dark_adad = 0
        #                 obv_adad = 0
        #                 sweat_adad = 0

        #                 time.sleep(1)
        
        return


if __name__ == '__main__':

    g_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    g_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    o_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    o_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
 
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_cutloss = db["cut_loss"]
    collection_cound = db["count"]

    ada_c_data = collection_cound.find_one({"market": 'ADAUSD_PERP'})

    bnb_con_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})

    

    bnbc_data  = collection_cutloss.find_one({"market": 'BNBUSD_PERP'})
  
    
    market ='BNBUSDT'

    dark_ada = ada_c_data["dark"]
    obv_ada = ada_c_data["obv"]
    sweat_ada = ada_c_data["sweat"]

    dark_bnb = bnb_con_data["dark"]
    obv_bnb = bnb_con_data["obv"]
    sweat_bnb = bnb_con_data["sweat"]
    
    dark_adad = ada_c_data["darkd"]
    obv_adad = ada_c_data["obvd"]
    sweat_adad = ada_c_data["sweatd"]

    dark_bnbd = bnb_con_data["darkd"]
    obv_bnbd = bnb_con_data["obvd"]
    sweat_bnbd = bnb_con_data["sweatd"]
    guide_bnb = bnb_con_data["guide"]
    guide_ada = ada_c_data["guide"]



    buy_unitbc = bnbc_data["buy"]
    sale_unitbc = bnbc_data["sale"]
    step_one_unitbc = bnbc_data["step_one_unit"]
    step_two_unitbc = bnbc_data["step_two_unit"]
    step_three_unitbc = bnbc_data["step_three_unit"]
    step_four_unitbc = bnbc_data["step_four_unit"]


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

