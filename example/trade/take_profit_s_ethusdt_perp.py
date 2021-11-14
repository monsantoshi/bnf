from typing import KeysView
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
import config
import json
import tempfile

detach_dir = 'c:\db'
class OkEx1(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
     
    def run(self):
        print("Starting: 1 " + self.name + "\n")
        k1 = getmail(market)
        k1.two_way_email("imap.gmail.com", "tedview33@gmail.com", "MoN3318#")
        #two_way_email("imap.gmail.com", "tedview88@gmail.com", "MoN3318#")
        #two_way_email("imap.gmail.com", "tedview1@gmail.com", "MoN3318#")
        #two_way_email("imap.gmail.com", "tedview59@gmail.com", "MoN3318#")
        print("Exiting: 1 " + self.name + "\n")
class OkEx2(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
     
    def run(self):
        print("Starting: 2 " + self.name + "\n")
        #two_way_email("imap.gmail.com", "monsan@gmail.com", "yevmkqcsnolrooti")
        k2 = getmail(market)
        k2.two_way_email("imap.gmail.com", "tedview34@gmail.com", "MoN3318#")
        #two_way_email("imap.gmail.com", "tedview1@gmail.com", "MoN3318#")
        #two_way_email("imap.gmail.com", "tedview59@gmail.com", "MoN3318#")
        print("Exiting: 2 " + self.name + "\n")
class Bin1(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 1" + self.name + "\n")
        b1 = CheckProfitLong(market)
        b1.check_profit_long_atom()
        print("Exiting: 1" + self.name + "\n")

class Bin2(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 2" + self.name + "\n")
        b2 = CheckProfitShort(market)
        b2.check_profit_short_atom()
        print("Exiting: 2" + self.name + "\n")
class Bin3(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 3" + self.name + "\n")
        b3 = TryToTakeOrder(market)
        b3.take_order_point()
        print("Exiting: 3" + self.name + "\n")
class Bin4(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 4" + self.name + "\n")
        b4 = TryToTakeOrder(market)
        b4.take_order_point_short()
        print("Exiting: 5" + self.name + "\n")
class Bin5(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 5" + self.name + "\n")
        b5 = TryToTakeOrder(market)
        b5.take_order_point_long()
        print("Exiting: 5" + self.name + "\n")
class Bin6(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 6" + self.name + "\n")
        b6 = CheckProfitLongFromOut(market)
        b6.check_profit_long_atom()
        print("Exiting: 6" + self.name + "\n")
class Bin7(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 7" + self.name + "\n")
        b7 = CheckProfitShortFromOut(market)
        b7.check_profit_short_atom()
        print("Exiting: 7" + self.name + "\n")
class Bin8(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 8" + self.name + "\n")
        b8 = CheckLossLong(market)
        b8.check_loss_long_atom()
        print("Exiting: 8" + self.name + "\n")
class Bin9(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 9" + self.name + "\n")
        b9 = CheckLossShort(market)
        b9.check_loss_short_atom()
        print("Exiting: 9" + self.name + "\n")
class Bin11(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 11 " + self.name + "\n")
        b11 = CheckProfitLongMore(market)
        b11.check_profit_long_atom()
        print("Exiting: 11 " + self.name + "\n")

class Bin12(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 12 " + self.name + "\n")
        b12 = CheckProfitShortMore(market)
        b12.check_profit_short_atom()
        print("Exiting: 12 " + self.name + "\n")

class Bin13(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 13" + self.name + "\n")
        b13 = CheckLossLongFromIn(market)
        b13.check_profit_long_atom()
        print("Exiting: 13" + self.name + "\n")
class Bin14(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 14" + self.name + "\n")
        b14 = CheckLossShortFromIn(market)
        b14.check_profit_short_atom()
        print("Exiting: 14" + self.name + "\n")
       
class TryToTakeOrder:

    def __init__(self,market):
        self.market = market

    def take_order_point(self):

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


        result = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
        init_bq = []
        init_bp = []
        init_aq = []
        init_ap = []
        bid_q = []
        bid_p = []
        ask_q = []
        ask_p = []
        price_bids = []
        price_asks = []
        Up = False
        Down = False
        for resb in result.bids:
            init_bq.append(round(float(resb.qty),4))
            init_bp.append(round(float(resb.price),4))
        for resa in result.asks:
            init_aq.append(round(float(resa.qty),4))
            init_ap.append(round(float(resa.price),4))
        index_init_bq = init_bq.index(max(init_bq))
        init_price_bid = init_bp[index_init_bq]
        #print("init_price_bid" ,init_price_bid)
        index_init_aq = init_aq.index(max(init_aq))
        init_price_ask = init_ap[index_init_aq]
        #print("init_price_ask" ,init_price_ask)
        time.sleep(1)
        price_bids.append(init_price_bid)
        price_asks.append(init_price_ask)

        for i in range(20):
            result_xtz = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
            #time.sleep(1)
            for resb in result_xtz.bids:
                #print(resb.qty)
                bid_q.append(round(float(resb.qty),4))
                bid_p.append(round(float(resb.price),4))

               
            for resa in result_xtz.asks:
                #print(resb.qty)
                ask_q.append(round(float(resa.qty),4))
                ask_p.append(round(float(resa.price),4))

            index_bid = bid_q.index(max(bid_q))
            index_ask = ask_q.index(max(ask_q))
            #print("index ask ",index_ask)
            #print("ask price ",ask_p[index_ask])
            #print("index bid ",index_bid)
            #print("bid price ",bid_p[index_bid])

            if bid_q[index_bid] != price_bids[-1]:
                price_bids.append(bid_p[index_bid])
            #print("price_bids in loop ",price_bids)
            if ask_q[index_ask] != price_asks[-1]:
                price_asks.append(ask_p[index_ask])
            #print("price_asks in loop ",price_asks)
            time.sleep(1)
        #print("price_asks : ",price_asks)
        #print("price_bids : ",price_bids)
        #print("price_asks_first ",price_asks[0])
        #print("price_asks_last ",price_asks[39])
        #print("price_bids_first ",price_bids[0])
        #print("price_bids_last ",price_bids[39])
        s = 0
        l = 0
        if (price_asks[0]< price_asks[19]):
            s = 0
        elif (price_asks[0] > price_asks[19]):
            s = 1
        #print(" s ",s)

        if (price_bids[0]< price_bids[19]):
            l = 1
        elif (price_bids[0] > price_bids[19]):
            l = 0
        #old matomod
        kline2 = request_client.get_candlestick_data(symbol="ATOMUSDT", interval=CandlestickInterval.MIN3,startTime=None, endTime=None, limit=20)
        #print("======= Kline/Candlestick Data =======")
        #PrintMix.print_data(result[0].volume)
        #print("======================================")
        open_list = []
        for res in kline2:
            d = collections.defaultdict()
            d['open'] = res.open
            d['high'] = res.high
            d['low'] = res.low
            d['close'] = res.close
            #d['unRealizedProfit'] = res.unRealizedProfit
            open_list.append(d)

        open0 = open_list[6]["open"]
        high0 = open_list[6]["high"]
        low0 = open_list[6]["low"]
        close0 = open_list[6]["close"]
        open1 = open_list[5]["open"]
        high1 = open_list[5]["high"]
        low1 = open_list[5]["low"]
        close1 = open_list[5]["close"]
        open2 = open_list[4]["open"]
        high2 = open_list[4]["high"]
        low2 = open_list[4]["low"]
        close2 = open_list[4]["close"]
        open3 = open_list[3]["open"]
        high3 = open_list[3]["high"]
        low3 = open_list[3]["low"]
        close3 = open_list[3]["close"]
        open4 = open_list[2]["open"]
        high4 = open_list[2]["high"]
        low4 = open_list[2]["low"]
        close4 = open_list[2]["close"]
        open5 = open_list[1]["open"]
        high5 = open_list[1]["high"]
        low5 = open_list[1]["low"]
        close5 = open_list[1]["close"]
        open6 = open_list[0]["open"]
        high6 = open_list[0]["high"]
        low6 = open_list[0]["low"]
        close6 = open_list[0]["close"]
        haclose = (float(open0)+float(high0)+float(low0)+float(close0))/4
        haclose1 = (float(open1)+float(high1)+float(low1)+float(close1))/4
        haclose2 = (float(open2)+float(high2)+float(low2)+float(close2))/4
        haclose3 = (float(open3)+float(high3)+float(low3)+float(close3))/4
        haclose4 = (float(open4)+float(high4)+float(low4)+float(close4))/4
        haclose5 = (float(open5)+float(high5)+float(low5)+float(close5))/4
        haclose6 = (float(open6)+float(high6)+float(low6)+float(close6))/4
        haopen6 = (float(open6)+float(close6))/2
        if (math.isnan(float(haopen6))):
            haopen5 = (float(haopen5)+float(haclose5))/2
        else:
            haopen5 = (float(haopen6)+float(haclose6))/2
        if (math.isnan(float(haopen5))):
            haopen4 = (float(haopen4)+float(haclose4))/2
        else:
            haopen4 = (float(haopen5)+float(haclose5))/2
        if (math.isnan(float(haopen4))):
            haopen3 = (float(haopen3)+float(haclose3))/2
        else:
            haopen3 = (float(haopen4)+float(haclose4))/2
        if (math.isnan(float(haopen3))):
            haopen2 = (float(haopen2)+float(haclose2))/2
        else:
            haopen2 = (float(haopen3)+float(haclose3))/2
        if (math.isnan(float(haopen2))):
            haopen1 = (float(haopen1)+float(haclose1))/2
        else:
            haopen1 = (float(haopen2)+float(haclose2))/2
        if (math.isnan(float(haopen1))):
            haopen = (float(haopen)+float(haclose))/2
        else:
            haopen = (float(haopen1)+float(haclose1))/2

        Down =  (float(haopen) > float(haclose)) and (s == 1)
        #atom_TrendDown = Bearish_Engulfing
        print("Down",Down)
        Up =  (float(haopen) < float(haclose)) and (l == 1)
        #atom_TrendUp =  Bullish_Engulfing
        print("Up",Up)
        result_p = request_client.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        order_list = []
        for resp in result_p:
            p = collections.defaultdict()
            p['symbol'] = resp.symbol
            p['positionAmt'] = resp.positionAmt
            p['entryPrice'] = resp.entryPrice
            p['markPrice'] = resp.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            order_list.append(p)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15])
        print(order_list[0]["symbol"]+'  '+str(order_list[0]["positionAmt"])+'  '+str(order_list[0]["entryPrice"])+'  '+str(order_list[0]["markPrice"]))
        print(order_list[1]["symbol"]+'  '+str(order_list[1]["positionAmt"])+'  '+str(order_list[1]["entryPrice"])+'  '+str(order_list[1]["markPrice"]))
        #time.sleep(1)
        #if ((order_list[0]["positionAmt"]) < step_one_unit)) :

        if ((Down)):
       
            print("take_order_short_full")
            take_order_sell(self)
            #take_order_short = request_client.post_order(symbol="ATOMUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
            #PrintBasic.print_obj(take_order_short)
            #time.sleep(1)

            return
       
        if ((Up)):
            print("take_order_long_full")
            take_order_buy(self)
            #take_order_long = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
            #PrintBasic.print_obj(take_order_long)
            time.sleep(1)
 
            return


    def take_order_point_long(self):


        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

        result = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
        init_bq = []
        init_bp = []
        init_aq = []
        init_ap = []
        bid_q = []
        bid_p = []
        ask_q = []
        ask_p = []
        price_bids = []
        price_asks = []
        up = False
        Down = False
       
        for res in result.bids:
            init_bq.append(round(float(res.qty),4))
            init_bp.append(round(float(res.price),4))
        for res in result.asks:
            init_aq.append(round(float(res.qty),4))
            init_ap.append(round(float(res.price),4))
        index_init_bq = init_bq.index(max(init_bq))
        init_price_bid = init_bp[index_init_bq]
        #print("init_price_bid" ,init_price_bid)
        index_init_aq = init_aq.index(max(init_aq))
        init_price_ask = init_ap[index_init_aq]
        #print("init_price_ask" ,init_price_ask)
        time.sleep(1)
        price_bids.append(init_price_bid)
        price_asks.append(init_price_ask)

        for i in range(20):
            result_xtz = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
            #time.sleep(1)
            for resb in result_xtz.bids:
                #print(resb.qty)
                bid_q.append(round(float(resb.qty),4))
                bid_p.append(round(float(resb.price),4))

               
            for resa in result_xtz.asks:
                #print(resb.qty)
                ask_q.append(round(float(resa.qty),4))
                ask_p.append(round(float(resa.price),4))

            index_bid = bid_q.index(max(bid_q))
            index_ask = ask_q.index(max(ask_q))
            #print("index ask ",index_ask)
            #print("ask price ",ask_p[index_ask])
            #print("index bid ",index_bid)
            #print("bid price ",bid_p[index_bid])

            if bid_q[index_bid] != price_bids[-1]:
                price_bids.append(bid_p[index_bid])
            #print("price_bids in loop ",price_bids)
            if ask_q[index_ask] != price_asks[-1]:
                price_asks.append(ask_p[index_ask])
            #print("price_asks in loop ",price_asks)
            time.sleep(1)
        #print("price_asks : ",price_asks)
        #print("price_bids : ",price_bids)
        #print("price_asks_first ",price_asks[0])
        #print("price_asks_last ",price_asks[39])
        #print("price_bids_first ",price_bids[0])
        #print("price_bids_last ",price_bids[39])
        s = 0
        l = 0
        if (price_asks[0]< price_asks[19]):
            s = 0
        elif (price_asks[0] > price_asks[19]):
            s = 1
        #print(" s ",s)

        if (price_bids[0]< price_bids[19]):
            l = 1
        elif (price_bids[0] > price_bids[19]):
            l = 0
        #old matomod
        kline2 = request_client.get_candlestick_data(symbol="ATOMUSDT", interval=CandlestickInterval.MIN3,startTime=None, endTime=None, limit=20)
        #print("======= Kline/Candlestick Data =======")
        #PrintMix.print_data(result[0].volume)
        #print("======================================")
        open_list = []
        for res in kline2:
            d = collections.defaultdict()
            d['open'] = res.open
            d['high'] = res.high
            d['low'] = res.low
            d['close'] = res.close
            #d['unRealizedProfit'] = res.unRealizedProfit
            open_list.append(d)

        open0 = open_list[6]["open"]
        high0 = open_list[6]["high"]
        low0 = open_list[6]["low"]
        close0 = open_list[6]["close"]
        open1 = open_list[5]["open"]
        high1 = open_list[5]["high"]
        low1 = open_list[5]["low"]
        close1 = open_list[5]["close"]
        open2 = open_list[4]["open"]
        high2 = open_list[4]["high"]
        low2 = open_list[4]["low"]
        close2 = open_list[4]["close"]
        open3 = open_list[3]["open"]
        high3 = open_list[3]["high"]
        low3 = open_list[3]["low"]
        close3 = open_list[3]["close"]
        open4 = open_list[2]["open"]
        high4 = open_list[2]["high"]
        low4 = open_list[2]["low"]
        close4 = open_list[2]["close"]
        open5 = open_list[1]["open"]
        high5 = open_list[1]["high"]
        low5 = open_list[1]["low"]
        close5 = open_list[1]["close"]
        open6 = open_list[0]["open"]
        high6 = open_list[0]["high"]
        low6 = open_list[0]["low"]
        close6 = open_list[0]["close"]
        haclose = (float(open0)+float(high0)+float(low0)+float(close0))/4
        haclose1 = (float(open1)+float(high1)+float(low1)+float(close1))/4
        haclose2 = (float(open2)+float(high2)+float(low2)+float(close2))/4
        haclose3 = (float(open3)+float(high3)+float(low3)+float(close3))/4
        haclose4 = (float(open4)+float(high4)+float(low4)+float(close4))/4
        haclose5 = (float(open5)+float(high5)+float(low5)+float(close5))/4
        haclose6 = (float(open6)+float(high6)+float(low6)+float(close6))/4
        haopen6 = (float(open6)+float(close6))/2
        if (math.isnan(float(haopen6))):
            haopen5 = (float(haopen5)+float(haclose5))/2
        else:
            haopen5 = (float(haopen6)+float(haclose6))/2
        if (math.isnan(float(haopen5))):
            haopen4 = (float(haopen4)+float(haclose4))/2
        else:
            haopen4 = (float(haopen5)+float(haclose5))/2
        if (math.isnan(float(haopen4))):
            haopen3 = (float(haopen3)+float(haclose3))/2
        else:
            haopen3 = (float(haopen4)+float(haclose4))/2
        if (math.isnan(float(haopen3))):
            haopen2 = (float(haopen2)+float(haclose2))/2
        else:
            haopen2 = (float(haopen3)+float(haclose3))/2
        if (math.isnan(float(haopen2))):
            haopen1 = (float(haopen1)+float(haclose1))/2
        else:
            haopen1 = (float(haopen2)+float(haclose2))/2
        if (math.isnan(float(haopen1))):
            haopen = (float(haopen)+float(haclose))/2
        else:
            haopen = (float(haopen1)+float(haclose1))/2



        Down =  (float(haopen) > float(haclose)) and (s == 1)
        #atom_TrendDown = Bearish_Engulfing
        print("Down",Down)
        Up =  (float(haopen) < float(haclose)) and (l == 1)
        #atom_TrendUp =  Bullish_Engulfing
        print("Up",Up)
        result_p = request_client.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        order_list = []
        for resp in result_p:
            p = collections.defaultdict()
            p['symbol'] = resp.symbol
            p['positionAmt'] = resp.positionAmt
            p['entryPrice'] = resp.entryPrice
            p['markPrice'] = resp.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            order_list.append(p)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15])
        long_price = float(order_list[0]["entryPrice"])
        long_amount = float(order_list[0]["positionAmt"])

       
        int_cur_long_price = float(order_list[0]["markPrice"])

       
        int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20

        print(order_list[0]["symbol"]+'  '+str(order_list[0]["positionAmt"])+'  '+str(order_list[0]["entryPrice"])+'  '+str(order_list[0]["markPrice"]))
        time.sleep(1)
        if (((order_list[0]["positionAmt"]) > 0) and ((order_list[0]["positionAmt"]) <= step_one_unit)):


           
            if ((Up)):
                print("take_order_long_full")
                take_order_buy(self)
                #take_order_long = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity= buy_unit)
                #PrintBasic.print_obj(take_order_long)
                time.sleep(1)
     
                return
        if (((order_list[0]["positionAmt"]) > step_one_unit) and ((order_list[0]["positionAmt"]) < step_two_unit) and (abs(int_long_rate * 100) > min_profit_rate_long) and (abs(int_long_rate * 100) < abs(stop_loss_rate_long))):


           
            if ((Up)):
                take_order_buy(self)
                #take_order_long = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity= buy_unit)
                #PrintBasic.print_obj(take_order_long)
                time.sleep(1)
     
                return
        if (((order_list[0]["positionAmt"]) >= step_two_unit) and ((order_list[0]["positionAmt"]) <= step_three_unit) and (abs(int_long_rate * 100) > min_profit_rate_long) and (abs(int_long_rate * 100) < abs(stop_loss_rate_long))):


           
            if ((Up)):
                print("take_order_long_full")
                take_order_buy(self)
                #take_order_long = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity= buy_unit)
                #PrintBasic.print_obj(take_order_long)
                time.sleep(1)
     
                return

        return
    def take_order_point_short(self):


        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)



        result = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
        init_bq = []
        init_bp = []
        init_aq = []
        init_ap = []
        bid_q = []
        bid_p = []
        ask_q = []
        ask_p = []
        price_bids = []
        price_asks = []
        Down = False
        Up = False
        for res in result.bids:
            init_bq.append(round(float(res.qty),4))
            init_bp.append(round(float(res.price),4))
        for res in result.asks:
            init_aq.append(round(float(res.qty),4))
            init_ap.append(round(float(res.price),4))
        index_init_bq = init_bq.index(max(init_bq))
        init_price_bid = init_bp[index_init_bq]
        #print("init_price_bid" ,init_price_bid)
        index_init_aq = init_aq.index(max(init_aq))
        init_price_ask = init_ap[index_init_aq]
        #print("init_price_ask" ,init_price_ask)
        time.sleep(1)
        price_bids.append(init_price_bid)
        price_asks.append(init_price_ask)

        for i in range(20):
            result_xtz = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
            time.sleep(1)
            for resb in result_xtz.bids:
                #print(resb.qty)
                bid_q.append(round(float(resb.qty),4))
                bid_p.append(round(float(resb.price),4))

               
            for resa in result_xtz.asks:
                #print(resb.qty)
                ask_q.append(round(float(resa.qty),4))
                ask_p.append(round(float(resa.price),4))

            index_bid = bid_q.index(max(bid_q))
            index_ask = ask_q.index(max(ask_q))
            #print("index ask ",index_ask)
            #print("ask price ",ask_p[index_ask])
            #print("index bid ",index_bid)
            #print("bid price ",bid_p[index_bid])

            if bid_q[index_bid] != price_bids[-1]:
                price_bids.append(bid_p[index_bid])
            #print("price_bids in loop ",price_bids)
            if ask_q[index_ask] != price_asks[-1]:
                price_asks.append(ask_p[index_ask])

        s = 0
        l = 0
        if (price_asks[0]< price_asks[19]):
            s = 0
        elif (price_asks[0] > price_asks[19]):
            s = 1
        #print(" s ",s)

        if (price_bids[0]< price_bids[19]):
            l = 1
        elif (price_bids[0] > price_bids[19]):
            l = 0
        #old matomod
        kline2 = request_client.get_candlestick_data(symbol="ATOMUSDT", interval=CandlestickInterval.MIN3,startTime=None, endTime=None, limit=20)
        #print("======= Kline/Candlestick Data =======")
        #PrintMix.print_data(result[0].volume)
        #print("======================================")
        open_list = []
        for res in kline2:
            d = collections.defaultdict()
            d['open'] = res.open
            d['high'] = res.high
            d['low'] = res.low
            d['close'] = res.close

            open_list.append(d)

        open0 = open_list[6]["open"]
        high0 = open_list[6]["high"]
        low0 = open_list[6]["low"]
        close0 = open_list[6]["close"]
        open1 = open_list[5]["open"]
        high1 = open_list[5]["high"]
        low1 = open_list[5]["low"]
        close1 = open_list[5]["close"]
        open2 = open_list[4]["open"]
        high2 = open_list[4]["high"]
        low2 = open_list[4]["low"]
        close2 = open_list[4]["close"]
        open3 = open_list[3]["open"]
        high3 = open_list[3]["high"]
        low3 = open_list[3]["low"]
        close3 = open_list[3]["close"]
        open4 = open_list[2]["open"]
        high4 = open_list[2]["high"]
        low4 = open_list[2]["low"]
        close4 = open_list[2]["close"]
        open5 = open_list[1]["open"]
        high5 = open_list[1]["high"]
        low5 = open_list[1]["low"]
        close5 = open_list[1]["close"]
        open6 = open_list[0]["open"]
        high6 = open_list[0]["high"]
        low6 = open_list[0]["low"]
        close6 = open_list[0]["close"]
        haclose = (float(open0)+float(high0)+float(low0)+float(close0))/4
        haclose1 = (float(open1)+float(high1)+float(low1)+float(close1))/4
        haclose2 = (float(open2)+float(high2)+float(low2)+float(close2))/4
        haclose3 = (float(open3)+float(high3)+float(low3)+float(close3))/4
        haclose4 = (float(open4)+float(high4)+float(low4)+float(close4))/4
        haclose5 = (float(open5)+float(high5)+float(low5)+float(close5))/4
        haclose6 = (float(open6)+float(high6)+float(low6)+float(close6))/4
        haopen6 = (float(open6)+float(close6))/2
        if (math.isnan(float(haopen6))):
            haopen5 = (float(haopen5)+float(haclose5))/2
        else:
            haopen5 = (float(haopen6)+float(haclose6))/2
        if (math.isnan(float(haopen5))):
            haopen4 = (float(haopen4)+float(haclose4))/2
        else:
            haopen4 = (float(haopen5)+float(haclose5))/2
        if (math.isnan(float(haopen4))):
            haopen3 = (float(haopen3)+float(haclose3))/2
        else:
            haopen3 = (float(haopen4)+float(haclose4))/2
        if (math.isnan(float(haopen3))):
            haopen2 = (float(haopen2)+float(haclose2))/2
        else:
            haopen2 = (float(haopen3)+float(haclose3))/2
        if (math.isnan(float(haopen2))):
            haopen1 = (float(haopen1)+float(haclose1))/2
        else:
            haopen1 = (float(haopen2)+float(haclose2))/2
        if (math.isnan(float(haopen1))):
            haopen = (float(haopen)+float(haclose))/2
        else:
            haopen = (float(haopen1)+float(haclose1))/2


        Down =  (float(haopen) > float(haclose)) and (s == 1)
        #atom_TrendDown = Bearish_Engulfing
        print("Down",Down)
        Up =  (float(haopen) < float(haclose)) and (l == 1)
        #atom_TrendUp =  Bullish_Engulfing
        print("Up",Up)
        result = request_client.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        order_list = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            order_list.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15])
        short_price = float(order_list[1]["entryPrice"])
        short_amount = float(order_list[1]["positionAmt"]*-1)

       
        int_cur_short_price = float(order_list[1]["markPrice"])

       
        int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20

        print(order_list[1]["symbol"]+'  '+str(order_list[1]["positionAmt"])+'  '+str(order_list[1]["entryPrice"])+'  '+str(order_list[1]["markPrice"]))
        time.sleep(1)
        if (((order_list[1]["positionAmt"]*-1) > 0) and ((order_list[1]["positionAmt"]*-1) <= step_one_unit)):


            if ((Down)):
           
                print("take_order_short_full")
                take_order_sell(self)
                #take_order_short = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity= sale_unit)
                #PrintBasic.print_obj(take_order_short)
                time.sleep(1)
 
                return
        if (((order_list[1]["positionAmt"]*-1) > step_one_unit) and ((order_list[1]["positionAmt"]*-1) < step_two_unit) and (abs(int_short_rate * 100) > min_profit_rate_short) and (abs(int_short_rate * 100) < abs(stop_loss_rate_short))):


            if ((Down)):
           
                print("take_order_short_full")
                take_order_sell(self)
                #take_order_short = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity= sale_unit)
                #PrintBasic.print_obj(take_order_short)
                time.sleep(1)
 
                return
        if (((order_list[1]["positionAmt"]*-1) >= step_two_unit) and ((order_list[1]["positionAmt"]*-1) <= step_three_unit) and (abs(int_short_rate * 100) > min_profit_rate_short) and (abs(int_short_rate * 100) < abs(stop_loss_rate_short))):


            if ((Down)):
           
                print("take_order_short_full")
                take_order_sell(self)
                #take_order_short = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity= sale_unit)
                #PrintBasic.print_obj(take_order_short)
                time.sleep(1)
 
                return
     
        return


class CheckProfitLong:

    def __init__(self,market):
        self.market = market


    def check_profit_long_atom(self):
            #price_exit = 0
        global stop_threads
        if stop_threads:
            return
        else:
            pl = []
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result = request_client.get_position()
            #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
            #time.sleep(1)
            object_list = []
            for res in result:
                d = collections.defaultdict()
                d['symbol'] = res.symbol
                d['positionAmt'] = res.positionAmt
                d['entryPrice'] = res.entryPrice
                d['markPrice'] = res.markPrice
                #d['unRealizedProfit'] = res.unRealizedProfit
                object_list.append(d)
                #j = json.dumps(object_list, indent=4)
            #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
           
            #long_price  = 711
            long_price = float(object_list[0]["entryPrice"])
            long_amount = float(object_list[0]["positionAmt"])

           
            int_cur_long_price = float(object_list[0]["markPrice"])

           
            int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20


     
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_long_rate : ",round((int_long_rate*100),4))
            print("Mark Price : ",int_cur_long_price)
            if (((int_long_rate*100) >= min_profit_rate_long) and (long_amount >=  step_three_unit)):
                take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                PrintBasic.print_obj(take_profit_atom)
                time.sleep(1)

                pl = []            
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > step_two_unit) and (long_amount < step_three_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(1)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                    #time.sleep(1)
                    object_list_in = []
                    for res_in in result_in:
                        d = collections.defaultdict()
                        d['symbol'] = res_in.symbol
                        d['positionAmt'] = res_in.positionAmt
                        d['entryPrice'] = res_in.entryPrice
                        d['markPrice'] = res_in.markPrice
                        #d['unRealizedProfit'] = res.unRealizedProfit
                        object_list_in.append(d)
                        #j = json.dumps(object_list, indent=4)
                    dym_cur_long_price = float(object_list_in[0]["markPrice"])
                    long_amount = float(object_list_in[0]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(1)
                    print("pl [-1] in loop",pl)
                    #time.sleep(1)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(1)
                            print("pl in if",pl)
                            #time.sleep(1)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_atom)
                        time.sleep(1)

                        pl = []
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > step_one_unit) and (long_amount <= step_two_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(1)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                    #time.sleep(1)
                    object_list_in = []
                    for res_in in result_in:
                        d = collections.defaultdict()
                        d['symbol'] = res_in.symbol
                        d['positionAmt'] = res_in.positionAmt
                        d['entryPrice'] = res_in.entryPrice
                        d['markPrice'] = res_in.markPrice
                        #d['unRealizedProfit'] = res.unRealizedProfit
                        object_list_in.append(d)
                        #j = json.dumps(object_list, indent=4)
                    dym_cur_long_price = float(object_list_in[0]["markPrice"])
                    long_amount = float(object_list_in[0]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(1)
                    print("pl [-1] in loop",pl)
                    #time.sleep(1)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(1)
                            print("pl in if",pl)
                            #time.sleep(1)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_atom)
                        time.sleep(1)

                        pl = []
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > 0) and (long_amount <= step_one_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(1)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                    #time.sleep(1)
                    object_list_in = []
                    for res_in in result_in:
                        d = collections.defaultdict()
                        d['symbol'] = res_in.symbol
                        d['positionAmt'] = res_in.positionAmt
                        d['entryPrice'] = res_in.entryPrice
                        d['markPrice'] = res_in.markPrice
                        #d['unRealizedProfit'] = res.unRealizedProfit
                        object_list_in.append(d)
                        #j = json.dumps(object_list, indent=4)
                    dym_cur_long_price = float(object_list_in[0]["markPrice"])
                    long_amount = float(object_list_in[0]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(1)
                    print("pl [-1] in loop",pl)
                    #time.sleep(1)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(1)
                            print("pl in if",pl)
                            #time.sleep(1)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_atom)
                        time.sleep(1)

                        pl = []
        return



class CheckProfitShort:

    def __init__(self,market):
        self.market = market


    def check_profit_short_atom(self):
            #price_exit = 0
        global stop_threads
        if stop_threads:
            return
        else:
           
            ps = []
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result = request_client.get_position()
            #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
            #time.sleep(1)
            object_list = []
            for res in result:
                d = collections.defaultdict()
                d['symbol'] = res.symbol
                d['positionAmt'] = res.positionAmt
                d['entryPrice'] = res.entryPrice
                d['markPrice'] = res.markPrice
                #d['unRealizedProfit'] = res.unRealizedProfit
                object_list.append(d)
                #j = json.dumps(object_list, indent=4)
            #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
           
            #long_price  = 711
            short_price = float(object_list[1]["entryPrice"])
            short_amount = float(object_list[1]["positionAmt"]*-1)

           
            int_cur_short_price = float(object_list[1]["markPrice"])

           
            int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


     
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_short_rate : ",round((int_short_rate*100),4))
            print("Mark Price Short: ",int_cur_short_price)
            if (((int_short_rate*100) >= min_profit_rate_short) and (short_amount >= step_three_unit)):
                take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                PrintBasic.print_obj(take_profit_atom)
                time.sleep(1)

                ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > step_two_unit) and  (short_amount < step_three_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(1)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(1)
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                    #time.sleep(1)
                    object_list_in = []
                    for res_in in result_in:
                        d = collections.defaultdict()
                        d['symbol'] = res_in.symbol
                        d['positionAmt'] = res_in.positionAmt
                        d['entryPrice'] = res_in.entryPrice
                        d['markPrice'] = res_in.markPrice
                        #d['unRealizedProfit'] = res.unRealizedProfit
                        object_list_in.append(d)
                        #j = json.dumps(object_list, indent=4)
                    dym_cur_short_price = float(object_list_in[1]["markPrice"])
                    short_amount = float(object_list_in[1]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(1)
                    print("ps [-1] in loop",ps)
                    #time.sleep(1)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(1)_
                            print("ps in if",ps)
                            #time.sleep(1)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_atom)
                        time.sleep(1)

                        ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > step_one_unit) and  (short_amount <= step_two_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(1)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(1)
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                    #time.sleep(1)
                    object_list_in = []
                    for res_in in result_in:
                        d = collections.defaultdict()
                        d['symbol'] = res_in.symbol
                        d['positionAmt'] = res_in.positionAmt
                        d['entryPrice'] = res_in.entryPrice
                        d['markPrice'] = res_in.markPrice
                        #d['unRealizedProfit'] = res.unRealizedProfit
                        object_list_in.append(d)
                        #j = json.dumps(object_list, indent=4)
                    dym_cur_short_price = float(object_list_in[1]["markPrice"])
                    short_amount = float(object_list_in[1]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(1)
                    print("ps [-1] in loop",ps)
                    #time.sleep(1)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(1)_
                            print("ps in if",ps)
                            #time.sleep(1)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_atom)
                        time.sleep(1)

                        ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > 0) and  (short_amount <= step_one_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(1)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(1)
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                    #time.sleep(1)
                    object_list_in = []
                    for res_in in result_in:
                        d = collections.defaultdict()
                        d['symbol'] = res_in.symbol
                        d['positionAmt'] = res_in.positionAmt
                        d['entryPrice'] = res_in.entryPrice
                        d['markPrice'] = res_in.markPrice
                        #d['unRealizedProfit'] = res.unRealizedProfit
                        object_list_in.append(d)
                        #j = json.dumps(object_list, indent=4)
                    dym_cur_short_price = float(object_list_in[1]["markPrice"])
                    short_amount = float(object_list_in[1]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(1)
                    print("ps [-1] in loop",ps)
                    #time.sleep(1)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(1)_
                            print("ps in if",ps)
                            #time.sleep(1)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_atom)
                        time.sleep(1)

                        ps = []

        return

class CheckProfitLongFromOut:

    def __init__(self,market):
        self.market = market


    def check_profit_long_atom(self):
        int_short_rate_out = 0
        in_short_out = False
        in_long_out = False
        in_short_in = False
        in_long_in = False
        short_amount_in = 0
        long_amount_in = 0
        request_client_out = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client_out.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        object_list_out = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list_out.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        short_price_out = float(object_list_out[1]["entryPrice"])
        short_amount_out = float(object_list_out[1]["positionAmt"])*-1
       
        if (short_amount_out > 0):
            in_short_out = True

       
        int_cur_short_price_out = float(object_list_out[1]["markPrice"])

        if (in_short_out):
            if short_amount_out != 0:
                int_short_rate_out = -1*(float(int_cur_short_price_out) - float(short_price_out)) / float(short_price_out) * 20
 
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_short_rate_out : ",round((int_short_rate_out*100),4))
            print("Mark Price : ",int_cur_short_price_out)
            if ((int_short_rate_out *100) >= stop_profit_rate_short):

                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                result_in = request_client_in.get_position()
                #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                #time.sleep(1)
                object_list_in = []
                for res_in in result_in:
                    d = collections.defaultdict()
                    d['symbol'] = res_in.symbol
                    d['positionAmt'] = res_in.positionAmt
                    d['entryPrice'] = res_in.entryPrice
                    d['markPrice'] = res_in.markPrice
                    #d['unRealizedProfit'] = res.unRealizedProfit
                    object_list_in.append(d)

                short_amount_in = float(object_list_in[1]["positionAmt"])*-1
                if ((short_amount_in == 0) and (short_amount_in < short_amount_out)):
                    take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
                    PrintBasic.print_obj(take_profit_atom)
                    time.sleep(1)
##            if ((int_short_rate_out * 100) <= (stop_profit_rate_short * -1)):
##                result = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
##                init_bq = []
##                init_bp = []
##                init_aq = []
##                init_ap = []
##                bid_q = []
##                bid_p = []
##                ask_q = []
##                ask_p = []
##                price_bids = []
##                price_asks = []
##                Down = False
##                Up = False
##                for res in result.bids:
##                    init_bq.append(round(float(res.qty),4))
##                    init_bp.append(round(float(res.price),4))
##                for res in result.asks:
##                    init_aq.append(round(float(res.qty),4))
##                    init_ap.append(round(float(res.price),4))
##                index_init_bq = init_bq.index(max(init_bq))
##                init_price_bid = init_bp[index_init_bq]
##                #print("init_price_bid" ,init_price_bid)
##                index_init_aq = init_aq.index(max(init_aq))
##                init_price_ask = init_ap[index_init_aq]
##                #print("init_price_ask" ,init_price_ask)
##                time.sleep(1)
##                price_bids.append(init_price_bid)
##                price_asks.append(init_price_ask)
##
##                for i in range(20):
##                    result_xtz = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
##                    time.sleep(1)
##                    for resb in result_xtz.bids:
##                        #print(resb.qty)
##                        bid_q.append(round(float(resb.qty),4))
##                        bid_p.append(round(float(resb.price),4))
##
##                       
##                    for resa in result_xtz.asks:
##                        #print(resb.qty)
##                        ask_q.append(round(float(resa.qty),4))
##                        ask_p.append(round(float(resa.price),4))
##
##                    index_bid = bid_q.index(max(bid_q))
##                    index_ask = ask_q.index(max(ask_q))
##                    #print("index ask ",index_ask)
##                    #print("ask price ",ask_p[index_ask])
##                    #print("index bid ",index_bid)
##                    #print("bid price ",bid_p[index_bid])
##
##                    if bid_q[index_bid] != price_bids[-1]:
##                        price_bids.append(bid_p[index_bid])
##                    #print("price_bids in loop ",price_bids)
##                    if ask_q[index_ask] != price_asks[-1]:
##                        price_asks.append(ask_p[index_ask])
##                    #print("price_asks in loop ",price_asks)
##                    #time.sleep(1)
##                #print("price_asks : ",price_asks)
##                #print("price_bids : ",price_bids)
##                #print("price_asks_first ",price_asks[0])
##                #print("price_asks_last ",price_asks[39])
##                #print("price_bids_first ",price_bids[0])
##                #print("price_bids_last ",price_bids[39])
##                s = 0
##                l = 0
##                if (price_asks[0]< price_asks[19]):
##                    s = 0
##                elif (price_asks[0] > price_asks[19]):
##                    s = 1
##                #print(" s ",s)
##
##                if (price_bids[0]< price_bids[19]):
##                    l = 1
##                elif (price_bids[0] > price_bids[19]):
##                    l = 0
##                #old matomod
##                kline2 = request_client.get_candlestick_data(symbol="ATOMUSDT", interval=interval,startTime=None, endTime=None, limit=20)
##                #print("======= Kline/Candlestick Data =======")
##                #PrintMix.print_data(result[0].volume)
##                #print("======================================")
##                open_list = []
##                for res in kline2:
##                    d = collections.defaultdict()
##                    d['open'] = res.open
##                    d['high'] = res.high
##                    d['low'] = res.low
##                    d['close'] = res.close
##                    #d['unRealizedProfit'] = res.unRealizedProfit
##                    open_list.append(d)
##
##                open0 = open_list[6]["open"]
##                high0 = open_list[6]["high"]
##                low0 = open_list[6]["low"]
##                close0 = open_list[6]["close"]
##                open1 = open_list[5]["open"]
##                high1 = open_list[5]["high"]
##                low1 = open_list[5]["low"]
##                close1 = open_list[5]["close"]
##                open2 = open_list[4]["open"]
##                high2 = open_list[4]["high"]
##                low2 = open_list[4]["low"]
##                close2 = open_list[4]["close"]
##                open3 = open_list[3]["open"]
##                high3 = open_list[3]["high"]
##                low3 = open_list[3]["low"]
##                close3 = open_list[3]["close"]
##                open4 = open_list[2]["open"]
##                high4 = open_list[2]["high"]
##                low4 = open_list[2]["low"]
##                close4 = open_list[2]["close"]
##                open5 = open_list[1]["open"]
##                high5 = open_list[1]["high"]
##                low5 = open_list[1]["low"]
##                close5 = open_list[1]["close"]
##                open6 = open_list[0]["open"]
##                high6 = open_list[0]["high"]
##                low6 = open_list[0]["low"]
##                close6 = open_list[0]["close"]
##                haclose = (float(open0)+float(high0)+float(low0)+float(close0))/4
##                haclose1 = (float(open1)+float(high1)+float(low1)+float(close1))/4
##                haclose2 = (float(open2)+float(high2)+float(low2)+float(close2))/4
##                haclose3 = (float(open3)+float(high3)+float(low3)+float(close3))/4
##                haclose4 = (float(open4)+float(high4)+float(low4)+float(close4))/4
##                haclose5 = (float(open5)+float(high5)+float(low5)+float(close5))/4
##                haclose6 = (float(open6)+float(high6)+float(low6)+float(close6))/4
##                haopen6 = (float(open6)+float(close6))/2
##                if (math.isnan(float(haopen6))):
##                    haopen5 = (float(haopen5)+float(haclose5))/2
##                else:
##                    haopen5 = (float(haopen6)+float(haclose6))/2
##                if (math.isnan(float(haopen5))):
##                    haopen4 = (float(haopen4)+float(haclose4))/2
##                else:
##                    haopen4 = (float(haopen5)+float(haclose5))/2
##                if (math.isnan(float(haopen4))):
##                    haopen3 = (float(haopen3)+float(haclose3))/2
##                else:
##                    haopen3 = (float(haopen4)+float(haclose4))/2
##                if (math.isnan(float(haopen3))):
##                    haopen2 = (float(haopen2)+float(haclose2))/2
##                else:
##                    haopen2 = (float(haopen3)+float(haclose3))/2
##                if (math.isnan(float(haopen2))):
##                    haopen1 = (float(haopen1)+float(haclose1))/2
##                else:
##                    haopen1 = (float(haopen2)+float(haclose2))/2
##                if (math.isnan(float(haopen1))):
##                    haopen = (float(haopen)+float(haclose))/2
##                else:
##                    haopen = (float(haopen1)+float(haclose1))/2
##
##
##                Down =  (float(haopen) > float(haclose)) and (s == 1)
##                #atom_TrendDown = Bearish_Engulfing
##                print("Down",Down)
##                Up =  (float(haopen) < float(haclose)) and (l == 1)
##                #atom_TrendUp =  Bullish_Engulfing
##                print("Up",Up)
##                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
##                result_in = request_client_in.get_position()
##                #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
##                #time.sleep(1)
##                object_list_in = []
##                for res_in in result_in:
##                    d = collections.defaultdict()
##                    d['symbol'] = res_in.symbol
##                    d['positionAmt'] = res_in.positionAmt
##                    d['entryPrice'] = res_in.entryPrice
##                    d['markPrice'] = res_in.markPrice
##                    #d['unRealizedProfit'] = res.unRealizedProfit
##                    object_list_in.append(d)
##
##                #short_amount_in = float(object_list_in[1]["positionAmt"]*-1)
##                long_amount_in = float(object_list_in[0]["positionAmt"])
##                if (long_amount_in > 0):
##
##                    in_long_in = True
##
##                if ((Up) and (long_amount_in == 0) and (long_amount_in < short_amount_out)):
##                    take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit*2)
##                    PrintBasic.print_obj(take_profit_atom)
##                    time.sleep(1)
##
##                if (in_long_in):
##                    if ((Up) and (long_amount_in < step_three_unit) and (long_amount_in < short_amount_out) and (short_amount_out < step_three_unit)):
##                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
##                        PrintBasic.print_obj(take_profit_atom)
##                        time.sleep(1)
##                        return
##                    if ((Up) and (long_amount_in < step_three_unit) and (long_amount_in < short_amount_out) and (short_amount_out >= step_three_unit)):
##                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
##                        PrintBasic.print_obj(take_profit_atom)
##                        time.sleep(1)
##                        return

        return



class CheckProfitShortFromOut:

    def __init__(self,market):
        self.market = market


    def check_profit_short_atom(self):
        int_long_rate_out = 0
        in_short_out = False
        in_long_out = False
        in_short_in = False
        in_long_in = False
        short_amount_in = 0
        long_amount_in = 0
        request_client_out = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client_out.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        object_list_out = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list_out.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        long_price_out = float(object_list_out[0]["entryPrice"])
        long_amount_out = float(object_list_out[0]["positionAmt"])
       
        if (long_amount_out > 0):

            in_long_out = True

       
        int_cur_long_price_out = float(object_list_out[0]["markPrice"])

        if (in_long_out):
            if long_amount_out != 0:
                int_long_rate_out = (float(int_cur_long_price_out) - float(long_price_out)) / float(long_price_out) * 20
 
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_long_rate_out : ",round((int_long_rate_out*100),4))
            print("Mark Price : ",int_cur_long_price_out)
            if ((int_long_rate_out *100) >= stop_profit_rate_long):

                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                result_in = request_client_in.get_position()
                #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                #time.sleep(1)
                object_list_in = []
                for res_in in result_in:
                    d = collections.defaultdict()
                    d['symbol'] = res_in.symbol
                    d['positionAmt'] = res_in.positionAmt
                    d['entryPrice'] = res_in.entryPrice
                    d['markPrice'] = res_in.markPrice
                    #d['unRealizedProfit'] = res.unRealizedProfit
                    object_list_in.append(d)

                long_amount_in = float(object_list_in[0]["positionAmt"])
                if ((long_amount_in == 0) and (long_amount_in < long_amount_out)):
                    take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                    PrintBasic.print_obj(take_profit_atom)
                    time.sleep(1)
##            if ((int_long_rate_out * 100) <= (stop_profit_rate_long * -1)):
##                result = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
##                init_bq = []
##                init_bp = []
##                init_aq = []
##                init_ap = []
##                bid_q = []
##                bid_p = []
##                ask_q = []
##                ask_p = []
##                price_bids = []
##                price_asks = []
##                Down = False
##                Up = False
##                for res in result.bids:
##                    init_bq.append(round(float(res.qty),4))
##                    init_bp.append(round(float(res.price),4))
##                for res in result.asks:
##                    init_aq.append(round(float(res.qty),4))
##                    init_ap.append(round(float(res.price),4))
##                index_init_bq = init_bq.index(max(init_bq))
##                init_price_bid = init_bp[index_init_bq]
##                #print("init_price_bid" ,init_price_bid)
##                index_init_aq = init_aq.index(max(init_aq))
##                init_price_ask = init_ap[index_init_aq]
##                #print("init_price_ask" ,init_price_ask)
##                time.sleep(1)
##                price_bids.append(init_price_bid)
##                price_asks.append(init_price_ask)
##
##                for i in range(20):
##                    result_xtz = request_client.get_order_book(symbol = "ATOMUSDT", limit = 20)
##                    time.sleep(1)
##                    for resb in result_xtz.bids:
##                        #print(resb.qty)
##                        bid_q.append(round(float(resb.qty),4))
##                        bid_p.append(round(float(resb.price),4))
##
##                       
##                    for resa in result_xtz.asks:
##                        #print(resb.qty)
##                        ask_q.append(round(float(resa.qty),4))
##                        ask_p.append(round(float(resa.price),4))
##
##                    index_bid = bid_q.index(max(bid_q))
##                    index_ask = ask_q.index(max(ask_q))
##                    #print("index ask ",index_ask)
##                    #print("ask price ",ask_p[index_ask])
##                    #print("index bid ",index_bid)
##                    #print("bid price ",bid_p[index_bid])
##
##                    if bid_q[index_bid] != price_bids[-1]:
##                        price_bids.append(bid_p[index_bid])
##                    #print("price_bids in loop ",price_bids)
##                    if ask_q[index_ask] != price_asks[-1]:
##                        price_asks.append(ask_p[index_ask])
##                    #print("price_asks in loop ",price_asks)
##                    #time.sleep(1)
##                #print("price_asks : ",price_asks)
##                #print("price_bids : ",price_bids)
##                #print("price_asks_first ",price_asks[0])
##                #print("price_asks_last ",price_asks[39])
##                #print("price_bids_first ",price_bids[0])
##                #print("price_bids_last ",price_bids[39])
##                s = 0
##                l = 0
##                if (price_asks[0]< price_asks[19]):
##                    s = 0
##                elif (price_asks[0] > price_asks[19]):
##                    s = 1
##                #print(" s ",s)
##
##                if (price_bids[0]< price_bids[19]):
##                    l = 1
##                elif (price_bids[0] > price_bids[19]):
##                    l = 0
##                #old matomod
##                kline2 = request_client.get_candlestick_data(symbol="ATOMUSDT", interval=interval,startTime=None, endTime=None, limit=20)
##                #print("======= Kline/Candlestick Data =======")
##                #PrintMix.print_data(result[0].volume)
##                #print("======================================")
##                open_list = []
##                for res in kline2:
##                    d = collections.defaultdict()
##                    d['open'] = res.open
##                    d['high'] = res.high
##                    d['low'] = res.low
##                    d['close'] = res.close
##                    #d['unRealizedProfit'] = res.unRealizedProfit
##                    open_list.append(d)
##
##                open0 = open_list[6]["open"]
##                high0 = open_list[6]["high"]
##                low0 = open_list[6]["low"]
##                close0 = open_list[6]["close"]
##                open1 = open_list[5]["open"]
##                high1 = open_list[5]["high"]
##                low1 = open_list[5]["low"]
##                close1 = open_list[5]["close"]
##                open2 = open_list[4]["open"]
##                high2 = open_list[4]["high"]
##                low2 = open_list[4]["low"]
##                close2 = open_list[4]["close"]
##                open3 = open_list[3]["open"]
##                high3 = open_list[3]["high"]
##                low3 = open_list[3]["low"]
##                close3 = open_list[3]["close"]
##                open4 = open_list[2]["open"]
##                high4 = open_list[2]["high"]
##                low4 = open_list[2]["low"]
##                close4 = open_list[2]["close"]
##                open5 = open_list[1]["open"]
##                high5 = open_list[1]["high"]
##                low5 = open_list[1]["low"]
##                close5 = open_list[1]["close"]
##                open6 = open_list[0]["open"]
##                high6 = open_list[0]["high"]
##                low6 = open_list[0]["low"]
##                close6 = open_list[0]["close"]
##                haclose = (float(open0)+float(high0)+float(low0)+float(close0))/4
##                haclose1 = (float(open1)+float(high1)+float(low1)+float(close1))/4
##                haclose2 = (float(open2)+float(high2)+float(low2)+float(close2))/4
##                haclose3 = (float(open3)+float(high3)+float(low3)+float(close3))/4
##                haclose4 = (float(open4)+float(high4)+float(low4)+float(close4))/4
##                haclose5 = (float(open5)+float(high5)+float(low5)+float(close5))/4
##                haclose6 = (float(open6)+float(high6)+float(low6)+float(close6))/4
##                haopen6 = (float(open6)+float(close6))/2
##                if (math.isnan(float(haopen6))):
##                    haopen5 = (float(haopen5)+float(haclose5))/2
##                else:
##                    haopen5 = (float(haopen6)+float(haclose6))/2
##                if (math.isnan(float(haopen5))):
##                    haopen4 = (float(haopen4)+float(haclose4))/2
##                else:
##                    haopen4 = (float(haopen5)+float(haclose5))/2
##                if (math.isnan(float(haopen4))):
##                    haopen3 = (float(haopen3)+float(haclose3))/2
##                else:
##                    haopen3 = (float(haopen4)+float(haclose4))/2
##                if (math.isnan(float(haopen3))):
##                    haopen2 = (float(haopen2)+float(haclose2))/2
##                else:
##                    haopen2 = (float(haopen3)+float(haclose3))/2
##                if (math.isnan(float(haopen2))):
##                    haopen1 = (float(haopen1)+float(haclose1))/2
##                else:
##                    haopen1 = (float(haopen2)+float(haclose2))/2
##                if (math.isnan(float(haopen1))):
##                    haopen = (float(haopen)+float(haclose))/2
##                else:
##                    haopen = (float(haopen1)+float(haclose1))/2
##
##
##                Down =  (float(haopen) > float(haclose)) and (s == 1)
##                #atom_TrendDown = Bearish_Engulfing
##                print("Down",Down)
##                Up =  (float(haopen) < float(haclose)) and (l == 1)
##                #atom_TrendUp =  Bullish_Engulfing
##                print("Up",Up)
##                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
##                result_in = request_client_in.get_position()
##                #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
##                #time.sleep(1)
##                object_list_in = []
##                for res_in in result_in:
##                    d = collections.defaultdict()
##                    d['symbol'] = res_in.symbol
##                    d['positionAmt'] = res_in.positionAmt
##                    d['entryPrice'] = res_in.entryPrice
##                    d['markPrice'] = res_in.markPrice
##                    #d['unRealizedProfit'] = res.unRealizedProfit
##                    object_list_in.append(d)
##
##                short_amount_in = float(object_list_in[1]["positionAmt"])*-1
##                long_amount_in = float(object_list_in[0]["positionAmt"])
##                if (short_amount_in > 0):
##                    in_short_in = True
##
##                if ((Down)  and (short_amount_in == 0) and (short_amount_in < long_amount_out)):
##                    take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,  quantity=sale_unit*2)
##                    PrintBasic.print_obj(take_profit_atom)
##                    time.sleep(1)
##
##                if (in_short_in):
##                    if ((Down)  and (short_amount_in < step_three_unit) and (short_amount_in < long_amount_out) and (long_amount_out < step_three_unit)):
##                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
##                        PrintBasic.print_obj(take_profit_atom)
##                        time.sleep(1)
##                        return
##                    if ((Down) and (short_amount_in < step_three_unit) and (short_amount_in < long_amount_out) and (long_amount_out >= step_three_unit)):
##                        take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
##                        PrintBasic.print_obj(take_profit_atom)
##                        time.sleep(1)
##                        return
        return

class CheckLossLong:

    def __init__(self,market):
        self.market = market


    def check_loss_long_atom(self):
            #price_exit = 0

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        object_list = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        long_price = float(object_list[0]["entryPrice"])
        long_amount = float(object_list[0]["positionAmt"])

       
        int_cur_long_price = float(object_list[0]["markPrice"])

       
        int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_long_rate : ",(int_long_rate*100))
        #time.sleep(1)
        print("Mark Price : ",int_cur_long_price)
        if (((int_long_rate*100) <= stop_loss_rate_long) ):

            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)



        return



class CheckLossShort:

    def __init__(self,market):
        self.market = market


    def check_loss_short_atom(self):

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        object_list = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        short_price = float(object_list[1]["entryPrice"])
        short_amount = float(object_list[1]["positionAmt"]*-1)

       
        int_cur_short_price = float(object_list[1]["markPrice"])

       
        int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_short_rate : ",(int_short_rate*100))
        #time.sleep(1)
        print("Mark Price Short: ",int_cur_short_price)
        if (((int_short_rate*100) <= stop_loss_rate_short) ):

            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)



        return

class CheckProfitLongMore:

    def __init__(self,market):
        self.market = market


    def check_profit_long_atom(self):
            #price_exit = 0
        #pl = []
        global stop_threads
        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        object_list = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        long_price = float(object_list[0]["entryPrice"])
        long_amount = float(object_list[0]["positionAmt"])

       
        int_cur_long_price = float(object_list[0]["markPrice"])

       
        int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_long_rate : ",round((int_long_rate*100),4))
        print("Mark Price : ",int_cur_long_price)
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount >=  step_three_unit) and (long_amount < step_four_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit/2)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #pl = []            
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount > step_two_unit) and (long_amount < step_three_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit/2)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #pl = []  
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount > step_one_unit) and (long_amount <= step_two_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit/4)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #pl = []  
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount > 0) and (long_amount <= step_one_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit/4)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #pl = []  
        return



class CheckProfitShortMore:

    def __init__(self,market):
        self.market = market


    def check_profit_short_atom(self):
            #price_exit = 0
        #ps = []
        global stop_threads
        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()

        object_list = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        short_price = float(object_list[1]["entryPrice"])
        short_amount = float(object_list[1]["positionAmt"]*-1)

       
        int_cur_short_price = float(object_list[1]["markPrice"])

       
        int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_short_rate : ",round((int_short_rate*100),4))
        print("Mark Price Short: ",int_cur_short_price)
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount >= step_three_unit) and (short_amount < step_four_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit/2)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount > step_two_unit) and  (short_amount < step_three_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit/2)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount > step_one_unit) and  (short_amount <= step_two_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit/4)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount > 0) and  (short_amount <= step_one_unit))):
            take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit/4)
            PrintBasic.print_obj(take_profit_atom)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\atom_m2End.bat'])

            #ps = []

        return


class CheckLossLongFromIn:

    def __init__(self,market):
        self.market = market


    def check_profit_long_atom(self):
        global reentry_unit
        int_long_rate_in = 0
        in_short_out = False
        in_long_out = False
        in_short_in = False
        in_long_in = False
        short_amount_in = 0
        long_amount_in = 0
        request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client_out.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        object_list_in = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list_in.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        long_price_in = float(object_list_in[0]["entryPrice"])
        long_amount_in = float(object_list_in[0]["positionAmt"])
       
        if (long_amount_in > 0):
            in_long_in = True

       
        int_cur_long_price_in = float(object_list_in[0]["markPrice"])

        if (in_long_in):
            if long_amount_in != 0:
                int_long_rate_in = (float(int_cur_long_price_in) - float(long_price_in)) / float(long_price_in) * 20
 
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_long_rate_in : ",round((int_long_rate_in*100),4))
            print("Mark Price : ",int_cur_long_price_in)
            if ((int_long_rate_in *100) <= -1):

                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                result_in = request_client_in.get_position()
                #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                #time.sleep(1)
                object_list_in = []
                for res_in in result_in:
                    d = collections.defaultdict()
                    d['symbol'] = res_in.symbol
                    d['positionAmt'] = res_in.positionAmt
                    d['entryPrice'] = res_in.entryPrice
                    d['markPrice'] = res_in.markPrice
                    #d['unRealizedProfit'] = res.unRealizedProfit
                    object_list_in.append(d)

                short_amount_in = float(object_list_in[1]["positionAmt"])*-1
                if ((short_amount_in == 0) and (short_amount_in < long_amount_in)):
                    if(reentry_unit >= long_amount_in):
                        reentry_unit = long_amount_in//2
                    take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=reentry_unit)
                    PrintBasic.print_obj(take_profit_atom)
                    time.sleep(1)


        return



class CheckLossShortFromIn:

    def __init__(self,market):
        self.market = market


    def check_profit_short_atom(self):
        global reentry_unit
        int_short_rate_in = 0
        in_short_out = False
        in_long_out = False
        in_short_in = False
        in_long_in = False
        short_amount_in = 0
        long_amount_in = 0
        request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client_in.get_position()
        #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
        #time.sleep(1)
        object_list_in = []
        for res in result:
            d = collections.defaultdict()
            d['symbol'] = res.symbol
            d['positionAmt'] = res.positionAmt
            d['entryPrice'] = res.entryPrice
            d['markPrice'] = res.markPrice
            #d['unRealizedProfit'] = res.unRealizedProfit
            object_list_in.append(d)
            #j = json.dumps(object_list, indent=4)
        #print(object_list[15]["symbol"]+'  '+str(object_list[15]["positionAmt"])+'  '+str(object_list[15]["entryPrice"])+'  '+str(object_list[15]["markPrice"]))
       
        #long_price  = 711
        short_price_in = float(object_list_in[1]["entryPrice"])
        short_amount_in = float(object_list_in[1]["positionAmt"]*-1)
       
        if (short_amount_in > 0):

            in_short_in = True

       
        int_cur_short_price_in = float(object_list_out[1]["markPrice"])

        if (in_short_in):
            if short_amount_in != 0:
                int_short_rate_in = -1*(float(int_cur_short_price_in) - float(short_price_in)) / float(short_price_in) * 20
 
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_short_rate_in : ",round((int_short_rate_in*100),4))
            print("Mark Price : ",int_cur_short_price_in)
            if ((int_short_rate_in *100) <= -1):

                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                result_in = request_client_in.get_position()
                #atom_account_trade_in = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
                #time.sleep(1)
                object_list_in = []
                for res_in in result_in:
                    d = collections.defaultdict()
                    d['symbol'] = res_in.symbol
                    d['positionAmt'] = res_in.positionAmt
                    d['entryPrice'] = res_in.entryPrice
                    d['markPrice'] = res_in.markPrice
                    #d['unRealizedProfit'] = res.unRealizedProfit
                    object_list_in.append(d)

                long_amount_in = float(object_list_in[0]["positionAmt"])
                if ((long_amount_in == 0) and (long_amount_in < short_amount_in)):
                    if(reentry_unit >= short_amount_in):
                        reentry_unit = short_amount_in//2 
                    take_profit_atom = request_client_in.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=reentry_unit)

                    PrintBasic.print_obj(take_profit_atom)
                    time.sleep(1)

        return



class getmail:

    def __init__(self,market):
        self.market = market
   


    def two_way_email(self,server,uname,pwd):
        username = uname
        password = pwd
        mail = imaplib.IMAP4_SSL(server)
        mail.login(username, password)
        mail.select("inbox")
        try:
            result, data = mail.uid('search', None, '(UNSEEN)')
            inbox_item_list = data[0].split()
            most_recent = inbox_item_list[-1]
            result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')
            raw_email = email_data[0][1].decode("UTF-8")
            email_message = email.message_from_string(raw_email)

            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                att_path = os.path.join(detach_dir, filename)

                if not os.path.isfile(att_path):
                    fp = open(att_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                    #print('Downloaded file:', filename)
            if email_message.is_multipart():
                for payload in email_message.get_payload():
                # print('To:\t\t', email_message['To'])
                    #print('From:\t',     email_message['From'])
                    print('Subject:', email_message['Subject'])
                    s1 = email_message['Subject']
                    #rs1 = s1.find('atom3MSH')
                    #rl1 = s1.find('atom3MLO')

                    # How to use find()
                    if (s1.find('BUY ATOM') != -1):
                        print ("Contains BUY substring ")
                        take_order_buy(self)
                        take_order_sell(self)
                        update_guided("l")
                        time.sleep(1)



                    elif (s1.find('SELL ATOM') != -1):
                        print ("Contains SELL substring ")
                        take_order_sell(self)
                        take_order_buy(self)
                        update_guided("s")
                        time.sleep(1)
                    else:
                        print ("Doesn't contains given substring")
                        time.sleep(1)

                    break
            else:
                #print('To:\t\t', email_message['To'])
                #print('From:\t', email_message['From'])
                print('Subject:', email_message['Subject'])
                s1 = email_message['Subject']
                    #rs1 = s1.find('atom3MSH')
                    #rl1 = s1.find('atom3MLO')

                    # How to use find()
                if (s1.find('BUY ATOM') != -1):
                    print ("Contains BUY  substring ")
                    take_order_buy(self)
                    take_order_sell(self)
                    update_guided("l")
                    time.sleep(1)


                elif (s1.find('SELL ATOM') != -1):
                    print ("Contains SELL substring ")
                    take_order_sell(self)
                    take_order_buy(self)
                    update_guided("s")
                    time.sleep(1)
   
                else:
                    print ("Doesn't contains given substring")
                    #take_order_buy()
                    time.sleep(1)


        except IndexError:
            print("No new email")
        return
           
   
def take_order_sell(self):
        #price_exit = 0
    #pl = []
    #global stop_threads
    inc_count_s(1)
    cls_count_l(0)
    short_amount_in = 0
    short_amount_out = 0
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_position()
    #atom_account_trade = request_client.get_account_trades(symbol="ATOMUSDT",limit= 1)
    #time.sleep(1)

    time.sleep(1)
    object_list = []
    for res in result:
        d = collections.defaultdict()
        d['symbol'] = res.symbol
        d['positionAmt'] = res.positionAmt
        d['entryPrice'] = res.entryPrice
        d['markPrice'] = res.markPrice
        #d['unRealizedProfit'] = res.unRealizedProfit
        object_list.append(d)
    long_amount_in = float(object_list[0]["positionAmt"])
    short_amount_in = float(object_list[1]["positionAmt"]*-1)
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    collection_core = db["base"]

    core_data = collection_core.find_one({"market": 'ATOM'})
    #print(core_data)
    atom_active_plan = core_data["ap"]
    #print(atom_active_plan)
    if (atom_active_plan == 'A'):
        atom_data = collection_atom.find_one({"market": 'ATOM_A'})
    if (atom_active_plan == 'B'):
        atom_data = collection_atom.find_one({"market": 'ATOM_B'})
    if (atom_active_plan == 'C'):
        atom_data = collection_atom.find_one({"market": 'ATOM_C'})     

    sale_unit = atom_data["sale"]

    step_two_unit = atom_data["step_two_unit"]


    
    count_s = atom_data["count_s"]
    
    limit_s = atom_data["limit_s"]


    if ((short_amount_in < step_two_unit) and (count_s > limit_s)):
        take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
        PrintBasic.print_obj(take_profit_atom)
        time.sleep(1)



    return
def take_order_buy(self):
        #price_exit = 0
    #pl = []
    #global stop_threads
    inc_count_l(1)
    cls_count_s(0)
    long_amount_in = 0
    long_amount_out = 0
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
        #d['unRealizedProfit'] = res.unRealizedProfit
        object_list.append(d)

    long_amount_in = float(object_list[0]["positionAmt"])
    short_amount_in = float(object_list[1]["positionAmt"]*-1)

    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    collection_core = db["base"]

    core_data = collection_core.find_one({"market": 'ATOM'})
    #print(core_data)
    atom_active_plan = core_data["ap"]
    #print(atom_active_plan)
    if (atom_active_plan == 'A'):
        atom_data = collection_atom.find_one({"market": 'ATOM_A'})
    if (atom_active_plan == 'B'):
        atom_data = collection_atom.find_one({"market": 'ATOM_B'})
    if (atom_active_plan == 'C'):
        atom_data = collection_atom.find_one({"market": 'ATOM_C'})     

    buy_unit = atom_data["buy"]

    step_two_unit = atom_data["step_two_unit"]


    count_l = atom_data["count_l"]
    
    limit_l = atom_data["limit_l"]


    if ((long_amount_in < step_two_unit) and (count_l > limit_l)):
        take_profit_atom = request_client.post_order(symbol="ATOMUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
        time.sleep(1)

    return


def inc_count_s(count):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    count_ss = count_s + count
    collection_atom.update_one({"market": 'ATOM_A'},{"$set":{"count_s":count_ss} })
    collection_atom.update_one({"market": 'ATOM_B'},{"$set":{"count_s":count_ss} })
    collection_atom.update_one({"market": 'ATOM_C'},{"$set":{"count_s":count_ss} })
    return

def cls_count_s(count):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    collection_atom.update_one({"market": 'ATOM_A'},{"$set":{"count_s":count} })
    collection_atom.update_one({"market": 'ATOM_B'},{"$set":{"count_s":count} })
    collection_atom.update_one({"market": 'ATOM_C'},{"$set":{"count_s":count} })
    return
def get_count_l(self):
    #cio_id = 'a8969001117907911480'
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    collection_core = db["base"]

    core_data = collection_core.find_one({"market": 'ATOM'})
    #print(core_data)
    atom_active_plan = core_data["ap"]
    #print(atom_active_plan)
    if (atom_active_plan == 'A'):
        atom_data = collection_atom.find_one({"market": 'ATOM_A'})
    if (atom_active_plan == 'B'):
        atom_data = collection_atom.find_one({"market": 'ATOM_B'})
    if (atom_active_plan == 'C'):
        atom_data = collection_atom.find_one({"market": 'ATOM_C'})
    return atom_data["count_l"]

def inc_count_l(count):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    count_ll = count_l + count
    collection_atom.update_one({"market": 'ATOM_A'},{"$set":{"count_l":count_ll} })
    collection_atom.update_one({"market": 'ATOM_B'},{"$set":{"count_l":count_ll} })
    collection_atom.update_one({"market": 'ATOM_C'},{"$set":{"count_l":count_ll} })
    return

def cls_count_l(count):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    collection_atom.update_one({"market": 'ATOM_A'},{"$set":{"count_l":count} })
    collection_atom.update_one({"market": 'ATOM_B'},{"$set":{"count_l":count} })
    collection_atom.update_one({"market": 'ATOM_C'},{"$set":{"count_l":count} })
    return
def get_count_s(self):
    #cio_id = 'a8969001117907911480'
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["atom"]
    collection_core = db["base"]

    core_data = collection_core.find_one({"market": 'ATOM'})
    #print(core_data)
    atom_active_plan = core_data["ap"]
    #print(atom_active_plan)
    if (atom_active_plan == 'A'):
        atom_data = collection_atom.find_one({"market": 'ATOM_A'})
    if (atom_active_plan == 'B'):
        atom_data = collection_atom.find_one({"market": 'ATOM_B'})
    if (atom_active_plan == 'C'):
        atom_data = collection_atom.find_one({"market": 'ATOM_C'})
    return atom_data["count_s"]

def insert_test(x):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_atom = db["test_mon_s"]
    #count_ss = count_s + count
    collection_atom.insert_one(x)

    return
def insert_open_order(x):
    #cio_id = 'a8969001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_open = db["open_mon_s"]
    #count_ss = count_s + count
    collection_open.insert_one(x)

    return
       
if __name__ == '__main__':
    g_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    g_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    o_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    o_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP' 
    psl = []

    stop_threads = False
    conts = 0
    try:
        while True:
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result_open_order = request_client.get_open_orders()
            time.sleep(1)
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
                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ETHUSDT") and (keys.get('type')=="LIMIT") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
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
                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ETHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
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
                if (key.get('positionSide') =='SHORT' and key.get('symbol') =='ETHUSDT' and key.get('positionAmt') < 0.0):
                    syms = key.get('symbol')
                    mPrices = key.get('markPrice')
                    priceIns = key.get('entryPrice')
                    positionAmtShort = key.get('positionAmt')
                    print(mPrices,'',priceIns,'',syms,'',positionAmtShort)
                    #d = Decimal(str(mPrices))

                    #pres = (d.as_tuple().exponent)*-1
                    ass = str(round(float(positionAmtShort)*-1,2))
                    time.sleep(1)
                        
                    try:
                        psl=[]

                        ps = str(round(float(priceIns) -((ps* float(priceIns))/20),2))

                        psf = str(round(float(priceIns) -((psf* float(priceIns))/20),2))
                        psff = str(round(float(priceIns) -((psff* float(priceIns))/20),2))
                        psfff = str(round(float(priceIns) -((psfff* float(priceIns))/20),2))
                        psffff = str(round(float(priceIns) -((psffff* float(priceIns))/20),2))
                        psloss = str(round(float(priceIns) +((pslost*float(priceIns))/20),2))
                        pslostf = str(round(float(priceIns) +((pslostf*float(priceIns))/20),2))
                        pslostl = str(round(float(priceIns) +((pslostl*float(priceIns))/20),2))
                        try:
                            cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT,stopPrice=pslostl,  ordertype=OrderType.STOP_MARKET, closePosition='True')
                        except IndexError as error:
                            print("Exiting: with error in try" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error in try" +  "\n")      

                        if (mPrices >= Decimal(pslostl) ):
                            try:
                            #cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=mPrices, quantity=ass//2,timeInForce='GTC')
                                cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET, quantity= str(float(ass)))
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
                                    ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=psf, quantity=str(round(rest,2)),timeInForce='GTC')
                                    #time.sleep(1)
                                    conts = 0
                            except IndexError as error:
                                print("Exiting: with error in try" + "\n")
                            except Exception as exception:
                                print("Exiting: Exception error in try" +  "\n")  
                        #if (mPrices >= Decimal(pslostl)):
                        #if (mPrices >= Decimal(pslostl)):
                            #cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=mPrices, quantity=ass//2,timeInForce='GTC')
                            #cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET, quantity= str(round(float(ass),2)))
                        #cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT,stopPrice=pslostf,  ordertype=OrderType.STOP_MARKET, closePosition='True')
                        
                        # if (mPrices >= Decimal(pslostf)):
                        #     request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                        #     result_open_order = request_client.get_open_orders()
                        #     time.sleep(1)
                        #     object_list_open = []
                        #     #t = 0
                        #     for reso in result_open_order:
                        #         c = collections.defaultdict()
                        #         #c['index'] = t
                        #         c['symbol'] = reso.symbol
                        #         c['orderId'] = reso.orderId
                        #         c['origQty'] = reso.origQty
                        #         c['side'] = reso.side
                        #         c['positionSide'] = reso.positionSide
                        #         c['status'] = reso.status
                        #         c['type'] = reso.type
                        #         #d['unRealizedProfit'] = res.unRealizedProfit
                        #         #t = t+1
                        #         object_list_open.append(c)

                                
                        #     for keys in object_list_open:
                        #         #cont = 0
                        #         if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ETHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                        #             markets = keys.get('symbol')
                        #             orderIds = keys.get('orderId')
                                    
                        #             print("market",markets)
                        #             print("orderId",orderIds)

                        #             #time.sleep(1)
                        #             result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)  
                        #     result_l = request_client.get_position()

                        #     #time.sleep(1)
                        #     object_list = []
                        #     #i = 0
                        #     for res in result_l:
                        #             d = collections.defaultdict()
                        #             #d['index'] = i
                        #             d['symbol'] = res.symbol
                        #             d['positionAmt'] = res.positionAmt
                        #             d['entryPrice'] = res.entryPrice
                        #             d['markPrice'] = res.markPrice
                        #             d['positionSide'] = res.positionSide
                        #             #d['unRealizedProfit'] = res.unRealizedProfit
                        #         # i = i+1
                        #             object_list.append(d)
                        #     for key in object_list:

                        #         if (key.get('positionSide') =='LONG' and key.get('positionAmt') >=0.0 and key.get('symbol') == syms):
                        #             sym = key.get('symbol')
                        #             mPrice = key.get('markPrice')
                        #             priceIn = key.get('entryPrice')
                        #             positionAmtLong = key.get('positionAmt')
                        #             #print(market,'',markPrice,'',entryPriceLong,'',positionAmtLong)
                        #             al = str(float(positionAmtLong))
                        #             if (mPrices >= Decimal(pslostf) and float(ass) > float(al)):
                        #                 re_unit = ((float(ass))-float(al))
                        #                 if (re_unit > 0):
                        #                 #cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=mPrices, quantity=ass//2,timeInForce='GTC')
                        #                     cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET, quantity= str(float(re_unit))) 
                        if (mPrices <= Decimal(psff) and mPrices > Decimal(psfff) ):
                            # ps = []
                            add_int_short_price =  round(float(priceIns)+ ((float(mPrices) - float(priceIns))/(float(priceIns)*100)*first_p),2)
                            #print("in if")
                            #time.sleep(1)
                            add_short_price = 0
                            psl.append(add_int_short_price)
                            print("ps [-1]",psl[-1])
                            #time.sleep(1)
                            stop_threads = False
                            while ((stop_threads == False ) and mPrices > Decimal(psfff)):
                            #while True:
                                request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                                result_in = request_client.get_position()
                                #sxp_account_trade_in = request_client.get_account_trades(symbol="SXPUSDT",limit= 1)
                                time.sleep(1)
                                object_list_in = []
                                for res_in in result_in:
                                    d = collections.defaultdict()
                                    d['symbol'] = res_in.symbol
                                    d['positionAmt'] = res_in.positionAmt
                                    d['entryPrice'] = res_in.entryPrice
                                    d['markPrice'] = res_in.markPrice
                                    d['positionSide'] = res_in.positionSide
                                    #d['unRealizedProfit'] = res.unRealizedProfit
                                    object_list_in.append(d)
                                    #j = json.dumps(object_list, indent=4)
                                for keyi in object_list_in:
                                    if (keyi.get('positionSide') =='SHORT' and keyi.get('symbol') =='ETHUSDT' and keyi.get('positionAmt') < 0.0):
                                        syms = keyi.get('symbol')
                                        mPrices = keyi.get('markPrice')
                                        priceIns = keyi.get('entryPrice')
                                        positionAmtShort = keyi.get('positionAmt')
                                        dym_cur_short_price = float(mPrices)
                                        short_amount = float(positionAmtShort*-1)
                                        #print("dc_price",dym_cur_long_price)
                                        add_short_price =  float(priceIns)+ float(priceIns)*((float(dym_cur_short_price) - float(priceIns))/(float(priceIns))*first_p)
                                        add_short_p = round(add_short_price,2)
                                        #psl.append(add_short_p)
                                        print("add_short_p" ,add_short_p)
                                        #time.sleep(1)
                                        print("ps [-1] in loop",psl)
                                        #time.sleep(1)
                                        #last_p = ps[-1]
                                        if (float(ass) != float(short_amount) or mPrices < Decimal(psfff) ):
                                            stop_threads = True
                                        psin = str(round(float(priceIns) -((first_p* float(priceIns))/20),2))
                                        # if (mPrices <= Decimal(psin) ):
                                        #     stop_threads = True
                                        if (float(dym_cur_short_price) < psl[-1]):
                                            if (add_short_p < psl[-1]):
                                        
                                                #exit_price = add_long_price
                                                psl.append(add_short_p)
                                        
                                                print("add_last_short_price" , add_short_p)
                                                #time.sleep(1)_
                                                print("ps in if",psl)
                                                #time.sleep(1)
                                        elif (float(dym_cur_short_price) >= psl[-1]):
                                            prices = round(psl[-1],2)
                                            print("last_short_TP_price",prices)
                                            #cancel_order_all()
                                            take_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET, quantity=ass)
                                            #take_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=prices, quantity=ass,timeInForce='GTC')
                                            PrintBasic.print_obj(take_profit_short)
                                            #time.sleep(1)

                                            psl = []
                                            stop_threads = True
                        elif (mPrices <= Decimal(psfff) and mPrices > Decimal(psffff) ):
                            # ps = []
                            add_int_short_price =  round(float(priceIns)+ ((float(mPrices) - float(priceIns))/(float(priceIns)*100)*sec_p),2)
                            #print("in if")
                            #time.sleep(1)
                            add_short_price = 0
                            psl.append(add_int_short_price)
                            print("ps [-1]",psl[-1])
                            #time.sleep(1)
                            stop_threads = False
                            while ((stop_threads == False ) and mPrices > Decimal(psffff)):
                            #while True:
                                request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                                result_in = request_client.get_position()
                                #sxp_account_trade_in = request_client.get_account_trades(symbol="SXPUSDT",limit= 1)
                                time.sleep(1)
                                object_list_in = []
                                for res_in in result_in:
                                    d = collections.defaultdict()
                                    d['symbol'] = res_in.symbol
                                    d['positionAmt'] = res_in.positionAmt
                                    d['entryPrice'] = res_in.entryPrice
                                    d['markPrice'] = res_in.markPrice
                                    d['positionSide'] = res_in.positionSide
                                    #d['unRealizedProfit'] = res.unRealizedProfit
                                    object_list_in.append(d)
                                    #j = json.dumps(object_list, indent=4)
                                for keyi in object_list_in:
                                    if (keyi.get('positionSide') =='SHORT' and keyi.get('symbol') =='ETHUSDT' and keyi.get('positionAmt') < 0.0):
                                        syms = keyi.get('symbol')
                                        mPrices = keyi.get('markPrice')
                                        priceIns = keyi.get('entryPrice')
                                        positionAmtShort = keyi.get('positionAmt')
                                        dym_cur_short_price = float(mPrices)
                                        short_amount = float(positionAmtShort*-1)
                                        #print("dc_price",dym_cur_long_price)
                                        add_short_price =  float(priceIns)+ float(priceIns)*((float(dym_cur_short_price) - float(priceIns))/(float(priceIns))*sec_p)
                                        add_short_p = round(add_short_price,2)
                                        #psl.append(add_short_p)
                                        print("add_short_p" ,add_short_p)
                                        #time.sleep(1)
                                        print("ps [-1] in loop",psl)
                                        #time.sleep(1)
                                        #last_p = ps[-1]
                                        if (float(ass) != float(short_amount) or mPrices < Decimal(psffff) ):
                                            stop_threads = True
                                        psin = str(round(float(priceIns) -((sec_p* float(priceIns))/20),2))
                                        # if (mPrices <= Decimal(psin) ):
                                        #     stop_threads = True
                                        if (float(dym_cur_short_price) < psl[-1]):
                                            if (add_short_p < psl[-1]):
                                        
                                                #exit_price = add_long_price
                                                psl.append(add_short_p)
                                        
                                                print("add_last_short_price" , add_short_p)
                                                #time.sleep(1)_
                                                print("ps in if",psl)
                                                #time.sleep(1)
                                        elif (float(dym_cur_short_price) >= psl[-1]):
                                            prices = round(psl[-1],2)
                                            print("last_short_TP_price",prices)
                                            #cancel_order_all()
                                            take_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET, quantity=ass)
                                            #take_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=prices, quantity=ass,timeInForce='GTC')
                                            PrintBasic.print_obj(take_profit_short)
                                            #time.sleep(1)

                                            psl = []
                                            stop_threads = True

                        elif (mPrices <= Decimal(psffff) and mPrices > Decimal(ps) ):
                            # ps = []
                            add_int_short_price =  round(float(priceIns)+ ((float(mPrices) - float(priceIns))/(float(priceIns)*100)*thr_p),2)
                            #print("in if")
                            #time.sleep(1)
                            add_short_price = 0
                            psl.append(add_int_short_price)
                            print("ps [-1]",psl[-1])
                            #time.sleep(1)
                            stop_threads = False
                            while ((stop_threads == False ) and mPrices > Decimal(ps)):
                            #while True:
                                request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                                result_in = request_client.get_position()
                                #sxp_account_trade_in = request_client.get_account_trades(symbol="SXPUSDT",limit= 1)
                                time.sleep(1)
                                object_list_in = []
                                for res_in in result_in:
                                    d = collections.defaultdict()
                                    d['symbol'] = res_in.symbol
                                    d['positionAmt'] = res_in.positionAmt
                                    d['entryPrice'] = res_in.entryPrice
                                    d['markPrice'] = res_in.markPrice
                                    d['positionSide'] = res_in.positionSide
                                    #d['unRealizedProfit'] = res.unRealizedProfit
                                    object_list_in.append(d)
                                    #j = json.dumps(object_list, indent=4)
                                for keyi in object_list_in:
                                    if (keyi.get('positionSide') =='SHORT' and keyi.get('symbol') =='ETHUSDT' and keyi.get('positionAmt') < 0.0):
                                        syms = keyi.get('symbol')
                                        mPrices = keyi.get('markPrice')
                                        priceIns = keyi.get('entryPrice')
                                        positionAmtShort = keyi.get('positionAmt')
                                        dym_cur_short_price = float(mPrices)
                                        short_amount = float(positionAmtShort*-1)
                                        #print("dc_price",dym_cur_long_price)
                                        add_short_price =  float(priceIns)+ float(priceIns)*((float(dym_cur_short_price) - float(priceIns))/(float(priceIns))*thr_p)
                                        add_short_p = round(add_short_price,2)
                                        #psl.append(add_short_p)
                                        print("add_short_p" ,add_short_p)
                                        #time.sleep(1)
                                        print("ps [-1] in loop",psl)
                                        #time.sleep(1)
                                        #last_p = ps[-1]
                                        if (float(ass) != float(short_amount)):
                                            stop_threads = True
                                        psin = str(round(float(priceIns) -((thr_p* float(priceIns))/20),2))
                                        # if (mPrices <= Decimal(psin) ):
                                        #     stop_threads = True
                                        if (float(dym_cur_short_price) < psl[-1]):
                                            if (add_short_p < psl[-1]):
                                        
                                                #exit_price = add_long_price
                                                psl.append(add_short_p)
                                        
                                                print("add_last_short_price" , add_short_p)
                                                #time.sleep(1)_
                                                print("ps in if",psl)
                                                #time.sleep(1)
                                        elif (float(dym_cur_short_price) >= psl[-1]):
                                            prices = round(psl[-1],2)
                                            print("last_short_TP_price",prices)
                                            #cancel_order_all()
                                            take_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET, quantity=ass)
                                            #take_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=prices, quantity=ass,timeInForce='GTC')
                                            PrintBasic.print_obj(take_profit_short)
                                            #time.sleep(1)

                                            psl = []
                                            stop_threads = True



                        # elif (mPrices <= Decimal(ps) ):
                        #     #cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=mPrices, quantity=ass//2,timeInForce='GTC')
                        #     cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET, quantity= str(round(float(ass),2)))
                        print(syms)
                        print(ps)
                        print(ass)
                        print(mPrices)
                    #return
    ##                    if (mPrices <= Decimal(psloss)):
    ##                        ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                    except IndexError as error:
                        print("Exiting: with error in try" + "\n")
                    except Exception as exception:
                        print("Exiting: Exception error in try" +  "\n")

            time.sleep(20)
            temp = tempfile.TemporaryFile()
            tempdir = tempfile.gettempdir()
            print(f"tempdir: {tempdir}")
            print(f"temp : {temp}")
            print(f"temp name : {temp.name}")
            temp.close()
            time.sleep(1)
    except IndexError as error:
        print("Exiting: with error" + "\n")
    except Exception as exception:
        print("Exiting: Exception error" +  "\n")
    else:
        print("Connection Error")
    

