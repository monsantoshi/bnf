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
        b1.check_profit_long_algo()
        print("Exiting: 1" + self.name + "\n")

class Bin2(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 2" + self.name + "\n")
        b2 = CheckProfitShort(market)
        b2.check_profit_short_algo()
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
        b6.check_profit_long_algo()
        print("Exiting: 6" + self.name + "\n")
class Bin7(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 7" + self.name + "\n")
        b7 = CheckProfitShortFromOut(market)
        b7.check_profit_short_algo()
        print("Exiting: 7" + self.name + "\n")
class Bin8(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 8" + self.name + "\n")
        b8 = CheckLossLong(market)
        b8.check_loss_long_algo()
        print("Exiting: 8" + self.name + "\n")
class Bin9(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 9" + self.name + "\n")
        b9 = CheckLossShort(market)
        b9.check_loss_short_algo()
        print("Exiting: 9" + self.name + "\n")
class Bin11(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 11 " + self.name + "\n")
        b11 = CheckProfitLongMore(market)
        b11.check_profit_long_algo()
        print("Exiting: 11 " + self.name + "\n")

class Bin12(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 12 " + self.name + "\n")
        b12 = CheckProfitShortMore(market)
        b12.check_profit_short_algo()
        print("Exiting: 12 " + self.name + "\n")

class Bin13(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 13" + self.name + "\n")
        b13 = CheckLossLongFromIn(market)
        b13.check_profit_long_algo()
        print("Exiting: 13" + self.name + "\n")
class Bin14(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 14" + self.name + "\n")
        b14 = CheckLossShortFromIn(market)
        b14.check_profit_short_algo()
        print("Exiting: 14" + self.name + "\n")

class Bin15(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting: 15" + self.name + "\n")
        b15 = CheckProfitLongFix(market)
        b15.check_profit_long_algo()
        print("Exiting: 15" + self.name + "\n")

class Bin16(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting: 16" + self.name + "\n")
        b16 = CheckProfitShortFix(market)
        b16.check_profit_short_algo()
        print("Exiting: 16" + self.name + "\n")
        
class Bin17(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 17" + self.name + "\n")
        b17 = CheckLossLongMore(market)
        b17.check_loss_long_algo()
        print("Exiting: 17" + self.name + "\n")
class Bin18(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):
        print("Starting: 18" + self.name + "\n")
        b18 = CheckLossShortMore(market)
        b18.check_loss_short_algo()
        print("Exiting: 18" + self.name + "\n")
        
class Bin33(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting: 33 " + self.name + "\n") 
        b33 = CountCandle(market)
        b33.take_order_point()
        print("Exiting: 33 " + self.name + "\n")


class Bin666(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting:666 " + self.name + "\n") 
        b666 = TakeProfitDoge(market)
        b666.clean_open_order_algo()
        print("Exiting: 666 " + self.name + "\n")

class Bin888(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting:666 " + self.name + "\n") 
        b888 = TakeProfitDoge(market)
        b888.take_profit_long_algo()
        print("Exiting: 666 " + self.name + "\n")

       
class TryToTakeOrder:

    def __init__(self,market):
        self.market = market

    def take_order_point(self):

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


        result = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
            result_xtz = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
        #old malgood
        kline2 = request_client.get_candlestick_data(symbol="ALGOUSDT", interval=CandlestickInterval.MIN1,startTime=None, endTime=None, limit=20)
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
        haopen6 = (float(open6)+float(close6))//2
        if (math.isnan(float(haopen6))):
            haopen5 = (float(haopen5)+float(haclose5))//2
        else:
            haopen5 = (float(haopen6)+float(haclose6))//2
        if (math.isnan(float(haopen5))):
            haopen4 = (float(haopen4)+float(haclose4))//2
        else:
            haopen4 = (float(haopen5)+float(haclose5))//2
        if (math.isnan(float(haopen4))):
            haopen3 = (float(haopen3)+float(haclose3))//2
        else:
            haopen3 = (float(haopen4)+float(haclose4))//2
        if (math.isnan(float(haopen3))):
            haopen2 = (float(haopen2)+float(haclose2))//2
        else:
            haopen2 = (float(haopen3)+float(haclose3))//2
        if (math.isnan(float(haopen2))):
            haopen1 = (float(haopen1)+float(haclose1))//2
        else:
            haopen1 = (float(haopen2)+float(haclose2))//2
        if (math.isnan(float(haopen1))):
            haopen = (float(haopen)+float(haclose))//2
        else:
            haopen = (float(haopen1)+float(haclose1))//2

        Down =  (float(haopen) > float(haclose)) and (s == 1)
        #algo_TrendDown = Bearish_Engulfing
        print("Down",Down)
        Up =  (float(haopen) < float(haclose)) and (l == 1)
        #algo_TrendUp =  Bullish_Engulfing
        print("Up",Up)
        result_p = request_client.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
        print(order_list[long_idx]["symbol"]+'  '+str(order_list[long_idx]["positionAmt"])+'  '+str(order_list[long_idx]["entryPrice"])+'  '+str(order_list[long_idx]["markPrice"]))
        print(order_list[short_idx]["symbol"]+'  '+str(order_list[short_idx]["positionAmt"])+'  '+str(order_list[short_idx]["entryPrice"])+'  '+str(order_list[short_idx]["markPrice"]))
        #time.sleep(1)
        #if ((order_list[long_idx]["positionAmt"]) < step_one_unit)) :

        if ((Down) and ((algo_active_plan =='C'))):
       
            print("take_order_short_full")
            take_order_sell(self)
            #take_order_short = request_client.post_order(symbol="ALGOUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
            #PrintBasic.print_obj(take_order_short)
            #time.sleep(1)

            return
       
        if ((Up) and ((algo_active_plan =='B'))):
            print("take_order_long_full")
            take_order_buy(self)
            #take_order_long = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
            #PrintBasic.print_obj(take_order_long)
            time.sleep(1)
 
            return

class CountCandle:

    def __init__(self,market):
        self.market = market

    def take_order_point(self):

        f1 = 0.35
        f2 = 0.07
        f3 = 0.25

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


        result = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
        enterShort1 = False
        enterShort2 = False
        enterLong1 = False
        enterLong2 = False
        i = 15
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
        #time.sleep(1)
        price_bids.append(init_price_bid)
        price_asks.append(init_price_ask)

        for i in range(20):
            result_algo = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
            #time.sleep(1)
            for resb in result_algo.bids:
                #print(resb.qty)
                bid_q.append(round(float(resb.qty),4))
                bid_p.append(round(float(resb.price),4))

               
            for resa in result_algo.asks:
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
            #time.sleep(1)
        #print("price_asks : ",price_asks)
        #print("price_bids : ",price_bids)
        #print("price_asks_first ",price_asks[0])
        #print("price_asks_last ",price_asks[39])
        #print("price_bids_first ",price_bids[0])
        #print("price_bids_last ",price_bids[39])
        s = 0
        l = 0
        if (price_asks[0]< price_asks[10]):
            s = 0
            l = 1
        elif (price_asks[0] > price_asks[19]):
            s = 1
            l = 0
        #print(" s ",s)

        if (price_bids[0]< price_bids[19]):
            l = 1
            s = 0
        elif (price_bids[0] > price_bids[19]):
            l = 0
            s = 1
        #old malgood
        kline2 = request_client.get_candlestick_data(symbol="ALGOUSDT", interval=CandlestickInterval.MIN15,startTime=None, endTime=None, limit=10)
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

        sSetup = round(float(high5) + f1 * (float(close5)-float(low5)),4)
        bSetup = round(float(low5) - f1 * (float(high5)-float(close5)),4)
        bBreak = round(sSetup + f3 * (sSetup-bSetup),4)
        sEnter = round(((float(low5)+f2)/2) * (float(high5)+ float(close5)) - f2*float(low5),4)
        bEnter = round(((float(low5)+f2)/2) * (float(low5)+ float(close5)) - f2*float(high5),4)
        sBreak = round(bSetup-f3 * (sSetup - bSetup),4)



        haclose = (float(open0)+float(high0)+float(low0)+float(close0))/4
        haclose1 = (float(open1)+float(high1)+float(low1)+float(close1))/4
        haclose2 = (float(open2)+float(high2)+float(low2)+float(close2))/4
        haclose3 = (float(open3)+float(high3)+float(low3)+float(close3))/4
        haclose4 = (float(open4)+float(high4)+float(low4)+float(close4))/4
        haclose5 = (float(open5)+float(high5)+float(low5)+float(close5))/4
        haclose6 = (float(open6)+float(high6)+float(low6)+float(close6))/4
        haopen6 = (float(open6)+float(close6))//2
        if (math.isnan(float(haopen6))):
            haopen5 = (float(haopen5)+float(haclose5))//2
        else:
            haopen5 = (float(haopen6)+float(haclose6))//2
        if (math.isnan(float(haopen5))):
            haopen4 = (float(haopen4)+float(haclose4))//2
        else:
            haopen4 = (float(haopen5)+float(haclose5))//2
        if (math.isnan(float(haopen4))):
            haopen3 = (float(haopen3)+float(haclose3))//2
        else:
            haopen3 = (float(haopen4)+float(haclose4))//2
        if (math.isnan(float(haopen3))):
            haopen2 = (float(haopen2)+float(haclose2))//2
        else:
            haopen2 = (float(haopen3)+float(haclose3))//2
        if (math.isnan(float(haopen2))):
            haopen1 = (float(haopen1)+float(haclose1))//2
        else:
            haopen1 = (float(haopen2)+float(haclose2))//2
        if (math.isnan(float(haopen1))):
            haopen = (float(haopen)+float(haclose))//2
        else:
            haopen = (float(haopen1)+float(haclose1))//2


        sTrigger = False
        bTrigger = False
  
        
        result_m = request_client.get_mark_price("ALGOUSDT")

##        print("result_m", result_m.markPrice)

            
        markPrice = result_m.markPrice


        sTrigger = ((round(float(markPrice),4) < sSetup)  or (round(float(markPrice),4) < sBreak))
        bTrigger = ((round(float(markPrice),4) < bSetup)  or (round(float(markPrice),4) < bBreak))
        
        enterShort1 = round(float(markPrice),4) < sBreak 
        enterShort2 = ((round(float(markPrice),4) < sEnter) and ((sTrigger== True)  < i) and ((sTrigger == True) < (bTrigger == True)))
##        print("markPrice", markPrice)
##        print("enterShort1", enterShort1)
##        print("enterShort2", enterShort2)
        Down =  ((enterShort1 or enterShort2)) # and (s == 1) and (l==0) or (float(haopen6) > float(haclose6)))
        #Down =  ((enterShort1 or enterShort2) and (s == 1) and (l==0) or (float(haopen6) > float(haclose6)))
        #algo_TrendDown = Bearish_Engulfing
        print("Down",Down)
        

        enterLong1 = round(float(markPrice),4) > bBreak
        enterLong2 = ((round(float(markPrice),4) > bEnter) and ((bTrigger== True)  < i) and ((bTrigger == True) < (sTrigger == True)))

##        print("enterLong1", enterLong1)
##        print("enterLong2", enterLong2)
##        
        Up =  ((enterLong1 or enterLong2))# and (l == 1) and (s==0) or (float(haopen6) < float(haclose6)))
       # Up =  ((enterLong1 or enterLong2) and (l == 1) and (s==0) or (float(haopen6) < float(haclose6)))
        #algo_TrendUp =  Bullish_Engulfing
        print("Up",Up)
        time.sleep(2)
        if (Down == Up):
            Down =  ((enterShort1 or enterShort2) and (s == 1) and (l==0) or (float(haopen6) > float(haclose6)))
            Up =  ((enterLong1 or enterLong2) and (l == 1) and (s==0) or (float(haopen6) < float(haclose6)))

            if (Down != Up):

                    
                result_p = request_client.get_position()
                #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                print(order_list[long_idx]["symbol"]+'  '+str(order_list[long_idx]["positionAmt"])+'  '+str(order_list[long_idx]["entryPrice"])+'  '+str(order_list[long_idx]["markPrice"]))
                print(order_list[short_idx]["symbol"]+'  '+str(order_list[short_idx]["positionAmt"])+'  '+str(order_list[short_idx]["entryPrice"])+'  '+str(order_list[short_idx]["markPrice"]))
                time.sleep(1)
                #if ((order_list[long_idx]["positionAmt"]) < step_one_unit)) :list[long_idx]["positionAmt"]) < step_one_unit)) :
                print("Down in",Down)
                print("Up in",Up)
                time.sleep(2)
                if ((Down)):
               
                    print("take_order_short_full")
                    #take_order_sell(self)
                    inc_count_s(1)
                    cls_count_l(0)
                    take_order_sell(self)
                    #take_order_short = request_client.post_order(symbol="ALGOUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                    #PrintBasic.print_obj(take_order_short)
                    #time.sleep(1)

                    return
               
                if ((Up)):
                    print("take_order_long_full")
                    #take_order_buy(self)
                    inc_count_l(1)
                    cls_count_s(0)
                    take_order_buy(self)
                    #take_order_long = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                    #PrintBasic.print_obj(take_order_long)
                    #time.sleep(1)
                return
        else:
            
                    
            result_p = request_client.get_position()
            #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
            print(order_list[long_idx]["symbol"]+'  '+str(order_list[long_idx]["positionAmt"])+'  '+str(order_list[long_idx]["entryPrice"])+'  '+str(order_list[long_idx]["markPrice"]))
            print(order_list[short_idx]["symbol"]+'  '+str(order_list[short_idx]["positionAmt"])+'  '+str(order_list[short_idx]["entryPrice"])+'  '+str(order_list[short_idx]["markPrice"]))
            time.sleep(1)
            #if ((order_list[long_idx]["positionAmt"]) < step_one_unit)) :list[long_idx]["positionAmt"]) < step_one_unit)) :

            if ((Down)):
           
                print("take_order_short_full")
                #take_order_sell(self)
                inc_count_s(1)
                cls_count_l(0)
                take_order_sell(self)
                #take_order_short = request_client.post_order(symbol="ALGOUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                #PrintBasic.print_obj(take_order_short)
                #time.sleep(1)

                return
           
            if ((Up)):
                print("take_order_long_full")
                #take_order_buy(self)
                inc_count_l(1)
                cls_count_s(0)
                take_order_buy(self)
                #take_order_long = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                #PrintBasic.print_obj(take_order_long)
                #time.sleep(1)

 
                return
        return
    def take_order_point_long(self):


        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

        result = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
            result_xtz = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
        #old malgood
        kline2 = request_client.get_candlestick_data(symbol="ALGOUSDT", interval=CandlestickInterval.MIN1,startTime=None, endTime=None, limit=20)
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
        haopen6 = (float(open6)+float(close6))//2
        if (math.isnan(float(haopen6))):
            haopen5 = (float(haopen5)+float(haclose5))//2
        else:
            haopen5 = (float(haopen6)+float(haclose6))//2
        if (math.isnan(float(haopen5))):
            haopen4 = (float(haopen4)+float(haclose4))//2
        else:
            haopen4 = (float(haopen5)+float(haclose5))//2
        if (math.isnan(float(haopen4))):
            haopen3 = (float(haopen3)+float(haclose3))//2
        else:
            haopen3 = (float(haopen4)+float(haclose4))//2
        if (math.isnan(float(haopen3))):
            haopen2 = (float(haopen2)+float(haclose2))//2
        else:
            haopen2 = (float(haopen3)+float(haclose3))//2
        if (math.isnan(float(haopen2))):
            haopen1 = (float(haopen1)+float(haclose1))//2
        else:
            haopen1 = (float(haopen2)+float(haclose2))//2
        if (math.isnan(float(haopen1))):
            haopen = (float(haopen)+float(haclose))//2
        else:
            haopen = (float(haopen1)+float(haclose1))//2



        Down =  (float(haopen) > float(haclose)) and (s == 1)
        #algo_TrendDown = Bearish_Engulfing
        print("Down",Down)
        Up =  (float(haopen) < float(haclose)) and (l == 1)
        #algo_TrendUp =  Bullish_Engulfing
        print("Up",Up)
        result_p = request_client.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
        long_price = float(order_list[long_idx]["entryPrice"])
        long_amount = float(order_list[long_idx]["positionAmt"])

       
        int_cur_long_price = float(order_list[long_idx]["markPrice"])

       
        int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20

        print(order_list[long_idx]["symbol"]+'  '+str(order_list[long_idx]["positionAmt"])+'  '+str(order_list[long_idx]["entryPrice"])+'  '+str(order_list[long_idx]["markPrice"]))
        time.sleep(1)
        if (((order_list[long_idx]["positionAmt"]) > 0) and ((order_list[long_idx]["positionAmt"]) <= step_one_unit)):


           
            if ((Up) and ((algo_active_plan =='B') )):
                print("take_order_long_full")
                take_order_buy(self)
                #take_order_long = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity= buy_unit)
                #PrintBasic.print_obj(take_order_long)
                time.sleep(1)
     
                return
        if (((order_list[long_idx]["positionAmt"]) > step_one_unit) and ((order_list[long_idx]["positionAmt"]) < step_two_unit) and (abs(int_long_rate * 100) > min_profit_rate_long) and (abs(int_long_rate * 100) < abs(stop_loss_rate_long))):


           
            if ((Up) and ((algo_active_plan =='B') )):
                take_order_buy(self)
                #take_order_long = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity= buy_unit)
                #PrintBasic.print_obj(take_order_long)
                time.sleep(1)
     
                return
        if (((order_list[long_idx]["positionAmt"]) >= step_two_unit) and ((order_list[long_idx]["positionAmt"]) <= step_three_unit) and (abs(int_long_rate * 100) > min_profit_rate_long) and (abs(int_long_rate * 100) < abs(stop_loss_rate_long))):


           
            if ((Up) and ((algo_active_plan =='B'))):
                print("take_order_long_full")
                take_order_buy(self)
                #take_order_long = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity= buy_unit)
                #PrintBasic.print_obj(take_order_long)
                time.sleep(1)
     
                return

        return
    def take_order_point_short(self):


        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)



        result = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
            result_xtz = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
        #old malgood
        kline2 = request_client.get_candlestick_data(symbol="ALGOUSDT", interval=CandlestickInterval.MIN1,startTime=None, endTime=None, limit=20)
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
        haopen6 = (float(open6)+float(close6))//2
        if (math.isnan(float(haopen6))):
            haopen5 = (float(haopen5)+float(haclose5))//2
        else:
            haopen5 = (float(haopen6)+float(haclose6))//2
        if (math.isnan(float(haopen5))):
            haopen4 = (float(haopen4)+float(haclose4))//2
        else:
            haopen4 = (float(haopen5)+float(haclose5))//2
        if (math.isnan(float(haopen4))):
            haopen3 = (float(haopen3)+float(haclose3))//2
        else:
            haopen3 = (float(haopen4)+float(haclose4))//2
        if (math.isnan(float(haopen3))):
            haopen2 = (float(haopen2)+float(haclose2))//2
        else:
            haopen2 = (float(haopen3)+float(haclose3))//2
        if (math.isnan(float(haopen2))):
            haopen1 = (float(haopen1)+float(haclose1))//2
        else:
            haopen1 = (float(haopen2)+float(haclose2))//2
        if (math.isnan(float(haopen1))):
            haopen = (float(haopen)+float(haclose))//2
        else:
            haopen = (float(haopen1)+float(haclose1))//2


        Down =  (float(haopen) > float(haclose)) and (s == 1)
        #algo_TrendDown = Bearish_Engulfing
        print("Down",Down)
        Up =  (float(haopen) < float(haclose)) and (l == 1)
        #algo_TrendUp =  Bullish_Engulfing
        print("Up",Up)
        result = request_client.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
        short_price = float(order_list[short_idx]["entryPrice"])
        short_amount = float(order_list[short_idx]["positionAmt"]*-1)

       
        int_cur_short_price = float(order_list[short_idx]["markPrice"])

       
        int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20

        print(order_list[short_idx]["symbol"]+'  '+str(order_list[short_idx]["positionAmt"])+'  '+str(order_list[short_idx]["entryPrice"])+'  '+str(order_list[short_idx]["markPrice"]))
        time.sleep(1)
        if (((order_list[short_idx]["positionAmt"]*-1) > 0) and ((order_list[short_idx]["positionAmt"]*-1) <= step_one_unit)):


            if ((Down) and ((algo_active_plan =='C'))):
           
                print("take_order_short_full")
                take_order_sell(self)
                #take_order_short = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity= sale_unit)
                #PrintBasic.print_obj(take_order_short)
                time.sleep(1)
 
                return
        if (((order_list[short_idx]["positionAmt"]*-1) > step_one_unit) and ((order_list[short_idx]["positionAmt"]*-1) < step_two_unit) and (abs(int_short_rate * 100) > min_profit_rate_short) and (abs(int_short_rate * 100) < abs(stop_loss_rate_short))):


            if ((Down) and ((algo_active_plan =='C'))):
           
                print("take_order_short_full")
                take_order_sell(self)
                #take_order_short = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity= sale_unit)
                #PrintBasic.print_obj(take_order_short)
                time.sleep(1)
 
                return
        if (((order_list[short_idx]["positionAmt"]*-1) >= step_two_unit) and ((order_list[short_idx]["positionAmt"]*-1) <= step_three_unit) and (abs(int_short_rate * 100) > min_profit_rate_short) and (abs(int_short_rate * 100) < abs(stop_loss_rate_short))):


            if ((Down) and ((algo_active_plan =='C'))):
           
                print("take_order_short_full")
                take_order_sell(self)
                #take_order_short = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity= sale_unit)
                #PrintBasic.print_obj(take_order_short)
                time.sleep(1)
 
                return
     
        return


class CheckProfitLong:

    def __init__(self,market):
        self.market = market


    def check_profit_long_algo(self):
            #price_exit = 0
        global stop_threads
        if stop_threads:
            return
        else:
            pl = []
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result = request_client.get_position()
            #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
           
            #long_price  = 7150
            long_price = float(object_list[long_idx]["entryPrice"])
            long_amount = float(object_list[long_idx]["positionAmt"])

           
            int_cur_long_price = float(object_list[long_idx]["markPrice"])

           
            int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20


     
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_long_rate : ",round((int_long_rate*100),4))
            print("Mark Price : ",int_cur_long_price)
            if (((int_long_rate*100) >= min_profit_rate_long) and (long_amount >=  step_three_unit)):
                take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                PrintBasic.print_obj(take_profit_algo)
                time.sleep(1)

                pl = []            
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > step_two_unit) and (long_amount < step_three_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(3)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_long_price = float(object_list_in[long_idx]["markPrice"])
                    long_amount = float(object_list_in[long_idx]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(3)
                    print("pl [-1] in loop",pl)
                    #time.sleep(3)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(2)
                            print("pl in if",pl)
                            #time.sleep(2)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        pl = []
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > step_one_unit) and (long_amount <= step_two_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(3)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_long_price = float(object_list_in[long_idx]["markPrice"])
                    long_amount = float(object_list_in[long_idx]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(3)
                    print("pl [-1] in loop",pl)
                    #time.sleep(3)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(2)
                            print("pl in if",pl)
                            #time.sleep(2)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        pl = []
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > 0) and (long_amount <= step_one_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(3)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_long_price = float(object_list_in[long_idx]["markPrice"])
                    long_amount = float(object_list_in[long_idx]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(3)
                    print("pl [-1] in loop",pl)
                    #time.sleep(3)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(2)
                            print("pl in if",pl)
                            #time.sleep(2)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        pl = []
        return



class CheckProfitShort:

    def __init__(self,market):
        self.market = market


    def check_profit_short_algo(self):
            #price_exit = 0
        global stop_threads
        if stop_threads:
            return
        else:
           
            ps = []
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result = request_client.get_position()
            #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
           
            #long_price  = 7150
            short_price = float(object_list[short_idx]["entryPrice"])
            short_amount = float(object_list[short_idx]["positionAmt"]*-1)

           
            int_cur_short_price = float(object_list[short_idx]["markPrice"])

           
            int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


     
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_short_rate : ",round((int_short_rate*100),4))
            print("Mark Price Short: ",int_cur_short_price)
            if (((int_short_rate*100) >= min_profit_rate_short) and (short_amount >= step_three_unit)):
                take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                PrintBasic.print_obj(take_profit_algo)
                time.sleep(1)

                ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > step_two_unit) and  (short_amount < step_three_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(3)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(3)
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_short_price = float(object_list_in[short_idx]["markPrice"])
                    short_amount = float(object_list_in[short_idx]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(3)
                    print("ps [-1] in loop",ps)
                    #time.sleep(3)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(2)_
                            print("ps in if",ps)
                            #time.sleep(2)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > step_one_unit) and  (short_amount <= step_two_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(3)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(3)
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_short_price = float(object_list_in[short_idx]["markPrice"])
                    short_amount = float(object_list_in[short_idx]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(3)
                    print("ps [-1] in loop",ps)
                    #time.sleep(3)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(2)_
                            print("ps in if",ps)
                            #time.sleep(2)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > 0) and  (short_amount <= step_one_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(3)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(3)
                #while ((stop_threads == False) and (len(ps) <5)):
                while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_short_price = float(object_list_in[short_idx]["markPrice"])
                    short_amount = float(object_list_in[short_idx]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(3)
                    print("ps [-1] in loop",ps)
                    #time.sleep(3)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(2)_
                            print("ps in if",ps)
                            #time.sleep(2)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        ps = []

        return


class CheckProfitLongFix:

    def __init__(self,market):
        self.market = market


    def check_profit_long_algo(self):
            #price_exit = 0
        global stop_threads
        if stop_threads:
            return
        else:
            pl = []
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result = request_client.get_position()
            #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
           
            #long_price  = 7150
            long_price = float(object_list[long_idx]["entryPrice"])
            long_amount = float(object_list[long_idx]["positionAmt"])

           
            int_cur_long_price = float(object_list[long_idx]["markPrice"])

           
            int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20


     
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_long_rate : ",round((int_long_rate*100),4))
            print("Mark Price : ",int_cur_long_price)
            if (((int_long_rate*100) >= min_profit_rate_long) and (long_amount >=  step_three_unit)):
                take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                PrintBasic.print_obj(take_profit_algo)
                time.sleep(1)

                pl = []            
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > step_two_unit) and (long_amount < step_three_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(3)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                while ((stop_threads == False) and (len(pl) < 6)):
                #while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_long_price = float(object_list_in[long_idx]["markPrice"])
                    long_amount = float(object_list_in[long_idx]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(3)
                    print("pl [-1] in loop",pl)
                    #time.sleep(3)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(2)
                            print("pl in if",pl)
                            #time.sleep(2)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        pl = []
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > step_one_unit) and (long_amount <= step_two_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(3)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                while ((stop_threads == False) and (len(pl) < 6)):
                #while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_long_price = float(object_list_in[long_idx]["markPrice"])
                    long_amount = float(object_list_in[long_idx]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(3)
                    print("pl [-1] in loop",pl)
                    #time.sleep(3)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(2)
                            print("pl in if",pl)
                            #time.sleep(2)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        pl = []
            if (((int_long_rate*100) >= stop_profit_rate_long) and ((long_amount > 0) and (long_amount <= step_one_unit))):
                add_int_long_price =  round(float(long_price)+ ((float(int_cur_long_price) - float(long_price))/(float(long_price)*100)*protect_profit),4)
                #print("in if")
                #time.sleep(3)
                add_long_price = 0
                pl.append(add_int_long_price)
                print("pl [-1]",pl[-1])
                while ((stop_threads == False) and (len(pl) < 6)):
                #while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_long_price = float(object_list_in[long_idx]["markPrice"])
                    long_amount = float(object_list_in[long_idx]["positionAmt"])
                    #print("dc_price",dym_cur_long_price)
                    add_long_price =  float(long_price)+ float(long_price)*((float(dym_cur_long_price) - float(long_price))/(float(long_price))*protect_profit)
                    add_long_p = round(add_long_price,4)
                    #pl.append(add_long_p)
                    print("add_long_p" ,add_long_p)
                    #time.sleep(3)
                    print("pl [-1] in loop",pl)
                    #time.sleep(3)
                    #last_p = pl[-1]
                    if (float(dym_cur_long_price) > pl[-1]):
                        if (add_long_p > pl[-1]):
                       
                            #exit_price = add_long_price
                            pl.append(add_long_p)
                       
                            print("add_last_price" , add_long_p)
                            #time.sleep(2)
                            print("pl in if",pl)
                            #time.sleep(2)
                    elif (float(dym_cur_long_price) <= pl[-1]):
                        price = round(pl[-1],4)
                        print("last_long_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        pl = []
        return



class CheckProfitShortFix:

    def __init__(self,market):
        self.market = market


    def check_profit_short_algo(self):
            #price_exit = 0
        global stop_threads
        if stop_threads:
            return
        else:
           
            ps = []
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result = request_client.get_position()
            #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
           
            #long_price  = 7150
            short_price = float(object_list[short_idx]["entryPrice"])
            short_amount = float(object_list[short_idx]["positionAmt"]*-1)

           
            int_cur_short_price = float(object_list[short_idx]["markPrice"])

           
            int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


     
            #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
             #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_short_rate : ",round((int_short_rate*100),4))
            print("Mark Price Short: ",int_cur_short_price)
            if (((int_short_rate*100) >= min_profit_rate_short) and (short_amount >= step_three_unit)):
                take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                PrintBasic.print_obj(take_profit_algo)
                time.sleep(1)

                ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > step_two_unit) and  (short_amount < step_three_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(3)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(3)
                while ((stop_threads == False)  and (len(ps) < 6) ):
                #while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_short_price = float(object_list_in[short_idx]["markPrice"])
                    short_amount = float(object_list_in[short_idx]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(3)
                    print("ps [-1] in loop",ps)
                    #time.sleep(3)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(2)_
                            print("ps in if",ps)
                            #time.sleep(2)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > step_one_unit) and  (short_amount <= step_two_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(3)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(3)
                while ((stop_threads == False)  and (len(ps) < 6) ):
                #while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_short_price = float(object_list_in[short_idx]["markPrice"])
                    short_amount = float(object_list_in[short_idx]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(3)
                    print("ps [-1] in loop",ps)
                    #time.sleep(3)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(2)_
                            print("ps in if",ps)
                            #time.sleep(2)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        ps = []
            if (((int_short_rate*100) >= stop_profit_rate_short) and ((short_amount > 0) and  (short_amount <= step_one_unit))):
                add_int_short_price =  round(float(short_price)+ ((float(int_cur_short_price) - float(short_price))/(float(short_price)*100)*protect_profit_s),4)
                #print("in if")
                #time.sleep(3)
                add_short_price = 0
                ps.append(add_int_short_price)
                print("ps [-1]",ps[-1])
                #time.sleep(3)
                while ((stop_threads == False) and (len(ps) < 6) ):
                #while True:
                    request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                    result_in = request_client_in.get_position()
                    #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
                    dym_cur_short_price = float(object_list_in[short_idx]["markPrice"])
                    short_amount = float(object_list_in[short_idx]["positionAmt"]*-1)
                    #print("dc_price",dym_cur_long_price)
                    add_short_price =  float(short_price)+ float(short_price)*((float(dym_cur_short_price) - float(short_price))/(float(short_price))*protect_profit_s)
                    add_short_p = round(add_short_price,4)
                    #pl.append(add_long_p)
                    print("add_short_p" ,add_short_p)
                    #time.sleep(3)
                    print("ps [-1] in loop",ps)
                    #time.sleep(3)
                    #last_p = ps[-1]
                    if (float(dym_cur_short_price) < ps[-1]):
                        if (add_short_p < ps[-1]):
                       
                            #exit_price = add_long_price
                            ps.append(add_short_p)
                       
                            print("add_last_short_price" , add_short_p)
                            #time.sleep(2)_
                            print("ps in if",ps)
                            #time.sleep(2)
                    elif (float(dym_cur_short_price) >= ps[-1]):
                        price = round(ps[-1],4)
                        print("last_short_TP_price",price)
                        #cancel_order_all()
                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
                        PrintBasic.print_obj(take_profit_algo)
                        time.sleep(1)

                        ps = []

        return

class CheckProfitLongFromOut:

    def __init__(self,market):
        self.market = market


    def check_profit_long_algo(self):
        int_short_rate_out = 0
        in_short_out = False
        in_long_out = False
        in_short_in = False
        in_long_in = False
        short_amount_in = 0
        long_amount_in = 0
        request_client_out = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client_out.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
       
        #long_price  = 7150
        short_price_out = float(object_list_out[short_idx]["entryPrice"])
        short_amount_out = float(object_list_out[short_idx]["positionAmt"])*-1
       
        if (short_amount_out > 0):
            in_short_out = True

       
        int_cur_short_price_out = float(object_list_out[short_idx]["markPrice"])

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
                #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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

                short_amount_in = float(object_list_in[short_idx]["positionAmt"])*-1
                if ((short_amount_in == 0) and (short_amount_in < short_amount_out)):
                    take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
                    PrintBasic.print_obj(take_profit_algo)
                    time.sleep(1)
##            if ((int_short_rate_out * 100) <= (stop_profit_rate_short * -1)):
##                result = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
##                    result_xtz = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
##                #old malgood
##                kline2 = request_client.get_candlestick_data(symbol="ALGOUSDT", interval=interval,startTime=None, endTime=None, limit=20)
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
##                haopen6 = (float(open6)+float(close6))//2
##                if (math.isnan(float(haopen6))):
##                    haopen5 = (float(haopen5)+float(haclose5))//2
##                else:
##                    haopen5 = (float(haopen6)+float(haclose6))//2
##                if (math.isnan(float(haopen5))):
##                    haopen4 = (float(haopen4)+float(haclose4))//2
##                else:
##                    haopen4 = (float(haopen5)+float(haclose5))//2
##                if (math.isnan(float(haopen4))):
##                    haopen3 = (float(haopen3)+float(haclose3))//2
##                else:
##                    haopen3 = (float(haopen4)+float(haclose4))//2
##                if (math.isnan(float(haopen3))):
##                    haopen2 = (float(haopen2)+float(haclose2))//2
##                else:
##                    haopen2 = (float(haopen3)+float(haclose3))//2
##                if (math.isnan(float(haopen2))):
##                    haopen1 = (float(haopen1)+float(haclose1))//2
##                else:
##                    haopen1 = (float(haopen2)+float(haclose2))//2
##                if (math.isnan(float(haopen1))):
##                    haopen = (float(haopen)+float(haclose))//2
##                else:
##                    haopen = (float(haopen1)+float(haclose1))//2
##
##
##                Down =  (float(haopen) > float(haclose)) and (s == 1)
##                #algo_TrendDown = Bearish_Engulfing
##                print("Down",Down)
##                Up =  (float(haopen) < float(haclose)) and (l == 1)
##                #algo_TrendUp =  Bullish_Engulfing
##                print("Up",Up)
##                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
##                result_in = request_client_in.get_position()
##                #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
##                #short_amount_in = float(object_list_in[short_idx]["positionAmt"]*-1)
##                long_amount_in = float(object_list_in[long_idx]["positionAmt"])
##                if (long_amount_in > 0):
##
##                    in_long_in = True
##
##                if ((Up) and (long_amount_in == 0) and (long_amount_in < short_amount_out)):
##                    take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit*2)
##                    PrintBasic.print_obj(take_profit_algo)
##                    time.sleep(1)
##
##                if (in_long_in):
##                    if ((Up) and (long_amount_in < step_three_unit) and (long_amount_in < short_amount_out) and (short_amount_out < step_three_unit)):
##                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
##                        PrintBasic.print_obj(take_profit_algo)
##                        time.sleep(1)
##                        return
##                    if ((Up) and (long_amount_in < step_three_unit) and (long_amount_in < short_amount_out) and (short_amount_out >= step_three_unit)):
##                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
##                        PrintBasic.print_obj(take_profit_algo)
##                        time.sleep(1)
##                        return

        return



class CheckProfitShortFromOut:

    def __init__(self,market):
        self.market = market


    def check_profit_short_algo(self):
        int_long_rate_out = 0
        in_short_out = False
        in_long_out = False
        in_short_in = False
        in_long_in = False
        short_amount_in = 0
        long_amount_in = 0
        request_client_out = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client_out.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
       
        #long_price  = 7150
        long_price_out = float(object_list_out[long_idx]["entryPrice"])
        long_amount_out = float(object_list_out[long_idx]["positionAmt"])
       
        if (long_amount_out > 0):

            in_long_out = True

       
        int_cur_long_price_out = float(object_list_out[long_idx]["markPrice"])

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
                #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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

                long_amount_in = float(object_list_in[long_idx]["positionAmt"])
                if ((long_amount_in == 0) and (long_amount_in < long_amount_out)):
                    take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                    PrintBasic.print_obj(take_profit_algo)
                    time.sleep(1)
##            if ((int_long_rate_out * 100) <= (stop_profit_rate_long * -1)):
##                result = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
##                    result_xtz = request_client.get_order_book(symbol = "ALGOUSDT", limit = 20)
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
##                #old malgood
##                kline2 = request_client.get_candlestick_data(symbol="ALGOUSDT", interval=interval,startTime=None, endTime=None, limit=20)
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
##                haopen6 = (float(open6)+float(close6))//2
##                if (math.isnan(float(haopen6))):
##                    haopen5 = (float(haopen5)+float(haclose5))//2
##                else:
##                    haopen5 = (float(haopen6)+float(haclose6))//2
##                if (math.isnan(float(haopen5))):
##                    haopen4 = (float(haopen4)+float(haclose4))//2
##                else:
##                    haopen4 = (float(haopen5)+float(haclose5))//2
##                if (math.isnan(float(haopen4))):
##                    haopen3 = (float(haopen3)+float(haclose3))//2
##                else:
##                    haopen3 = (float(haopen4)+float(haclose4))//2
##                if (math.isnan(float(haopen3))):
##                    haopen2 = (float(haopen2)+float(haclose2))//2
##                else:
##                    haopen2 = (float(haopen3)+float(haclose3))//2
##                if (math.isnan(float(haopen2))):
##                    haopen1 = (float(haopen1)+float(haclose1))//2
##                else:
##                    haopen1 = (float(haopen2)+float(haclose2))//2
##                if (math.isnan(float(haopen1))):
##                    haopen = (float(haopen)+float(haclose))//2
##                else:
##                    haopen = (float(haopen1)+float(haclose1))//2
##
##
##                Down =  (float(haopen) > float(haclose)) and (s == 1)
##                #algo_TrendDown = Bearish_Engulfing
##                print("Down",Down)
##                Up =  (float(haopen) < float(haclose)) and (l == 1)
##                #algo_TrendUp =  Bullish_Engulfing
##                print("Up",Up)
##                request_client_in = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
##                result_in = request_client_in.get_position()
##                #algo_account_trade_in = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
##                short_amount_in = float(object_list_in[short_idx]["positionAmt"])*-1
##                long_amount_in = float(object_list_in[long_idx]["positionAmt"])
##                if (short_amount_in > 0):
##                    in_short_in = True
##
##                if ((Down)  and (short_amount_in == 0) and (short_amount_in < long_amount_out)):
##                    take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,  quantity=sale_unit*2)
##                    PrintBasic.print_obj(take_profit_algo)
##                    time.sleep(1)
##
##                if (in_short_in):
##                    if ((Down)  and (short_amount_in < step_three_unit) and (short_amount_in < long_amount_out) and (long_amount_out < step_three_unit)):
##                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
##                        PrintBasic.print_obj(take_profit_algo)
##                        time.sleep(1)
##                        return
##                    if ((Down) and (short_amount_in < step_three_unit) and (short_amount_in < long_amount_out) and (long_amount_out >= step_three_unit)):
##                        take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
##                        PrintBasic.print_obj(take_profit_algo)
##                        time.sleep(1)
##                        return
        return

class CheckLossLong:

    def __init__(self,market):
        self.market = market


    def check_loss_long_algo(self):
            #price_exit = 0

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
       
        #long_price  = 7150
        long_price = float(object_list[long_idx]["entryPrice"])
        long_amount = float(object_list[long_idx]["positionAmt"])

       
        int_cur_long_price = float(object_list[long_idx]["markPrice"])

       
        int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_long_rate : ",(int_long_rate*100))
        #time.sleep(2)
        print("Mark Price : ",int_cur_long_price)
        if (((int_long_rate*100) <= stop_loss_rate_long) ):

            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)



        return



class CheckLossShort:

    def __init__(self,market):
        self.market = market


    def check_loss_short_algo(self):

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
       
        #long_price  = 7150
        short_price = float(object_list[short_idx]["entryPrice"])
        short_amount = float(object_list[short_idx]["positionAmt"]*-1)

       
        int_cur_short_price = float(object_list[short_idx]["markPrice"])

       
        int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_short_rate : ",(int_short_rate*100))
        #time.sleep(2)
        print("Mark Price Short: ",int_cur_short_price)
        if (((int_short_rate*100) <= stop_loss_rate_short) ):

            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)



        return

class CheckProfitLongMore:

    def __init__(self,market):
        self.market = market


    def check_profit_long_algo(self):
            #price_exit = 0
        #pl = []
        global stop_threads
        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
        #time.sleep(1)
        object_list = []
        int_long_rate = 0
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
       
        #long_price  = 7150
        long_price = float(object_list[long_idx]["entryPrice"])
        long_amount = float(object_list[long_idx]["positionAmt"])

       
        int_cur_long_price = float(object_list[long_idx]["markPrice"])

       
        int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_long_rate : ",round((int_long_rate*100),4))
        print("Mark Price : ",int_cur_long_price)
        
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount >=  step_three_unit) and (long_amount < step_four_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #pl = []            
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount > step_two_unit) and (long_amount < step_three_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #pl = []  
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount > step_one_unit) and (long_amount <= step_two_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #pl = []  
        if (((int_long_rate*100) >= stop_profit_rate_long_more) and ((long_amount > 0) and (long_amount <= step_one_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #pl = []  
        return



class CheckProfitShortMore:

    def __init__(self,market):
        self.market = market


    def check_profit_short_algo(self):
            #price_exit = 0
        #ps = []
        global stop_threads
        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()

        object_list = []
        int_short_rate = 0
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
       
        #long_price  = 7150
        short_price = float(object_list[short_idx]["entryPrice"])
        short_amount = float(object_list[short_idx]["positionAmt"]*-1)

       
        int_cur_short_price = float(object_list[short_idx]["markPrice"])

       
        int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_short_rate : ",round((int_short_rate*100),4))
        print("Mark Price Short: ",int_cur_short_price)
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount >= step_three_unit) and (short_amount < step_four_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount > step_two_unit) and  (short_amount < step_three_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount > step_one_unit) and  (short_amount <= step_two_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount > 0) and  (short_amount <= step_one_unit))):
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit//2)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #ps = []

        return


class CheckLossLongFromIn:

    def __init__(self,market):
        self.market = market


    def check_profit_long_algo(self):
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
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
       
        #long_price  = 7150
        long_price_in = float(object_list_in[long_idx]["entryPrice"])
        long_amount_in = float(object_list_in[long_idx]["positionAmt"])
        short_amount_in = float(object_list_in[short_idx]["positionAmt"]*-1)

       
        #int_cur_long_price_in = float(object_list_in[long_idx]["markPrice"])

        int_cur_long_price_in = str(round(float(object_list_in[long_idx]["markPrice"]),4))

        if long_amount_in > 0:
            #int_long_rate_in = (float(int_cur_long_price_in) - float(long_price_in)) / float(long_price_in) * 20

            plossfirst = str(round(float(object_list_in[long_idx]["entryPrice"])-((0.50*(object_list_in[long_idx]["entryPrice"])/20)*-1),4))

        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
            #print("int_long_rate_in : ",round((int_long_rate_in*100),2))
            #print("Mark Price : ",int_cur_long_price_in)
            if ((float(int_cur_long_price_in) <= float(plossfirst)) and (short_amount_in == 0)):

                take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=str(round(float(reentry_unit),4)))
                PrintBasic.print_obj(take_profit_algo)
                time.sleep(1)


        return



class CheckLossShortFromIn:

    def __init__(self,market):
        self.market = market


    def check_profit_short_algo(self):
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
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
       
        #long_price  = 7150
        short_price_in = float(object_list_in[short_idx]["entryPrice"])
        short_amount_in = float(object_list_in[short_idx]["positionAmt"]*-1)
        long_amount_in = float(object_list_in[long_idx]["positionAmt"])
       


       
        int_cur_short_price_in = float(object_list_out[short_idx]["markPrice"])

        if short_amount_in > 0:
            int_short_rate_in = -1*(float(int_cur_short_price_in) - float(short_price_in)) / float(short_price_in) * 20

        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
            print("int_short_rate_in : ",round((int_short_rate_in*100),2))
            print("Mark Price : ",int_cur_short_price_in)
            if (((int_short_rate_in *100) <= -50) and (long_amount_in == 0)):


                take_profit_algo = request_client_in.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=str(round(float(reentry_unit),4)))

                PrintBasic.print_obj(take_profit_algo)
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
                    #rs1 = s1.find('algo3MSH')
                    #rl1 = s1.find('algo3MLO')

                    # How to use find()
                    if (s1.find('BUY ALGO') != -1):
                        print ("Contains BUY substring ")
                        take_order_buy(self)
                        take_order_sell(self)
                        update_guided("l")
                        time.sleep(1)



                    elif (s1.find('SELL ALGO') != -1):
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
                    #rs1 = s1.find('algo3MSH')
                    #rl1 = s1.find('algo3MLO')

                    # How to use find()
                if (s1.find('BUY ALGO') != -1):
                    print ("Contains BUY  substring ")
                    take_order_buy(self)
                    take_order_sell(self)
                    update_guided("l")
                    time.sleep(1)


                elif (s1.find('SELL ALGO') != -1):
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

    short_amount_in = 0
    short_amount_out = 0
    count_s = 0
    limit_s = 0
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_position()
    #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
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
    long_amount_in = float(object_list[long_idx]["positionAmt"])
    short_amount_in = float(object_list[short_idx]["positionAmt"]*-1)
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]
 
    algo_data = collection_algo.find_one({"market": 'ALGOUSDT'})
    sale_unit = algo_data["sale"]

    step_two_unit = algo_data["step_two_unit"]


    
    count_s = algo_data["count_s"]
    
    limit_s = algo_data["limit_s"]
    reentryunit = str(round(float(algo_data["reentry_unit"]),4))

    if ((short_amount_in == 0) and (short_amount_in <= step_two_unit) and (count_s > limit_s)):
        take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=reentryunit)
        PrintBasic.print_obj(take_profit_algo)
        time.sleep(1)
        #inc_count_s(1)
        cls_count_s(0)
        time.sleep(1)
    elif ((short_amount_in >  0) and (short_amount_in <= step_two_unit) and (count_s > limit_s)):
        take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
        PrintBasic.print_obj(take_profit_algo)
        time.sleep(1)
        #inc_count_s(1)
        cls_count_s(0)
        time.sleep(1)
    # if ((long_amount_in > 0) and (count_s > limit_s)):
    #     take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=long_amount_in)
    #     PrintBasic.print_obj(take_profit_algo)
    #     time.sleep(1)


    return
def take_order_buy(self):
        #price_exit = 0
    #pl = []
    #global stop_threads

    long_amount_in = 0
    long_amount_out = 0
    count_l = 0
    limit_l = 0    
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

    long_amount_in = float(object_list[long_idx]["positionAmt"])
    short_amount_in = float(object_list[short_idx]["positionAmt"]*-1)

    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]
    algo_data = collection_algo.find_one({"market": 'ALGOUSDT'})

    buy_unit = algo_data["buy"]

    step_two_unit = algo_data["step_two_unit"]

    reentryunit = str(round(float(algo_data["reentry_unit"]),4))


    count_l = algo_data["count_l"]
    
    limit_l = algo_data["limit_l"]

    if ((long_amount_in == 0) and (long_amount_in <= step_two_unit) and (count_l > limit_l)):
        take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=reentryunit)
        PrintBasic.print_obj(take_profit_algo)
        time.sleep(1)
        #inc_count_s(1)
        cls_count_l(0)
        time.sleep(1)
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
    elif ((long_amount_in > 0) and (long_amount_in <= step_two_unit) and (count_l > limit_l)):
        take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
        PrintBasic.print_obj(take_profit_algo)
        time.sleep(1)
        #inc_count_s(1)
        cls_count_l(0)
        time.sleep(1)
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
    return


def inc_count_s(count):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]
    #count_s = get_count_s()
    if (count_s <= limit_s):
        count_ss = count_s + count
        collection_algo.update_one({"market": 'ALGOUSDT'},{"$set":{"count_s":count_ss} })
    if (count_s > limit_s+1):
        #count_ss = count_s + count
        collection_algo.update_one({"market": 'ALGOUSDT'},{"$set":{"count_s":0} })

    return

def cls_count_s(count):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]
    collection_algo.update_one({"market": 'ALGOUSDT'},{"$set":{"count_s":count} })

    return
def get_count_l(self):
    #cio_id = 'a8966001117907911480'
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]
    algo_data = collection_algo.find_one({"market": 'ALGOUSDT'})
    return algo_data["count_l"]

def inc_count_l(count):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]
    #count_l = get_count_l()
    if (count_l <= limit_l):
        count_ll = count_l + count
        collection_algo.update_one({"market": 'ALGOUSDT'},{"$set":{"count_l":count_ll} })
    if (count_l > limit_l+1):
        #count_ss = count_s + count
        collection_algo.update_one({"market": 'ALGOUSDT'},{"$set":{"count_l":0} })

    #count_ll = count_l + count
    #collection_algo.update_one({"market": 'ALGOUSDT'},{"$set":{"count_l":count_ll} })
    return

def cls_count_l(count):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]
    collection_algo.update_one({"market": 'ALGOUSDT'},{"$set":{"count_l":count} })
    return
def get_count_s(self):
    #cio_id = 'a8966001117907911480'
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]


    algo_data = collection_algo.find_one({"market": 'ALGOUSDT'})

    return algo_data["count_s"]


class CheckLossLongMore:

    def __init__(self,market):
        self.market = market


    def check_loss_long_algo(self):
            #price_exit = 0
        #pl = []
        global stop_threads
        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()
        #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
        #time.sleep(1)
        object_list = []
        int_long_rate = 0
        reentry = 0
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
       
        #long_price  = 7150
        long_price = str(round(float(object_list[long_idx]["entryPrice"]),2))
        long_amount = float(object_list[long_idx]["positionAmt"])

       
        int_cur_long_price = str(round(float(object_list[long_idx]["markPrice"]),2))

       
        #int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20

        
        plosslast = str(round(float(object_list[long_idx]["entryPrice"])+((-4.00*(object_list[long_idx]["entryPrice"])/20)),4))

 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        #print("int_long_rate : ",round((int_long_rate*100),2))
        #print("Mark Price : ",int_cur_long_price)
        
##        if ((float(int_cur_long_price) <= float(plosslast)) and ((long_amount >=  step_six_unit) and (long_amount < step_seven_unit))):
##            reentry = str(round(float(step_seven_unit - long_amount),2))
##            take_profit_algo = request_client.post_order(symbol="ALGOUSDT",newClientOrderId="long10000" , side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=reentry)
##            PrintBasic.print_obj(take_profit_algo)
##            time.sleep(5)
##            stop_threads = True
##            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])
##
##            #pl = []            
##        if ((float(int_cur_long_price) <= float(plosslast))  and ((long_amount >= step_five_unit) and (long_amount < step_six_unit))):
##            reentry = str(round(float(step_six_unit - long_amount),2))
##            take_profit_algo = request_client.post_order(symbol="ALGOUSDT",newClientOrderId="long10000" , side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=reentry)
##            PrintBasic.print_obj(take_profit_algo)
##            time.sleep(5)
##            stop_threads = True
##            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #pl = []  
        if ((float(int_cur_long_price) <= float(plosslast))  and ((long_amount >= step_three_unit) and (long_amount < step_four_unit))):
            reentry = str(round(float(step_four_unit - long_amount),2))
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT",newClientOrderId="long10000" , side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=reentry)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(5)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #pl = []  
        if ((float(int_cur_long_price) <= float(plosslast))  and ((long_amount > 0) and (long_amount < step_two_unit))):
            reentry = str(round(float(step_two_unit - long_amount),2))
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT",newClientOrderId="long10000" , side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=reentry)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(5)
            stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #pl = []  
        return



class CheckLossShortMore:

    def __init__(self,market):
        self.market = market


    def check_loss_short_algo(self):
            #price_exit = 0
        #ps = []
        global stop_threads
        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        result = request_client.get_position()

        object_list = []
        int_short_rate = 0
        reentrys = 0
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
       
        #long_price  = 7150
        short_price = str(round(float(object_list[short_idx]["entryPrice"]),2))
        short_amount = float(object_list[short_idx]["positionAmt"]*-1)

       
        int_cur_short_price = str(round(float(object_list[short_idx]["markPrice"]),2))

       
        int_short_rate = -1*(float(int_cur_short_price) - float(short_price)) / float(short_price) * 20


 
        #print("long_price:  ",self.long_price +"   "+"int_long_price: ",self.int_cur_long_price +"   "+
         #     "int_long_rate: ",round((self.int_long_rate*100),4))
        print("int_short_rate : ",round((int_short_rate*100),4))
        print("Mark Price Short: ",int_cur_short_price)
##        if (((int_short_rate*100) <= -250) and ((short_amount >= step_six_unit) and (short_amount < step_seven_unit))):
##            reentrys = str(round(float(step_seven_unit = short_amount),2))
##            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=reentrys)
##            PrintBasic.print_obj(take_profit_algo)
##            time.sleep(1)
##            #stop_threads = True
##            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])
##
##            #ps = []
##        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount >= step_five_unit) and  (short_amount < step_six_unit))):
##            reentrys = str(round(float(step_six_unit = short_amount),2))
##            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=reentrys)
##            PrintBasic.print_obj(take_profit_algo)
##            time.sleep(1)
            #stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount >= step_three_unit) and  (short_amount < step_four_unit))):
            reentrys = str(round(float(step_four_unit = short_amount),2))
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=reentrys)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            #stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #ps = []
        if (((int_short_rate*100) >= stop_profit_rate_short_more) and ((short_amount > 0) and  (short_amount < step_two_unit))):
            reentrys = str(round(float(step_two_unit = short_amount),2))
            take_profit_algo = request_client.post_order(symbol="ALGOUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=reentrys)
            PrintBasic.print_obj(take_profit_algo)
            time.sleep(1)
            #stop_threads = True
            #subprocess.call([r'C:\Users\mon\Desktop\Batch_Re\algo_m2End.bat'])

            #ps = []

        return



class TakeProfitDoge:

    def __init__(self,market):
        self.market = market

    def clean_open_order_algo(self):

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
         
        result_open_order = request_client.get_open_orders()
        time.sleep(1)
        object_list_open = []
        #t = 0
        for reso in result_open_order:
            c = collections.defaultdict()
            #c['index'] = t
            c['symbol'] = reso.symbol
            c['orderId'] = reso.orderId
            c['side'] = reso.side
            c['positionSide'] = reso.positionSide
            #d['unRealizedProfit'] = res.unRealizedProfit
            #t = t+1
            object_list_open.append(c)                       

        for key in object_list_open:
            if ((key.get('positionSide') =='LONG') and (key.get('side') == "SELL") and (key.get('symbol') == "ALGOUSDT")):
                marketl = key.get('symbol')
                orderIdl = key.get('orderId')
                result_for_cancel_l = request_client.cancel_order(symbol=marketl, orderId=orderIdl)


        for keys in object_list_open:
            if ((keys.get('positionSide') =='SHORT') and (keys.get('side') == "BUY") and (keys.get('symbol') == "ALGOUSDT")):
                markets = key.get('symbol')
                orderIds = key.get('orderId')
                result_for_cancel_s = request_client.cancel_order(symbol=markets, orderId=orderIds)

        return


    def take_profit_long_algo(self):

        request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
        
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
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ALGOUSDT") and key.get('positionAmt') >= 0.0):
                market = key.get('symbol')
                markPrice = key.get('markPrice')
                entryPriceLong = key.get('entryPrice')
                positionAmtLong = key.get('positionAmt')
                #print(market,'',markPrice,'',entryPriceLong,'',positionAmtLong)
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(entryPriceLong) +((0.03* float(entryPriceLong))/20),4))
                ploss = str(round(float(entryPriceLong) +((-0.40*float(entryPriceLong))/20),4))
                if (Decimal(markPrice) >= Decimal(ploss) and (Decimal(a) > 0)):
                    take_profit_long = request_client.post_order(symbol=market, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                    time.sleep(1)


        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ALGOUSDT") and keys.get('positionAmt') <= 0.0):
                market = keys.get('symbol')
                markPrice = keys.get('markPrice')
                entryPriceShort = keys.get('entryPrice')
                positionAmtShort = keys.get('positionAmt')*-1
                #print(market,'',entryPriceShort,'',positionAmtShort)
                ass = str(round(float(positionAmtShort),3))
                ps = str(round((float(entryPriceShort)-((-0.03* float(entryPriceShort))/20)*-1),4))
                psloss = str(round((float(entryPriceShort)-((0.40*float(entryPriceShort))/20)*-1),4))
                if (Decimal(markPrice) <= Decimal(psloss) and (Decimal(ass) < 0)):
                    ake_profit_short = request_client.post_order(symbol=market, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                    time.sleep(1)


     
        return


if __name__ == '__main__':
    o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    g_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    g_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
 
    client = MongoClient(port=27017)
    db = client.binance
    collection_algo = db["cut_loss"]

    collection_test = db["test"]

   
    index_data = []
    index_data = collection_test.find({"symbol": 'ALGOUSDT'})
    
    long_idx = index_data[1]["index"]
    short_idx = index_data[2]["index"]

    algo_data = collection_algo.find_one({"market": 'ALGOUSDT'})
 
    
    market ='ALGOUSDT'

   
    stop_profit_rate_short = algo_data["mgain_profit_percent_s"]
    stop_profit_rate_long = algo_data["mgain_profit_percent"]
    stop_profit_rate_short_more = algo_data["mgain_profit_percent_s"]
    stop_profit_rate_long_more = algo_data["mgain_profit_percent"]
    min_profit_rate_short = algo_data["fgain_profit_percent_s"]
    min_profit_rate_long = algo_data["fgain_profit_percent"]
    step_two_profit_short = algo_data["lgain_profit_percent_s"]
    step_two_profit_long = algo_data["lgain_profit_percent"]
    stop_loss_rate_long = algo_data["loss_percent"]
    stop_loss_rate_short = algo_data["loss_percent_s"]
    buy_unit = algo_data["buy"]
    sale_unit = algo_data["sale"]
    step_one_unit = algo_data["step_one_unit"]
    step_two_unit = algo_data["step_two_unit"]
    step_three_unit = algo_data["step_three_unit"]
    step_four_unit = algo_data["step_four_unit"]
##    step_five_unit = algo_data["step_five_unit"]
##    step_six_unit = algo_data["step_six_unit"]
##    step_seven_unit = algo_data["step_seven_unit"]
    guided = algo_data["guided"]
    macd = algo_data["macd"]
    count_l = algo_data["count_l"]
    count_s = algo_data["count_s"]
    limit_l = algo_data["limit_l"]
    limit_s = algo_data["limit_s"]
    #interval = algo_data["interval"]
    reentry_unit = algo_data["reentry_unit"]

    try:
        while True:
            client = MongoClient(port=27017)
            db = client.binance
            collection_algo = db["cut_loss"]
            collection_test = db["test"]

           
            index_data = []
            index_data = collection_test.find({"symbol": 'ALGOUSDT'})
            
            long_idx = index_data[1]["index"]
            short_idx = index_data[2]["index"]
            algo_data = collection_algo.find_one({"market": 'ALGOUSDT'})
   
            market ='ALGOUSDT'

           
            stop_profit_rate_short = algo_data["mgain_profit_percent_s"]
            stop_profit_rate_long = algo_data["mgain_profit_percent"]
            stop_profit_rate_short_more = algo_data["mgain_profit_percent_s"]
            stop_profit_rate_long_more = algo_data["mgain_profit_percent"]
            min_profit_rate_short = algo_data["fgain_profit_percent_s"]
            min_profit_rate_long = algo_data["fgain_profit_percent"]
            step_two_profit_short = algo_data["lgain_profit_percent_s"]
            step_two_profit_long = algo_data["lgain_profit_percent"]
            stop_loss_rate_long = algo_data["loss_percent"]
            stop_loss_rate_short = algo_data["loss_percent_s"]
            buy_unit = algo_data["buy"]
            sale_unit = algo_data["sale"]
            step_one_unit = algo_data["step_one_unit"]
            step_two_unit = algo_data["step_two_unit"]
            step_three_unit = algo_data["step_three_unit"]
            step_four_unit = algo_data["step_four_unit"]

            guided = algo_data["guided"]
            macd = algo_data["macd"]
            count_l = algo_data["count_l"]
            count_s = algo_data["count_s"]
            limit_l = algo_data["limit_l"]
            limit_s = algo_data["limit_s"]
            reentry_unit = algo_data["reentry_unit"]
            #interval = algo_data["interval"]
            ps = []
            pl = []
            short_amount =0
            long_amount = 0
            short_amount_in =0
            long_amount_in = 0
            short_amount_out =0
            long_amount_out = 0
            in_long = False
            in_short = False
            stop_threads = False
            request_client_out = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result_out = request_client_out.get_position()
            #algo_account_trade = request_client.get_account_trades(symbol="ALGOUSDT",limit= 1)
            #time.sleep(1)
            object_list_out = []
            for res in result_out:
                d = collections.defaultdict()
                d['symbol'] = res.symbol
                d['positionAmt'] = res.positionAmt
                d['entryPrice'] = res.entryPrice
                d['markPrice'] = res.markPrice
                #d['unRealizedProfit'] = res.unRealizedProfit
                object_list_out.append(d)
                #j = json.dumps(object_list, indent=4)
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


            #print(object_list_out[long_idx]["symbol"]+'  '+str(object_list_out[long_idx]["positionAmt"])+'  '+str(object_list_out[long_idx]["entryPrice"])+'  '+str(object_list_out[long_idx]["markPrice"]))

            print(object_list[long_idx]["symbol"]+'  '+str(object_list[long_idx]["positionAmt"])+'  '+str(object_list[long_idx]["entryPrice"])+'  '+str(object_list[long_idx]["markPrice"]))
            #time.sleep(3)
            #print(object_list_out[short_idx]["symbol"]+'  '+str(object_list_out[short_idx]["positionAmt"])+'  '+str(object_list_out[short_idx]["entryPrice"])+'  '+str(object_list_out[short_idx]["markPrice"]))

            print(object_list[short_idx]["symbol"]+'  '+str(object_list[short_idx]["positionAmt"])+'  '+str(object_list[short_idx]["entryPrice"])+'  '+str(object_list[short_idx]["markPrice"]))
            time.sleep(1)
            short_amount_in = (object_list_out[short_idx]["positionAmt"])*-1
            long_amount_in = (object_list_out[long_idx]["positionAmt"])
            short_amount_in = (object_list_out[short_idx]["positionAmt"])*-1
            long_amount_in = (object_list_out[long_idx]["positionAmt"])
            #if ((long_amount_in == 0) or (short_amount_in ==0)):            
            thread33 = Bin33(33, "Count Candle")
            #thread666 = Bin666(666, "Clean Open Order")
            #thread888 = Bin888(888, "Take Profit")
            thread33.start()
            #time.sleep(3)
            #thread666.start()
            #time.sleep(2)
            #thread888.start()
            #time.sleep(1)
            thread33.join()
            #thread666.join()
            #thread888.join()
            time.sleep(1)


                    
##            if (long_amount_in > 0):
##
##                #long_price = str(round(float(object_list[long_idx]["entryPrice"]),2))
##
##                int_cur_long_price = str(round(float(object_list[long_idx]["markPrice"]),4))
##                
##                #int_long_rate = (float(int_cur_long_price) - float(long_price)) / float(long_price) * 20
##
##                plosslast = str(round(float(object_list[long_idx]["entryPrice"])+((-4.00*(object_list[long_idx]["entryPrice"])/20)),4))
##
##                plossfirst = str(round(float(object_list[long_idx]["entryPrice"])+((-0.70*(object_list[long_idx]["entryPrice"])/20)),4))
##
##                #ploss = str(round(float(object_list[long_idx]["entryPrice"]+((-3.00*object_list[long_idx]["entryPrice"])/20)),2))
##                print("entryPrice",float(object_list[long_idx]["entryPrice"]))
##                #print("plosslast",plosslast)
##                print("plossfirst",plossfirst)
##                print("plosslast",plosslast)
##                #print("ploss",ploss)
##                time.sleep(1)
##                
##                if ((float(int_cur_long_price) >= float(plosslast)) and(float(int_cur_long_price) < float(plossfirst))):
##                    thread13 = Bin13(13,"Check Loss Long More")
##                    #thread8.start()
##                    #thread5.start()
##                    thread13.start()
##                    time.sleep(1)
##                    #thread8.join()
##                    #thread5.join()
##                    thread13.join()
##                    time.sleep(1)
##                elif (float(int_cur_long_price) < float(plosslast)):
##                    #thread8 = Bin8(8, "Check Loss Long algo")
##                    #thread5 = Bin5(5, "Try to Make Order")
##                    thread13 = Bin13(13,"Check Loss Long More")
##                    thread17 = Bin17(17,"Check Loss Long More")
##                    #thread8.start()
##                    #thread5.start()
##                    thread13.start()
##                    thread17.start()
##                    time.sleep(1)
##                    #thread8.join()
##                    #thread5.join()
##                    thread13.join()
##                    thread17.join()

            time.sleep(15)

    except IndexError as error:
        print("Exiting: with error" + "\n")
    except Exception as exception:
        print("Exiting: Exception error" +  "\n")
    else:
        print("Connection Error")
