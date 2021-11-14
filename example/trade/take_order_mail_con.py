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
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"dark":d} })
def update_obv(o,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"obv":o} })
def update_sweat(s,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"sweat":s} })

def update_guide(g,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"guide":g} })

def update_darkd(d,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"darkd":d} })
def update_obvd(o,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"obvd":o} })
def update_sweatd(s,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"sweatd":s} })

def update_obvc(o,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"obvc":o} })
def update_sweatc(s,markett):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_count = db["count"]
    collection_count.update_one({"market": markett},{"$set":{"sweatc":s} })
class CountCandle:
    Down = False
    Up = False
    def __init__(self,market):
        self.market = market
    def take_order_point(self):

        global dark_ada
        global obv_ada
        global sweat_ada

        global dark_bnb
        global obv_bnb
        global sweat_bnb

        

        positionAmtShort = 0
        positionAmtLong = 0


        client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")
        db = client.Binance
        collection_cound = db["count"]

        ada_c_data = collection_cound.find_one({"market": 'ADAUSD_PERP'})

        bnb_c_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})
        
        #btc_c_data = collection_cound.find_one({"market": 'BTCUSD_PERP'})

        #bnbu_c_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})

        dark_ada = ada_c_data["dark"]
        obv_ada = ada_c_data["obv"]
        sweat_ada= ada_c_data["sweat"]


        dark_bnb = bnb_c_data["dark"]
        obv_bnb = bnb_c_data["obv"]
        sweat_bnb = bnb_c_data["sweat"]


        #obv_btc = btc_c_data["obv"]
        #sweat_btc= btc_c_data["sweat"]

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
                pl = str(round(float(priceIn) -((0.25* float(priceIn))/20),3))
                pll = str(round(float(priceIn) -((thr_p* float(priceIn))/20),3))
                if (float(positionAmtLong) >= 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((obv_bnb ==2 and sweat_bnb ==2) and (float(positionAmtShort) >= 0) and (float(positionAmtShort) < 90)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbnb)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0

                        time.sleep(1)
                    elif ((obv_bnb ==2 and sweat_bnb ==2) and (float(positionAmtShort) >= 90) ):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbnb*15)
                        PrintBasic.print_obj(take_order_long)
                       # update_obv(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0

                        time.sleep(1)
                # elif ((float(positionAmtLong) > 0) and  (float(mPrice) >= float(p))):
            
                #     # client = MongoClient(port=27017)
                #     # db = client.binance
                #     # collection_ltc = db["count"]
                #     # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                #     # dark = ltc_data["dark"]
                #     # obv = ltc_data["obv"]
                #     # sweat = ltc_data["sweat"]
                #     # if ((float(dark)+float(obv)+float(sweat)) <3):
                #     if ((dark_bnb+obv_bnb+sweat_bnb) >= 1 and (dark_bnb+obv_bnb+sweat_bnb) < 6 ):
                #         Up = False
                #         Down = True
                #         print("TP_LONG",True)
                #         time.sleep(1)
                #         print("take_profit_long")
                #         take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                #         PrintBasic.print_obj(take_order_long)
                #         #update_obv(0,'BNBUSD_PERP')
                #         #update_dark(0,'BNBUSD_PERP')
                #         update_sweat(0,'BNBUSD_PERP')
                #         update_guide(0,'BNBUSD_PERP')
                #         #dark_bnb = 0
                #         #obv_bnb = 0
                #         sweat_bnb = 0
                #         guide_bnb = 0
                #         time.sleep(1)
                    # elif ((obv_bnb+sweat_bnb) ==4 and (float(a) < float(step_two_unitbnb))):
                    #     Up = False
                    #     Down = True
                    #     print("TP_LONG",True)
                    #     time.sleep(1)
                    #     print("take_profit_long")
                    #     take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitbnb)
                    #     PrintBasic.print_obj(take_order_long)
                    #     #update_obv(0,'BNBUSD_PERP')
                    #     #update_dark(0,'BNBUSD_PERP')
                    #     update_sweat(0,'BNBUSD_PERP')
                    #     #update_guide(0,'BNBUSD_PERP')
                    #     #dark_bnb = 0
                    #     #obv_bnb = 0
                    #     sweat_bnb = 0
                    #     #guide_bnb = 0
                    #     time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitbnb)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((obv_bnb ==2 and sweat_bnb ==2)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbnb)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0
                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unitbnb)) and (float(positionAmtLong) < float(step_three_unitbnb)) and  (float(mPrice) <= float(pll))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]
                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((obv_bnb ==2 and sweat_bnb ==2)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbnb)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0
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
                if (float(positionAmtShort) >= 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((obv_bnb ==1 and sweat_bnb ==1) and (float(positionAmtLong) >= 0) and (float(positionAmtLong) < 90)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbnb)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0

                        time.sleep(1)
                    elif ((obv_bnb ==1 and sweat_bnb ==1) and (float(positionAmtLong) >= 90)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbnb*15)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0

                        time.sleep(1)
                # elif (float(positionAmtShort) > 0 and  (float(mPrices) <= float(ps))):
                #     # client = MongoClient(port=27017)
                #     # db = client.binance
                #     # collection_ltc = db["count"]

                #     # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                #     # dark = ltc_data["dark"]
                #     # obv = ltc_data["obv"]
                #     # sweat = ltc_data["sweat"]
                #     # if ((float(dark)+float(obv)+float(sweat)) <3):
                #     if ((dark_bnb+obv_bnb+sweat_bnb) >= 3):
                #         Down = False
                #         Up = True

                #         print("TP_SHORT ",Down)
                #         time.sleep(1)
                
                #         print("take_order_short_full")

                #         take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                #         PrintBasic.print_obj(take_order_short)
                #         #update_obv(0,'BNBUSD_PERP')
                #         #update_dark(0,'BNBUSD_PERP')
                #         update_sweat(0,'BNBUSD_PERP')
                #         update_guide(0,'BNBUSD_PERP')
                #         #dark_bnb = 0
                #         #obv_bnb = 0
                #         sweat_bnb = 0
                #         guide_bnb = 0

                #         time.sleep(1)
                    # elif ((obv_bnb ==1 and sweat_bnb ==1) and (float(ass) < float(step_two_unitbnb))):
                    #     Down = False
                    #     Up = True

                    #     print("TP_SHORT ",Down)
                    #     time.sleep(1)
                
                    #     print("take_order_short_full")

                    #     take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitbnb)
                    #     PrintBasic.print_obj(take_order_short)
                    #     #update_obv(0,'BNBUSD_PERP')
                    #     #update_dark(0,'BNBUSD_PERP')
                    #     update_sweat(0,'BNBUSD_PERP')
                    #     #update_guide(0,'BNBUSD_PERP')
                    #     #dark_bnb = 0
                    #     #obv_bnb = 0
                    #     sweat_bnb = 0
                    #     #guide_bnb = 0

                    #     time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitbnb) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((obv_bnb ==1 and sweat_bnb ==1)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbnb)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unitbnb) and float(positionAmtShort) < float(step_three_unitbnb) and (float(mPrices) >= float(psss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_ltc = db["count"]

                    # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
                    # dark = ltc_data["dark"]
                    # obv = ltc_data["obv"]
                    # sweat = ltc_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((obv_bnb ==1 and sweat_bnb ==1)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbnb)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv(0,'BNBUSD_PERP')
                        #update_dark(0,'BNBUSD_PERP')
                        update_sweat(0,'BNBUSD_PERP')
                        #update_guide(0,'BNBUSD_PERP')
                        #dark_bnb = 0
                        #obv_bnb = 0
                        sweat_bnb = 0
                        #guide_bnb = 0

                        time.sleep(1)



        # for key in object_list:
        #     if (key.get('positionSide') =='SHORT' and (key.get('symbol') == "BTCUSD_PERP")):
        #         positionAmtShort = key.get('positionAmt')*-1
        #     if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BTCUSD_PERP")):
        #         positionAmtLong = key.get('positionAmt')
        #         priceIn = key.get('entryPrice')
        #         mPrice = key.get('markPrice')
        #         a = str(round(float(positionAmtLong),0))
        #         p = str(round(float(priceIn) +((0.025* float(priceIn))/20),3))
        #         pl = str(round(float(priceIn) -((0.25* float(priceIn))/20),3))
        #         pll = str(round(float(priceIn) -((thr_p* float(priceIn))/20),3))
        #         if (float(positionAmtLong) == 0):
        
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((obv_btc ==2 and sweat_btc ==2) and (float(positionAmtShort) >= 0) and (float(positionAmtShort) < 90)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbtc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 #update_dark(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0

        #                 time.sleep(1)
        #             elif ((obv_btc ==2 and sweat_btc ==2) and (float(positionAmtShort) >= 90) ):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbtc*15)
        #                 PrintBasic.print_obj(take_order_long)
        #                # update_obv(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0

        #                 time.sleep(1)
        #         # elif ((float(positionAmtLong) > 0) and  (float(mPrice) >= float(p))):
            
        #         #     # client = MongoClient(port=27017)
        #         #     # db = client.binance
        #         #     # collection_ltc = db["count"]
        #         #     # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #         #     # dark = ltc_data["dark"]
        #         #     # obv = ltc_data["obv"]
        #         #     # sweat = ltc_data["sweat"]
        #         #     # if ((float(dark)+float(obv)+float(sweat)) <3):
        #         #     if ((dark_bnb+obv_bnb+sweat_bnb) >= 1 and (dark_bnb+obv_bnb+sweat_bnb) < 6 ):
        #         #         Up = False
        #         #         Down = True
        #         #         print("TP_LONG",True)
        #         #         time.sleep(1)
        #         #         print("take_profit_long")
        #         #         take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
        #         #         PrintBasic.print_obj(take_order_long)
        #         #         #update_obv(0,'BNBUSD_PERP')
        #         #         #update_dark(0,'BNBUSD_PERP')
        #         #         update_sweat(0,'BNBUSD_PERP')
        #         #         update_guide(0,'BNBUSD_PERP')
        #         #         #dark_bnb = 0
        #         #         #obv_bnb = 0
        #         #         sweat_bnb = 0
        #         #         guide_bnb = 0
        #         #         time.sleep(1)
        #             elif ((obv_btc+sweat_btc) ==4 and (float(a) < float(step_two_unitbtc))):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unitbtc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 #update_dark(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unitbtc)) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((obv_btc ==2 and sweat_btc ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbtc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 #update_dark(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) >= float(step_two_unitbtc)) and (float(positionAmtLong) < float(step_three_unitbtc)) and  (float(mPrice) <= float(pll))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]
        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((obv_btc ==2 and sweat_btc ==2)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unitbtc)
        #                 PrintBasic.print_obj(take_order_long)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 #update_dark(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0
        #                 time.sleep(1)
        # for keys in object_list:
        #     if (keys.get('positionSide') =='LONG' and (keys.get('symbol') == "BTCUSD_PERP")):

        #         positionAmtLong = keys.get('positionAmt')
        #     if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BTCUSD_PERP")):

        #         positionAmtShort = keys.get('positionAmt')*-1
        #         mPrices = keys.get('markPrice')
        #         priceIns = keys.get('entryPrice')
        #         ass = str(round(float(positionAmtShort),0))
        #         ps = str(round(float(priceIns) -((0.025* float(priceIns))/20),3))
        #         pss = str(round(float(priceIns) +((0.35* float(priceIns))/20),3))
        #         psss = str(round(float(priceIns) +((0.50* float(priceIns))/20),3))
        #         if (float(positionAmtShort) == 0):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((obv_btc ==1 and sweat_btc ==1) and (float(positionAmtLong) >= 0) and (float(positionAmtLong) < 90)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BTCUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbtc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0

        #                 time.sleep(1)
        #             elif ((obv_btc ==1 and sweat_btc ==1) and (float(positionAmtLong) >= 90)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BTCUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbtc*15)
        #                 PrintBasic.print_obj(take_order_short)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0

        #                 time.sleep(1)
        #         # elif (float(positionAmtShort) > 0 and  (float(mPrices) <= float(ps))):
        #         #     # client = MongoClient(port=27017)
        #         #     # db = client.binance
        #         #     # collection_ltc = db["count"]

        #         #     # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #         #     # dark = ltc_data["dark"]
        #         #     # obv = ltc_data["obv"]
        #         #     # sweat = ltc_data["sweat"]
        #         #     # if ((float(dark)+float(obv)+float(sweat)) <3):
        #         #     if ((dark_bnb+obv_bnb+sweat_bnb) >= 3):
        #         #         Down = False
        #         #         Up = True

        #         #         print("TP_SHORT ",Down)
        #         #         time.sleep(1)
                
        #         #         print("take_order_short_full")

        #         #         take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
        #         #         PrintBasic.print_obj(take_order_short)
        #         #         #update_obv(0,'BNBUSD_PERP')
        #         #         #update_dark(0,'BNBUSD_PERP')
        #         #         update_sweat(0,'BNBUSD_PERP')
        #         #         update_guide(0,'BNBUSD_PERP')
        #         #         #dark_bnb = 0
        #         #         #obv_bnb = 0
        #         #         sweat_bnb = 0
        #         #         guide_bnb = 0

        #         #         time.sleep(1)
        #             elif ((obv_btc ==1 and sweat_btc ==1) and (float(ass) < float(step_two_unitbtc))):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unitbtc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 #update_dark(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unitbtc) and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((obv_btc ==1 and sweat_btc ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BTCUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbtc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 #update_dark(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) >= float(step_two_unitbtc) and float(positionAmtShort) < float(step_three_unitbtc) and (float(mPrices) >= float(psss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_ltc = db["count"]

        #             # ltc_data = collection_ltc.find_one({"market": 'LTCUSDT'})   
        #             # dark = ltc_data["dark"]
        #             # obv = ltc_data["obv"]
        #             # sweat = ltc_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((obv_btc ==1 and sweat_btc ==1)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BTCUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unitbtc)
        #                 PrintBasic.print_obj(take_order_short)
        #                 #update_obv(0,'BNBUSD_PERP')
        #                 #update_dark(0,'BNBUSD_PERP')
        #                 update_sweat(0,'BTCUSD_PERP')
        #                 #update_guide(0,'BNBUSD_PERP')
        #                 #dark_bnb = 0
        #                 #obv_bnb = 0
        #                 sweat_btc = 0
        #                 #guide_bnb = 0

        #                 time.sleep(1)

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

    ada_c_data = collection_cound.find_one({"market": 'ADAUSD_PERP'})
    #btc_c_data = collection_cound.find_one({"market": 'BTCUSD_PERP'})

    bnb_con_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})

    

    bnbc_data  = collection_cutloss.find_one({"market": 'BNBUSD_PERP'})
    adac_data  = collection_cutloss.find_one({"market": 'ADAUSD_PERP'}) 
    #btcc_data  = collection_cutloss.find_one({"market": 'BTCUSD_PERP'})    
    market ='BNBUSD_PERP'
    marketc = 'BTCUSD_PERP'
    marketd = 'ADAUSD_PERP'

    dark_ada = ada_c_data["dark"]
    obv_ada = ada_c_data["obv"]
    sweat_ada = ada_c_data["sweat"]

    dark_bnb = bnb_con_data["dark"]
    obv_bnb = bnb_con_data["obv"]
    sweat_bnb = bnb_con_data["sweat"]
    
    #obv_btc = btc_c_data["obv"]
    #sweat_btc = btc_c_data["sweat"]



    buy_unitbnb = bnbc_data["buy"]
    sale_unitbnb = bnbc_data["sale"]
    step_one_unitbnb = bnbc_data["step_one_unit"]
    step_two_unitbnb = bnbc_data["step_two_unit"]
    step_three_unitbnb = bnbc_data["step_three_unit"]
    step_four_unitbnb = bnbc_data["step_four_unit"]

    buy_unitada = adac_data["buy"]
    sale_unitada = adac_data["sale"]
    step_one_unitada = adac_data["step_one_unit"]
    step_two_unitada = adac_data["step_two_unit"]
    step_three_unitada = adac_data["step_three_unit"]
    step_four_unitada = adac_data["step_four_unit"]

    #buy_unitbtc = btcc_data["buy"]
    #sale_unitbtc = btcc_data["sale"]
    #step_one_unitbtc = btcc_data["step_one_unit"]
    #step_two_unitbtc = btcc_data["step_two_unit"]
    #step_three_unitbtc = btcc_data["step_three_unit"]
    #step_four_unitbtc = btcc_data["step_four_unit"]

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

