#!/usr/bin/env python
from binance_d import RequestClient

from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *


from datetime import datetime
from binance.client import Client

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
import json

class take_order_coin_perp:
    
    def __init__(self,markett):
        self.markett = markett
    
    
    def take_order_sell_coin_perp_p(self,markett,c):
        
        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)


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
                psloss = str(round(float(mPrices) +((0.40*float(mPrices))/20),2))
                ##time.sleep()
                ass = str(round(float(positionAmtShort)*-1,0))
                print("ass" ,ass)
                # if (markett=="ADAUSD_PERP"):
                #     f = open ('adausd.json', "r")

                #     data = json.loads(f.read())
                #     res_val = data['ADA']['SHORT'] + data['ADA']['short']
                #     f.close() 
                # elif (markett=="BNBUSD_PERP"):
                #     f = open ('bnbusd.json', "r")

                #     data = json.loads(f.read())
                #     res_val = data['BNB']['SHORT'] + data['BNB']['short']
                #     f.close() 
                # elif (markett=="DOGEUSD_PERP"):
                #     f = open ('dogeusd.json', "r")

                #     data = json.loads(f.read())
                #     res_val = data['DOGE']['SHORT'] + data['DOGE']['short']
                #     f.close() 
                if ((float(ass) <  6)): #and res_val == 11):

                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,  quantity=c)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                return


        return
    def take_order_buy_coin_perp_p(self,markett,c):
        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)

    
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
                a = str(round(float(positionAmtLong),0))
                print("a" ,a)
                # if (markett=="ADAUSD_PERP"):
                #     f = open ('adausd.json', "r")

                #     data = json.loads(f.read())
                #     res_val = data['ADA']['LONG'] + data['ADA']['long']
                #     f.close() 
                # elif (markett=="BNBUSD_PERP"):
                #     f = open ('bnbusd.json', "r")

                #     data = json.loads(f.read())
                #     res_val = data['BNB']['LONG'] + data['BNB']['long']
                #     f.close() 
                # elif (markett=="DOGEUSD_PERP"):
                #     f = open ('dogeusd.json', "r")

                #     data = json.loads(f.read())
                #     res_val = data['DOGE']['LONG'] + data['DOGE']['long']
                #     f.close() 
                if ((float(a) < 6) ):# and res_val == 3):
                
                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG,ordertype=OrderType.MARKET,  quantity=c)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                    return
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
        return


    # def take_order_sell_coin_perp(self,markett):
    #     close_order_buy_coin_perp(self,markett)
    #     o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    #     o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    #     n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    #     n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    #     request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)


    #     result = request_client.get_position()

    #     time.sleep(1)
    #     object_list = []
    #     #i = 0
    #     for res in result:
    #         d = collections.defaultdict()
    #         #d['index'] = i
    #         d['symbol'] = res.symbol
    #         d['positionAmt'] = res.positionAmt
    #         d['entryPrice'] = res.entryPrice
    #         d['markPrice'] = res.markPrice
    #         d['positionSide'] = res.positionSide
    #         #d['unRealizedProfit'] = res.unRealizedProfit
    #     # i = i+1
    #         object_list.append(d)

    #     for key in object_list:
    #         if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
    #             syms = key.get('symbol')
    #             mPrices = key.get('markPrice')
    #             priceIns = key.get('entryPrice')
    #             positionAmtShort = key.get('positionAmt')
    #             print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
    #             psloss = str(round(float(mPrices) +((0.40*float(mPrices))/20),2))
    #             ##time.sleep()
    #             ass = str(round(float(positionAmtShort)*-1,0))
    #             print("ass" ,ass)
    #         # time.sleep(5)
    #             if ((float(ass) >=  0) and (float(ass) < 20)):

    #                 take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=1)
    #                 PrintBasic.print_obj(take_profit_coin)
    #                 time.sleep(1)
    #             return


    #     return
    # def take_order_buy_coin_perp(self,markett):
    #     o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    #     o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    #     n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    #     n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    #     request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)

    
    #     result = request_client.get_position()

    #     time.sleep(1)
    #     object_list = []
    #     #i = 0
    #     for res in result:
    #         d = collections.defaultdict()
    #         #d['index'] = i
    #         d['symbol'] = res.symbol
    #         d['positionAmt'] = res.positionAmt
    #         d['entryPrice'] = res.entryPrice
    #         d['markPrice'] = res.markPrice
    #         d['positionSide'] = res.positionSide
    #         #d['unRealizedProfit'] = res.unRealizedProfit
    #     # i = i+1
    #         object_list.append(d)

    #     for key in object_list:
    #         if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
    #             sym = key.get('symbol')
    #             mPrice = key.get('markPrice')
    #             priceIn = key.get('entryPrice')
    #             positionAmtLong = key.get('positionAmt')
    #             print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
    #             ploss =  str(round(float(mPrice) +((-0.40*float(mPrice))/20),2))
    #             ##time.sleep()
    #             a = str(round(float(positionAmtLong),0))
    #             print("a" ,a)


    #             if ((float(a) >= 0) and (float(a) < 20)):
                
    #                 take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET, quantity=1)
    #                 PrintBasic.print_obj(take_profit_coin)
    #                 time.sleep(1)
    #                 return
    # # if ((short_amount_in > 0) and (count_l > limit_l)):
    # #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
        return
    
    
    def take_order_sell_coin_perp_bnb(self,markett):
        
        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)


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
                psloss = str(round(float(mPrices) +((0.40*float(mPrices))/20),2))
                ##time.sleep()
                ass = str(round(float(positionAmtShort)*-1,0))
                print("ass" ,ass)
            # time.sleep(5)
                if ((float(ass) >=  0) and (float(ass) < 50)):

                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=10)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                return


        return
    def take_order_buy_coin_perp_bnb(self,markett):
        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)

    
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
                ploss =  str(round(float(mPrice) +((-0.40*float(mPrice))/20),2))
                
                ##time.sleep()
                a = str(round(float(positionAmtLong),0))
                print("a" ,a)


                if ((float(a) >= 0) and (float(a) < 50)):
                
                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=10)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                    return
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
        return

    def close_order_sell_coin_perp(self,markett):
        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)

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
                ass = str(round(float(positionAmtShort)*-1,0))
                print("ass" ,ass)



                if (float(ass) >  0) and (float(mPrices) < float(priceIns)):

                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=ass)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                    return


        return
    def close_order_buy_coin_perp(self,markett):
        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)

    
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
                a = str(round(float(positionAmtLong),0))
                print("a" ,a)


                if (float(a) > 0 and (float(mPrice) > float(priceIn))):

                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=a)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                    return

        return

    def take_order_sell_coin_perp(self,markett):
        self.close_order_buy_coin_perp(markett)
        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)


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
                #psloss = str(round(float(mPrices) +((0.40*float(mPrices))/20),2))
                ##time.sleep()
                ass = str(round(float(positionAmtShort)*-1,0))
                print("ass" ,ass)
                if (markett=="ADAUSD_PERP"):
                    f = open ('adausd.json', "r")

                    data = json.loads(f.read())
                    res_val = data['ADA']['SHORT'] + data['ADA']['short']
                    f.close() 
                if ((float(ass) >=  0) and (float(ass) < 20 )): #and res_val == 11)):

                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=1)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                return


        return
    def take_order_buy_coin_perp(self,markett):
        self.close_order_sell_coin_perp(markett)

        o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
        o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
        n_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
        n_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
        request_client = RequestClient(api_key=o_api_key, secret_key=o_secret_key)

    
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
                a = str(round(float(positionAmtLong),0))
                print("a" ,a)
                if (markett=="ADAUSD_PERP"):
                    f = open ('adausd.json', "r")

                    data = json.loads(f.read())
                    res_val = data['ADA']['LONG'] + data['ADA']['long']
                    f.close() 

                if ((float(a) >= 0) and (float(a) < 20)): # and res_val == 3):
                
                    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET, quantity=1)
                    PrintBasic.print_obj(take_profit_coin)
                    time.sleep(1)
                    return
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
        return
