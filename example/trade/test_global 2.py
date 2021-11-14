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
        print("Exiting: 1 " + self.name + "\n")
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

        print("Starting: 33 " + self.name + "\n") 
        b33 = CountCandle(market)
        #b33.take_order_point()
        b33.take_order_point_mon()
        print("Exiting: 33 " + self.name + "\n")
class Bin1(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
   
    def run(self):

        print("Starting: 1 " + self.name + "\n") 
        b1 = test_insert(market)
        #b33.take_order_point()
        b1.test_update()
        print("Exiting: 1 " + self.name + "\n")

class test_insert:
    

    def __init__(self,market):
        self.market = market
    def test_update(self):
        global dark_alpha
        global obv_alpha
        global sweat_alpha
        print("before var inside class dark" ,dark_alpha)
        print("before var inside class obv" ,obv_alpha)
        print("before var inside class sweat" ,sweat_alpha)
        time.sleep(5)
        
        print("########################")
        dark_alpha = '1'
        obv_alpha = '1'
        sweat_alpha = '1'
        print("after var inside class dark" ,dark_alpha)
        print("after var inside class obv" ,obv_alpha)
        print("after var inside class sweat" ,sweat_alpha) 
        time.sleep(5)       
        


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
                    #rs1 = s1.find('alpha3MSH')
                    #rl1 = s1.find('alpha3MLO')

                    # How to use find()
                    if (s1.find('DBA') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ALPHAUSDT"
                        update_dark("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('DSA') != -1):
                        print ("Contains SELL substring ")
                        markett = "ALPHAUSDT"
                        update_dark("0",markett)
                        time.sleep(1)  
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                         
                    elif (s1.find('OBA') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ALPHAUSDT"
                        update_obv("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('OSA') != -1):
                        print ("Contains SELL substring ")
                        markett = "ALPHAUSDT"
                        update_obv("0",markett)
                        time.sleep(1) 
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge() 
                    elif (s1.find('SBA') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ALPHAUSDT"
                        update_sweat("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SSA') != -1):
                        print ("Contains SELL substring ")
                        markett = "ALPHAUSDT"
                        update_sweat("0",markett)
                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('DBS') != -1):
                        print ("Contains BUY  substring ")
                        markett = "SXPUSDT"
                        update_dark("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('DSS') != -1):
                        print ("Contains SELL substring ")
                        markett = "SXPUSDT"
                        update_dark("0",markett)
                        time.sleep(1) 
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge() 
                    elif (s1.find('OBS') != -1):
                        print ("Contains BUY  substring ")
                        markett = "SXPUSDT"
                        update_obv("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('OSS') != -1):
                        print ("Contains SELL substring ")
                        markett = "SXPUSDT"
                        update_obv("0",markett)
                        time.sleep(1)   
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('SBS') != -1):
                        print ("Contains BUY  substring ")
                        markett = "SXPUSDT"
                        update_sweat("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('SSS') != -1):
                        print ("Contains SELL substring ")
                        markett = "SXPUSDT"
                        update_sweat("0",markett)
                        time.sleep(1) 
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()



                    elif (s1.find('DBG') != -1):
                        print ("Contains BUY  substring ")
                        markett = "GRTUSDT"
                        update_dark("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('DSG') != -1):
                        print ("Contains SELL substring ")
                        markett = "GRTUSDT"
                        update_dark("0",markett)
                        time.sleep(1) 
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge() 
                    elif (s1.find('OBG') != -1):
                        print ("Contains BUY  substring ")
                        markett = "GRTUSDT"
                        update_obv("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('OSG') != -1):
                        print ("Contains SELL substring ")
                        markett = "GRTUSDT"
                        update_obv("0",markett)
                        time.sleep(1)   
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SBG') != -1):
                        print ("Contains BUY  substring ")
                        markett = "GRTUSDT"
                        update_sweat("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SSG') != -1):
                        print ("Contains SELL substring ")
                        markett = "GRTUSDT"
                        update_sweat("0",markett)
                        time.sleep(1) 
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('DBD') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ADAUSDT"
                        update_dark("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('DSD') != -1):
                        print ("Contains SELL substring ")
                        markett = "ADAUSDT"
                        update_dark("0",markett)
                        time.sleep(1) 
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge() 
                    elif (s1.find('OBD') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ADAUSDT"
                        update_obv("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('OSD') != -1):
                        print ("Contains SELL substring ")
                        markett = "ADAUSDT"
                        update_obv("0",markett)
                        time.sleep(1)   
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('SBD') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ADAUSDT"
                        update_sweat("1",markett)

                        time.sleep(1)
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SSD') != -1):
                        print ("Contains SELL substring ")
                        markett = "ADAUSDT"
                        update_sweat("0",markett)
                        time.sleep(1) 
                        # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    else:
                        print ("Doesn't contains given substring")
                        time.sleep(1)

                    break
            else:
                #print('To:\t\t', email_message['To'])
                #print('From:\t', email_message['From'])
                print('Subject:', email_message['Subject'])
                s1 = email_message['Subject']
                if (s1.find('DBA') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ALPHAUSDT"
                    update_dark("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSA') != -1):
                    print ("Contains SELL substring ")
                    markett = "ALPHAUSDT"
                    update_dark("0",markett)
                    time.sleep(1)   
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('OBA') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ALPHAUSDT"
                    update_obv("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('OSA') != -1):
                    print ("Contains SELL substring ")
                    markett = "ALPHAUSDT"
                    update_obv("0",markett)
                    time.sleep(1)   
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                   # mail.expunge()
                elif (s1.find('SBA') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ALPHAUSDT"
                    update_sweat("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSA') != -1):
                    print ("Contains SELL substring ")
                    markett = "ALPHAUSDT"
                    update_sweat("0",markett)
                    time.sleep(1) 
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('DBS') != -1):
                    print ("Contains BUY  substring ")
                    markett = "SXPUSDT"
                    update_dark("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSS') != -1):
                    print ("Contains SELL substring ")
                    markett = "SXPUSDT"
                    update_dark("0",markett)
                    time.sleep(1)  
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('OBS') != -1):
                    print ("Contains BUY  substring ")
                    markett = "SXPUSDT"
                    update_obv("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                   # mail.expunge()
                elif (s1.find('OSS') != -1):
                    print ("Contains SELL substring ")
                    markett = "SXPUSDT"
                    update_obv("0",markett)
                    time.sleep(1)   
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SBS') != -1):
                    print ("Contains BUY  substring ")
                    markett = "SXPUSDT"
                    update_sweat("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                   # mail.expunge()
                elif (s1.find('SSS') != -1):
                    print ("Contains SELL substring ")
                    markett = "SXPUSDT"
                    update_sweat("0",markett)
                    time.sleep(1) 
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DBG') != -1):
                    print ("Contains BUY  substring ")
                    markett = "GRTUSDT"
                    update_dark("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSG') != -1):
                    print ("Contains SELL substring ")
                    markett = "GRTUSDT"
                    update_dark("0",markett)
                    time.sleep(1) 
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('OBG') != -1):
                    print ("Contains BUY  substring ")
                    markett = "GRTUSDT"
                    update_obv("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                   # mail.expunge()
                elif (s1.find('OSG') != -1):
                    print ("Contains SELL substring ")
                    markett = "GRTUSDT"
                    update_obv("0",markett)
                    time.sleep(1)   
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                   # mail.expunge()
                elif (s1.find('SBG') != -1):
                    print ("Contains BUY  substring ")
                    markett = "GRTUSDT"
                    update_sweat("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSG') != -1):
                    print ("Contains SELL substring ")
                    markett = "GRTUSDT"
                    update_sweat("0",markett)
                    time.sleep(1) 
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()



                elif (s1.find('DBD') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ADAUSDT"
                    update_dark("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSD') != -1):
                    print ("Contains SELL substring ")
                    markett = "ADAUSDT"
                    update_dark("0",markett)
                    time.sleep(1) 
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('OBD') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ADAUSDT"
                    update_obv("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                   # mail.expunge()
                elif (s1.find('OSD') != -1):
                    print ("Contains SELL substring ")
                    markett = "ADAUSDT"
                    update_obv("0",markett)
                    time.sleep(1)   
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                   # mail.expunge()
                elif (s1.find('SBD') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ADAUSDT"
                    update_sweat("1",markett)

                    time.sleep(1)
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSD') != -1):
                    print ("Contains SELL substring ")
                    markett = "ADAUSDT"
                    update_sweat("0",markett)
                    time.sleep(1) 
                    # mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                else:
                    print ("Doesn't contains given substring")
                    #take_order_buy()
                    time.sleep(1)


        except IndexError:
            print("No new email")
        return
def update_dark(d,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_alpha = db["count"]
    collection_alpha.update_one({"market": markett},{"$set":{"dark":d} })
def update_obv(o,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_alpha = db["count"]
    collection_alpha.update_one({"market": markett},{"$set":{"obv":o} })
def update_sweat(s,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient(port=27017)
    db = client.binance
    collection_alpha = db["count"]
    collection_alpha.update_one({"market": markett},{"$set":{"sweat":s} })
class CountCandle:
    Down = False
    Up = False
    def __init__(self,market):
        self.market = market
    def take_order_point(self):

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
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ALPHAUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.055* float(priceIn))/20),5))
                pl = str(round(float(priceIn) -((0.10* float(priceIn))/20),5))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
        
                if (float(positionAmtLong) == 0):
        
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')
                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')
                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')
                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ALPHAUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.055* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.10* float(priceIns))/20),5))



                if (float(positionAmtShort) == 0):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ALPHAUSDT')
                        update_dark("2",'ALPHAUSDT')
                        update_sweat("2",'ALPHAUSDT')

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "SXPUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.055* float(priceIn))/20),4))
                pl = str(round(float(priceIn) -((0.10* float(priceIn))/20),4))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
            
                if (float(positionAmtLong) == 0):
        
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_sxp = db["count"]
                    sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    dark = sxp_data["dark"]
                    obv = sxp_data["obv"]
                    sweat = sxp_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "SXPUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                ass = str(round(float(positionAmtShort),3))
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.055* float(priceIns))/20),4))
                pss = str(round(float(priceIns) +((0.10* float(priceIns))/20),4))

                if (float(positionAmtShort) == 0):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_sxp = db["count"]

                    sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    dark = sxp_data["dark"]
                    obv = sxp_data["obv"]
                    sweat = sxp_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
                elif ( float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'SXPUSDT')
                        update_dark("2",'SXPUSDT')
                        update_sweat("2",'SXPUSDT')

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "GRTUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.055* float(priceIn))/20),5))
                pl = str(round(float(priceIn) -((0.10* float(priceIn))/20),5))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
            
                if (float(positionAmtLong) == 0):
        
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_sxp = db["count"]
                    sxp_data = collection_sxp.find_one({"market": 'GRTUSDT'})   
                    dark = sxp_data["dark"]
                    obv = sxp_data["obv"]
                    sweat = sxp_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "GRTUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                ass = str(round(float(positionAmtShort),3))
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.055* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.10* float(priceIns))/20),5))

                if (float(positionAmtShort) == 0):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_sxp = db["count"]

                    sxp_data = collection_sxp.find_one({"market": 'GRTUSDT'})   
                    dark = sxp_data["dark"]
                    obv = sxp_data["obv"]
                    sweat = sxp_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'GRTUSDT')
                        update_dark("2",'GRTUSDT')
                        update_sweat("2",'GRTUSDT')

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ADAUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.055* float(priceIn))/20),5))
                pl = str(round(float(priceIn) -((0.10* float(priceIn))/20),5))
                ploss =  str(round(float(priceIn) +((-0.20*float(priceIn))/20),3))
                plost =  str(round(float(priceIn) +((-1.00*float(priceIn))/20),3))
        
                if (float(positionAmtLong) == 0):
        
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]
                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="1" and obv =="1" and sweat =="1")):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ADAUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.055* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.10* float(priceIns))/20),5))



                if (float(positionAmtShort) == 0):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((float(dark)+float(obv)+float(sweat)) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    client = MongoClient(port=27017)
                    db = client.binance
                    collection_alpha = db["count"]

                    alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    dark = alpha_data["dark"]
                    obv = alpha_data["obv"]
                    sweat = alpha_data["sweat"]
                    if ((dark =="0" and obv =="0" and sweat =="0")):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(2)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        update_obv("2",'ADAUSDT')
                        update_dark("2",'ADAUSDT')
                        update_sweat("2",'ADAUSDT')

                        time.sleep(1)
        return


def take_order_sell(self):

    short_amount_in = 0
    #short_amount_out = 0
    count_s = 0
    limit_s = 0
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_position()
    #alpha_account_trade = request_client.get_account_trades(symbol="ALPHAUSDT",limit= 1)
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
    #long_amount_in = float(object_list[long_idx]["positionAmt"])
    short_amount_in = float(object_list[short_idx]["positionAmt"]*-1)
    client = MongoClient(port=27017)
    db = client.binance
    collection_alpha = db["cut_loss"]
 
    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})
    sale_unit = alpha_data["sale"]

    step_two_unit = alpha_data["step_two_unit"]


    
    count_s = alpha_data["count_s"]
    
    limit_s = alpha_data["limit_s"]

    limit_ss = alpha_data["limit_ss"]

    count_ss = alpha_data["count_ss"]
    protect_profit_s = alpha_data["protect_profit_s"]

    reentryunit = str(round(float(alpha_data["reentry_unit"]),3))

    if ((short_amount_in == 0) and (short_amount_in <= step_two_unit) and (protect_profit_s ==1)):

        take_profit_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=reentryunit)
        PrintBasic.print_obj(take_profit_alpha)
        time.sleep(1)

        time.sleep(1)
    elif ((short_amount_in >  0) and (short_amount_in <= step_two_unit) and (count_ss < limit_ss) and (count_s > limit_s)):

        take_profit_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=sale_unit)
        PrintBasic.print_obj(take_profit_alpha)
        time.sleep(1)

        time.sleep(1)

    return
def take_order_buy(self):

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
    collection_alpha = db["cut_loss"]
    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})

    buy_unit = alpha_data["buy"]

    step_two_unit = alpha_data["step_two_unit"]

    reentryunit = str(round(float(alpha_data["reentry_unit"]),3))


    count_l = alpha_data["count_l"]
    
    limit_l = alpha_data["limit_l"]

    limit_ll = alpha_data["limit_ll"]

    count_ll = alpha_data["count_ll"]
    protect_profit = alpha_data["protect_profit"]

    if ((long_amount_in == 0) and (long_amount_in <= step_two_unit) and (protect_profit == 1 )):

                
        take_profit_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=reentryunit)
        PrintBasic.print_obj(take_profit_alpha)
        time.sleep(1)

        time.sleep(1)
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
    elif ((long_amount_in > 0) and (long_amount_in <= step_two_unit) and (count_ll <= limit_ll) and (count_l > limit_l)):

        take_profit_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
        PrintBasic.print_obj(take_profit_alpha)
        time.sleep(1)

        time.sleep(1)
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
    return

if __name__ == '__main__':

    o_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    o_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    g_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    g_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'

    dark_alpha = '2'
    obv_alpha = '2'
    sweat_alpha = '2'
    market = 'ALPHAUSDT'
    
    
    
    
    try:
        while True:
            print("before out_side thread dark",dark_alpha)
            print("before out_side thread obv",obv_alpha)
            print("before out_side thread sweat",sweat_alpha)
            time.sleep(5)
            #thread1 = OkEx1(1,"get mail 1")
            #thread2 = Bin33(2,"Count Candle")
            thread3 = Bin1(1,"test global")
            #thread1.start()
            #thread2.start()
            thread3.start()
           # thread1.join()
            #thread2.join()
            thread3.join()
            print("after out_side thread dark",dark_alpha)
            print("after out_side thread obv",obv_alpha)
            print("after out_side thread sweat",sweat_alpha)   
                     
            
            time.sleep(5)
    except IndexError as error:
        print("Exiting: with error" + "\n")
    except Exception as exception:
        print("Exiting: Exception error" +  "\n")
    else:
        print("Connection Error")
