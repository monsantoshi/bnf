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

        print("Starting: 333 " + self.name + "\n") 
        b33 = CountCandle(market)
        #b33.take_order_point()
        b33.take_order_point_new()
        print("Exiting: 333 " + self.name + "\n")
class getmail:

    def __init__(self,market):
        self.market = market
   


    def two_way_email(self,server,uname,pwd):
        username = uname
        password = pwd
        mail = imaplib.IMAP4_SSL(server)
        mail.login(username, password)
        mail.select("inbox")
        global dark_alpha
        global obv_alpha
        global sweat_alpha
        global dark_ada
        global obv_ada
        global sweat_ada
        global dark_sxp
        global obv_sxp
        global sweat_sxp
        global dark_grt
        global obv_grt
        global sweat_grt
        global sweat_bnb
        global dark_bnb
        global obv_bnb
        global sweat_eth
        global dark_eth
        global obv_eth
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
                        update_dark(1,markett)
                        dark_alpha=1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()
                    elif (s1.find('DSA') != -1):
                        print ("Contains SELL substring ")
                        markett = "ALPHAUSDT"
                        update_dark(0,markett)
                        dark_alpha = 0
                        #time.sleep(1)  
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                         
                    elif (s1.find('OBA') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ALPHAUSDT"
                        update_obv(1,markett)
                        obv_alpha = 1

                       # time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('OSA') != -1):
                        print ("Contains SELL substring ")
                        markett = "ALPHAUSDT"
                        update_obv(0,markett)
                        obv_alpha = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge() 
                    elif (s1.find('SBA') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ALPHAUSDT"
                        update_sweat(1,markett)
                        sweat_alpha = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SSA') != -1):
                        print ("Contains SELL substring ")
                        markett = "ALPHAUSDT"
                        update_sweat(0,markett)
                        sweat_alpha = 0
                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()
                    elif (s1.find('DBS') != -1):
                        print ("Contains BUY  substring ")
                        markett = "SXPUSDT"
                        update_dark(1,markett)
                        dark_sxp =  1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('DSS') != -1):
                        print ("Contains SELL substring ")
                        markett = "SXPUSDT"
                        update_dark(0,markett)
                        dark_sxp = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge() 
                    elif (s1.find('OBS') != -1):
                        print ("Contains BUY  substring ")
                        markett = "SXPUSDT"
                        update_obv(1,markett)
                        obv_sxp = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()
                    elif (s1.find('OSS') != -1):
                        print ("Contains SELL substring ")
                        markett = "SXPUSDT"
                        update_obv(0,markett)
                        obv_sxp = 0
                        #time.sleep(1)   
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('SBS') != -1):
                        print ("Contains BUY  substring ")
                        markett = "SXPUSDT"
                        update_sweat(1,markett)
                        sweat_sxp = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('SSS') != -1):
                        print ("Contains SELL substring ")
                        markett = "SXPUSDT"
                        update_sweat(0,markett)
                        sweat_sxp = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()



                    elif (s1.find('DBG') != -1):
                        print ("Contains BUY  substring ")
                        markett = "GRTUSDT"
                        update_dark(1,markett)
                        dark_grt = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('DSG') != -1):
                        print ("Contains SELL substring ")
                        markett = "GRTUSDT"
                        update_dark(0,markett)
                        dark_grt = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge() 
                    elif (s1.find('OBG') != -1):
                        print ("Contains BUY  substring ")
                        markett = "GRTUSDT"
                        update_obv(1,markett)
                        obv_grt = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                       # mail.expunge()
                    elif (s1.find('OSG') != -1):
                        print ("Contains SELL substring ")
                        markett = "GRTUSDT"
                        update_obv(0,markett)
                        obv_grt = 0
                        #time.sleep(1)   
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()
                    elif (s1.find('SBG') != -1):
                        print ("Contains BUY  substring ")
                        markett = "GRTUSDT"
                        update_sweat(1,markett)
                        sweat_grt = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SSG') != -1):
                        print ("Contains SELL substring ")
                        markett = "GRTUSDT"
                        update_sweat(0,markett)
                        sweat_grt = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()
                    elif (s1.find('DBD') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ADAUSDT"
                        update_dark(1,markett)
                        dark_ada =1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()
                    elif (s1.find('DSD') != -1):
                        print ("Contains SELL substring ")
                        markett = "ADAUSDT"
                        update_dark(0,markett)
                        dark_ada = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge() 
                    elif (s1.find('OBD') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ADAUSDT"
                        update_obv(1,markett)
                        obv_ada = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('OSD') != -1):
                        print ("Contains SELL substring ")
                        markett = "ADAUSDT"
                        update_obv(0,markett)
                        obv_ada = 0
                        #time.sleep(1)   
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('SBD') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ADAUSDT"
                        update_sweat(1,markett)
                        sweat_ada = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SSD') != -1):
                        print ("Contains SELL substring ")
                        markett = "ADAUSDT"
                        update_sweat(0,markett)
                        sweat_ada = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('DBB') != -1):
                        print ("Contains BUY  substring ")
                        markett = "BNBUSDT"
                        update_dark(1,markett)
                        update_dark(1,'BNBUSD_PERP')
                        dark_bnb =1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('DSB') != -1):
                        print ("Contains SELL substring ")
                        markett = "BNBUSDT"
                        update_dark(0,markett)
                        update_dark(0,'BNBUSD_PERP')
                        dark_bnb = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge() 
                    elif (s1.find('OBB') != -1):
                        print ("Contains BUY  substring ")
                        markett = "BNBUSDT"
                        update_obv(1,markett)
                        update_obv(1,'BNBUSD_PERP')
                        obv_bnb = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('OSB') != -1):
                        print ("Contains SELL substring ")
                        markett = "BNBUSDT"
                        update_obv(0,markett)
                        update_obv(0,'BNBUSD_PERP')
                        obv_bnb = 0
                        #time.sleep(1)   
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('SBB') != -1):
                        print ("Contains BUY  substring ")
                        markett = "BNBUSDT"
                        update_sweat(1,markett)
                        sweat_bnb = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('SSB') != -1):
                        print ("Contains SELL substring ")
                        markett = "BNBUSDT"
                        update_sweat(0,markett)
                        sweat_bnb = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('DBE') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ETHUSDT"
                        update_dark(1,markett)
                        dark_eth =1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    elif (s1.find('DSE') != -1):
                        print ("Contains SELL substring ")
                        markett = "ETHUSDT"
                        update_dark(0,markett)
                        dark_eth = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge() 
                    elif (s1.find('OBE') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ETHUSDT"
                        update_obv(1,markett)
                        obv_eth = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('OSE') != -1):
                        print ("Contains SELL substring ")
                        markett = "ETHUSDT"
                        update_obv(0,markett)
                        obv_eth = 0
                        #time.sleep(1)   
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                    # mail.expunge()
                    elif (s1.find('SBE') != -1):
                        print ("Contains BUY  substring ")
                        markett = "ETHUSDT"
                        update_sweat(1,markett)
                        sweat_eth = 1

                        #time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        mail.expunge()
                    elif (s1.find('SSE') != -1):
                        print ("Contains SELL substring ")
                        markett = "ETHUSDT"
                        update_sweat(0,markett)
                        sweat_eth = 0
                        #time.sleep(1) 
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                                # Expunge after marking emails deleted
                        #mail.expunge()
                    else:
                        print ("Doesn't contains given substring")
                        #time.sleep(1)

                    break
            else:
                #print('To:\t\t', email_message['To'])
                #print('From:\t', email_message['From'])
                print('Subject:', email_message['Subject'])
                s1 = email_message['Subject']
                if (s1.find('DBA') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ALPHAUSDT"
                    update_dark(1,markett)
                    dark_alpha=1

                    time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSA') != -1):
                    print ("Contains SELL substring ")
                    markett = "ALPHAUSDT"
                    update_dark(0,markett)
                    dark_alpha = 0
                    #time.sleep(1)  
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                        
                elif (s1.find('OBA') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ALPHAUSDT"
                    update_obv(1,markett)
                    obv_alpha = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('OSA') != -1):
                    print ("Contains SELL substring ")
                    markett = "ALPHAUSDT"
                    update_obv(0,markett)
                    obv_alpha = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('SBA') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ALPHAUSDT"
                    update_sweat(1,markett)
                    sweat_alpha = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSA') != -1):
                    print ("Contains SELL substring ")
                    markett = "ALPHAUSDT"
                    update_sweat(0,markett)
                    sweat_alpha = 0
                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('DBS') != -1):
                    print ("Contains BUY  substring ")
                    markett = "SXPUSDT"
                    update_dark(1,markett)
                    dark_sxp =  1

                   # time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('DSS') != -1):
                    print ("Contains SELL substring ")
                    markett = "SXPUSDT"
                    update_dark(0,markett)
                    dark_sxp = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('OBS') != -1):
                    print ("Contains BUY  substring ")
                    markett = "SXPUSDT"
                    update_obv(1,markett)
                    obv_sxp = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('OSS') != -1):
                    print ("Contains SELL substring ")
                    markett = "SXPUSDT"
                    update_obv(0,markett)
                    obv_sxp = 0
                   # time.sleep(1)   
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('SBS') != -1):
                    print ("Contains BUY  substring ")
                    markett = "SXPUSDT"
                    update_sweat(1,markett)
                    sweat_sxp = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('SSS') != -1):
                    print ("Contains SELL substring ")
                    markett = "SXPUSDT"
                    update_sweat(0,markett)
                    sweat_sxp = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('DBG') != -1):
                    print ("Contains BUY  substring ")
                    markett = "GRTUSDT"
                    update_dark(1,markett)
                    dark_grt = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('DSG') != -1):
                    print ("Contains SELL substring ")
                    markett = "GRTUSDT"
                    update_dark(0,markett)
                    dark_grt = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge() 
                elif (s1.find('OBG') != -1):
                    print ("Contains BUY  substring ")
                    markett = "GRTUSDT"
                    update_obv(1,markett)
                    obv_grt = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    # mail.expunge()
                elif (s1.find('OSG') != -1):
                    print ("Contains SELL substring ")
                    markett = "GRTUSDT"
                    update_obv(0,markett)
                    obv_grt = 0
                    #time.sleep(1)   
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SBG') != -1):
                    print ("Contains BUY  substring ")
                    markett = "GRTUSDT"
                    update_sweat(1,markett)
                    sweat_grt = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSG') != -1):
                    print ("Contains SELL substring ")
                    markett = "GRTUSDT"
                    update_sweat(0,markett)
                    sweat_grt = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DBD') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ADAUSDT"
                    update_dark(1,markett)
                    dark_ada =1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSD') != -1):
                    print ("Contains SELL substring ")
                    markett = "ADAUSDT"
                    update_dark(0,markett)
                    dark_ada = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('OBD') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ADAUSDT"
                    update_obv(1,markett)
                    obv_ada = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                # mail.expunge()
                elif (s1.find('OSD') != -1):
                    print ("Contains SELL substring ")
                    markett = "ADAUSDT"
                    update_obv(0,markett)
                    obv_ada = 0
                    #time.sleep(1)   
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                # mail.expunge()
                elif (s1.find('SBD') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ADAUSDT"
                    update_sweat(1,markett)
                    sweat_ada = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSD') != -1):
                    print ("Contains SELL substring ")
                    markett = "ADAUSDT"
                    update_sweat(0,markett)
                    sweat_ada = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DBB') != -1):
                    print ("Contains BUY  substring ")
                    markett = "BNBUSDT"
                    update_dark(1,markett)
                    dark_bnb =1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSB') != -1):
                    print ("Contains SELL substring ")
                    markett = "BNBUSDT"
                    update_dark(0,markett)
                    dark_bnb = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('OBB') != -1):
                    print ("Contains BUY  substring ")
                    markett = "BNBUSDT"
                    update_obv(1,markett)
                    obv_bnb = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                # mail.expunge()
                elif (s1.find('OSB') != -1):
                    print ("Contains SELL substring ")
                    markett = "BNBUSDT"
                    update_obv(0,markett)
                    obv_bnb = 0
                    #time.sleep(1)   
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                # mail.expunge()
                elif (s1.find('SBB') != -1):
                    print ("Contains BUY  substring ")
                    markett = "BNBUSDT"
                    update_sweat(1,markett)
                    sweat_bnb = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSB') != -1):
                    print ("Contains SELL substring ")
                    markett = "BNBUSDT"
                    update_sweat(0,markett)
                    sweat_bnb = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DBE') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ETHUSDT"
                    update_dark(1,markett)
                    dark_eth =1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('DSE') != -1):
                    print ("Contains SELL substring ")
                    markett = "ETHUSDT"
                    update_dark(0,markett)
                    dark_eth = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge() 
                elif (s1.find('OBE') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ETHUSDT"
                    update_obv(1,markett)
                    obv_eth = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                # mail.expunge()
                elif (s1.find('OSE') != -1):
                    print ("Contains SELL substring ")
                    markett = "ETHUSDT"
                    update_obv(0,markett)
                    obv_eth = 0
                    #time.sleep(1)   
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                # mail.expunge()
                elif (s1.find('SBE') != -1):
                    print ("Contains BUY  substring ")
                    markett = "ETHUSDT"
                    update_sweat(1,markett)
                    sweat_eth = 1

                    #time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                            # Expunge after marking emails deleted
                    #mail.expunge()
                elif (s1.find('SSE') != -1):
                    print ("Contains SELL substring ")
                    markett = "ETHUSDT"
                    update_sweat(0,markett)
                    sweat_eth = 0
                    #time.sleep(1) 
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
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
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_alpha = db["count"]
    collection_alpha.update_one({"market": markett},{"$set":{"dark":d} })
def update_obv(o,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_alpha = db["count"]
    collection_alpha.update_one({"market": markett},{"$set":{"obv":o} })
def update_sweat(s,markett):
    #cio_id = 'a8966001117907911480'
    #state = int(order_type)
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_alpha = db["count"]
    collection_alpha.update_one({"market": markett},{"$set":{"sweat":s} })
class CountCandle:
    Down = False
    Up = False
    def __init__(self,market):
        self.market = market
    def take_order_point(self):
        global dark_alpha
        global obv_alpha
        global sweat_alpha
        global dark_ada
        global obv_ada
        global sweat_ada
        global dark_sxp
        global obv_sxp
        global sweat_sxp
        global dark_grt
        global obv_grt
        global sweat_grt
        global dark_bnb
        global obv_bnb
        global sweat_bnb
        global dark_eth
        global obv_eth
        global sweat_eth

        client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")
        db = client.Binance
        collection_cound = db["count"]
        sxp_c_data = collection_cound.find_one({"market": 'SXPUSDT'})
        ada_c_data = collection_cound.find_one({"market": 'ADAUSDT'})
        alpha_c_data = collection_cound.find_one({"market": 'ALPHAUSDT'})
        grt_c_data = collection_cound.find_one({"market": 'GRTUSDT'})
        bnb_c_data = collection_cound.find_one({"market": 'BNBUSDT'})
        eth_c_data = collection_cound.find_one({"market": 'ETHUSDT'})
        #bnbu_c_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})
        dark_alpha = alpha_c_data["dark"]
        obv_alpha = alpha_c_data["obv"]
        sweat_alpha = alpha_c_data["sweat"]
        dark_ada = ada_c_data["dark"]
        obv_ada = ada_c_data["obv"]
        sweat_ada = ada_c_data["sweat"]
        dark_grt = grt_c_data["dark"]
        obv_grt = grt_c_data["obv"]
        sweat_grt = grt_c_data["sweat"]
        dark_sxp = sxp_c_data["dark"]
        obv_sxp = sxp_c_data["obv"]
        sweat_sxp = sxp_c_data["sweat"]
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
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ALPHAUSDT")):
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
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_alpha ==1 and obv_alpha ==1 and sweat_alpha ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_alpha+obv_alpha+sweat_alpha) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2
                        time.sleep(1)
                    elif ((dark_alpha+obv_alpha+sweat_alpha) ==3 and (float(a) < float(step_two_unit))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_alpha ==1 and obv_alpha ==1 and sweat_alpha ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_alpha ==1 and obv_alpha ==1 and sweat_alpha ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2
                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ALPHAUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))



                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_alpha ==0 and obv_alpha ==0 and sweat_alpha ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_alpha+obv_alpha+sweat_alpha) > 0 and (dark_alpha+obv_alpha+sweat_alpha) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2

                        time.sleep(1)
                    elif ((dark_alpha+obv_alpha+sweat_alpha) == 0 and (float(ass) < float(step_two_unit))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_alpha ==0 and obv_alpha ==0 and sweat_alpha ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_alpha ==0 and obv_alpha ==0 and sweat_alpha ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ALPHAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_alpha = 2
                        # obv_alpha = 2
                        # sweat_alpha = 2

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "SXPUSDT")):
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
                    # collection_sxp = db["count"]
                    # sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_sxp ==1 and obv_sxp ==1 and sweat_sxp ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_sxp+obv_sxp+sweat_sxp) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                    elif ((dark_sxp+obv_sxp+sweat_sxp) ==3 and (float(a) < float(step_two_unit))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_sxp ==1 and obv_sxp ==1 and sweat_sxp ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_sxp ==1 and obv_sxp ==1 and sweat_sxp ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "SXPUSDT")):

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
                    # collection_sxp = db["count"]

                    # sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_sxp ==0 and obv_sxp ==0 and sweat_sxp ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ( (dark_sxp+obv_sxp+sweat_sxp) > 0 and (dark_sxp+obv_sxp+sweat_sxp) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                    elif ( (dark_sxp+obv_sxp+sweat_sxp) ==0 and (float(ass) < float(step_two_unit))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_sxp ==0 and obv_sxp ==0 and sweat_sxp ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
                elif ( float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_sxp ==0 and obv_sxp ==0 and sweat_sxp ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="SXPUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_sxp = 2
                        # obv_sxp = 2
                        # sweat_sxp = 2

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "GRTUSDT")):
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
                    # collection_sxp = db["count"]
                    # sxp_data = collection_sxp.find_one({"market": 'GRTUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_grt ==1 and obv_grt ==1 and sweat_grt ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_grt+ obv_grt+sweat_grt) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)                    
                    elif ((dark_grt+ obv_grt+sweat_grt) ==3 and (float(a) < float(step_two_unit))):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_grt ==1 and obv_grt ==1 and sweat_grt ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_grt ==1 and obv_grt ==1 and sweat_grt ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "GRTUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                ass = str(round(float(positionAmtShort),3))
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))

                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_sxp = db["count"]

                    # sxp_data = collection_sxp.find_one({"market": 'GRTUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_grt ==0 and obv_grt ==0 and sweat_grt ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_grt+ obv_grt+sweat_grt) > 0 and (dark_grt+ obv_grt+sweat_grt) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
                    elif ((dark_grt+ obv_grt+sweat_grt) == 0 and (float(ass) < float(step_two_unit))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unit)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_grt ==0 and obv_grt ==0 and sweat_grt ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'GRTUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_grt ==0 and obv_grt ==0 and sweat_grt ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="GRTUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_grt = 2
                        # obv_grt = 2
                        # sweat_grt = 2

                        time.sleep(1)
        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "ADAUSDT")):
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
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_ada ==1 and obv_ada ==1 and sweat_ada ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ( (dark_ada+ obv_ada+sweat_ada) <3):
                    
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                    elif ( (dark_ada+ obv_ada+sweat_ada) ==3 and (float(a) < float(step_two_unit))):
                        
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_ada ==1 and obv_ada ==1 and sweat_ada ==1)):

                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unit)) and (float(positionAmtLong) < float(step_three_unit)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_ada ==1 and obv_ada ==1 and sweat_ada ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unit)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "ADAUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),5))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),5))



                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_ada ==0 and obv_ada ==0 and sweat_ada ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_ada+ obv_ada+sweat_ada) > 0 and (dark_ada+ obv_ada+sweat_ada) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                    elif ((dark_ada+ obv_ada+sweat_ada) == 0 and (float(ass) < float(step_two_unit))):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_ada ==0 and obv_ada ==0 and sweat_ada ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unit) and float(positionAmtShort) < float(step_three_unit) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ADAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_ada ==0 and obv_ada ==0 and sweat_ada ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ADAUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unit)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ADAUSDT')
                        # update_dark("2",'ADAUSDT')
                        # update_sweat("2",'ADAUSDT')
                        # dark_ada = 2
                        # obv_ada = 2
                        # sweat_ada = 2

                        time.sleep(1)


        # for key in object_list:
        #     if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BNBUSDT")):
        #         positionAmtLong = key.get('positionAmt')
        #         priceIn = key.get('entryPrice')
        #         mPrice = key.get('markPrice')
        #         a = str(round(float(positionAmtLong),3))
        #         p = str(round(float(priceIn) +((0.045* float(priceIn))/20),2))
        #         pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),2))
        #         if (float(positionAmtLong) == 0):
        
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]
        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]
        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_bnb+obv_bnb+sweat_bnb) <3):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        #             elif ((dark_bnb+obv_bnb+sweat_bnb) ==3 and (float(a) < float(step_two_unite))):
        #                 Up = False
        #                 Down = True
        #                 print("TP_LONG",True)
        #                 time.sleep(1)
        #                 print("take_profit_long")
        #                 take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=buy_unite)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb= 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unite)) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]
        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        #         elif ((float(positionAmtLong) >= float(step_two_unite)) and (float(positionAmtLong) < float(step_three_unite)) and  (float(mPrice) <= float(pl))):
                    
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]
        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((dark =="1" and obv =="1" and sweat =="1")):
        #             if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
        #                 Up = True
        #                 Down = False
        #                 print("Up",Up)
        #                 time.sleep(1)
        #                 print("take_order_long_full")
        #                 take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
        #                 PrintBasic.print_obj(take_order_long)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2
        #                 time.sleep(1)
        # for keys in object_list:
        #     if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BNBUSDT")):

        #         positionAmtShort = keys.get('positionAmt')*-1
        #         mPrices = keys.get('markPrice')
        #         priceIns = keys.get('entryPrice')
        #         ass = str(round(float(positionAmtShort),3))
        #         ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),2))
        #         pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),2))
        #         if (float(positionAmtShort) == 0):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]

        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]

        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((float(dark)+float(obv)+float(sweat)) <3):
        #             if ((dark_bnb+obv_bnb+sweat_bnb) > 0 and (dark_bnb+obv_bnb+sweat_bnb) <3):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #             elif ((dark_bnb+obv_bnb+sweat_bnb) == 0 and (float(ass) < float(step_two_unite))):
        #                 Down = False
        #                 Up = True

        #                 print("TP_SHORT ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=sale_unite)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unite) and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]

        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        #         elif (float(positionAmtShort) >= float(step_two_unite) and float(positionAmtShort) < float(step_three_unite) and (float(mPrices) >= float(pss))):
        #             # client = MongoClient(port=27017)
        #             # db = client.binance
        #             # collection_alpha = db["count"]

        #             # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
        #             # dark = alpha_data["dark"]
        #             # obv = alpha_data["obv"]
        #             # sweat = alpha_data["sweat"]
        #             # if ((dark =="0" and obv =="0" and sweat =="0")):
        #             if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
        #                 Down = True
        #                 Up = False

        #                 print("Down ",Down)
        #                 time.sleep(1)
                
        #                 print("take_order_short_full")

        #                 take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
        #                 PrintBasic.print_obj(take_order_short)
        #                 # update_obv("2",'ALPHAUSDT')
        #                 # update_dark("2",'ALPHAUSDT')
        #                 # update_sweat("2",'ALPHAUSDT')
        #                 # dark_bnb = 2
        #                 # obv_bnb = 2
        #                 # sweat_bnb = 2

        #                 time.sleep(1)
        
        
        
        
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
                    # collection_sxp = db["count"]
                    # sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_eth+obv_eth+sweat_eth) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
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
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unite)) and (float(positionAmtLong) < float(step_three_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
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
                    # collection_sxp = db["count"]

                    # sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ( (dark_eth+obv_eth+sweat_eth) > 0 and (dark_eth+obv_eth+sweat_eth) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
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
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)
                elif ( float(positionAmtShort) >= float(step_two_unite) and float(positionAmtShort) < float(step_three_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        # dark_eth = 2
                        # obv_eth = 2
                        # sweat_eth = 2

                        time.sleep(1)



        for key in object_list:
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BNBUSD_PERP")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),0))
                p = str(round(float(priceIn) +((0.055* float(priceIn))/20),2))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),2))
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=5)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) ==3 and (a < 10)):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG,  ordertype=OrderType.MARKET,  quantity=5)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb= 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < 5) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=5)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) >= 5) and (float(positionAmtLong) < 10) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=5)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2
                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BNBUSD_PERP")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),0))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),2))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),2))
                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=5)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) > 0 and (dark_bnb+obv_bnb+sweat_bnb) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) == 0 and (ass <10)):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,quantity=5)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < 5 and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=5)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= 5 and float(positionAmtShort) < 10 and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSD_PERP",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=5)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        # dark_bnb = 2
                        # obv_bnb = 2
                        # sweat_bnb = 2

                        time.sleep(1)
        
        return
    def take_order_point_new(self):
        global dark_bnb
        global obv_bnb
        global sweat_bnb
        global dark_eth
        global obv_eth
        global sweat_eth



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
            if (key.get('positionSide') =='LONG' and (key.get('symbol') == "BNBUSDT")):
                positionAmtLong = key.get('positionAmt')
                priceIn = key.get('entryPrice')
                mPrice = key.get('markPrice')
                a = str(round(float(positionAmtLong),3))
                p = str(round(float(priceIn) +((0.045* float(priceIn))/20),3))
                pl = str(round(float(priceIn) -((0.15* float(priceIn))/20),3))

        
                if (float(positionAmtLong) == 0):
        
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
            
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2
                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) ==3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb= 2
                        obv_bnb = 2
                        sweat_bnb = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2
                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unite)) and (float(positionAmtLong) < float(step_three_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2
                        time.sleep(1)
        for keys in object_list:
            if (keys.get('positionSide') =='SHORT' and (keys.get('symbol') == "BNBUSDT")):

                positionAmtShort = keys.get('positionAmt')*-1
                mPrices = keys.get('markPrice')
                priceIns = keys.get('entryPrice')
                ass = str(round(float(positionAmtShort),3))
                ps = str(round(float(priceIns) -((0.045* float(priceIns))/20),3))
                pss = str(round(float(priceIns) +((0.15* float(priceIns))/20),3))



                if (float(positionAmtShort) == 0):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==1 and obv_bnb ==1 and sweat_bnb ==1)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_bnb+obv_bnb+sweat_bnb) > 0 and (dark_bnb+obv_bnb+sweat_bnb) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2

                        time.sleep(1)
                    elif ((dark_bnb+obv_bnb+sweat_bnb) == 0):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2

                        time.sleep(1)
                elif (float(positionAmtShort) >= float(step_two_unite) and float(positionAmtShort) < float(step_three_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_bnb ==0 and obv_bnb ==0 and sweat_bnb ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="BNBUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        # update_obv("2",'ALPHAUSDT')
                        # update_dark("2",'ALPHAUSDT')
                        # update_sweat("2",'ALPHAUSDT')
                        dark_bnb = 2
                        obv_bnb = 2
                        sweat_bnb = 2

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
                    # collection_sxp = db["count"]
                    # sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and  (float(mPrice) > float(p))):
                
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ((dark_eth+obv_eth+sweat_eth) <3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                    elif ((dark_eth+obv_eth+sweat_eth) ==3):
                        Up = False
                        Down = True
                        print("TP_LONG",True)
                        time.sleep(1)
                        print("take_profit_long")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=p, quantity=a,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) > 0) and (float(positionAmtLong) < float(step_two_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                elif ((float(positionAmtLong) >= float(step_two_unite)) and (float(positionAmtLong) < float(step_three_unite)) and  (float(mPrice) <= float(pl))):
                    
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]
                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="1" and obv =="1" and sweat =="1")):
                    if ((dark_eth ==1 and obv_eth ==1 and sweat_eth ==1)):
                        Up = True
                        Down = False
                        print("Up",Up)
                        time.sleep(1)
                        print("take_order_long_full")
                        take_order_long = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=buy_unite)
                        PrintBasic.print_obj(take_order_long)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

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
                    # collection_sxp = db["count"]

                    # sxp_data = collection_sxp.find_one({"market": 'SXPUSDT'})   
                    # dark = sxp_data["dark"]
                    # obv = sxp_data["obv"]
                    # sweat = sxp_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and  (float(mPrices) < float(ps))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((float(dark)+float(obv)+float(sweat)) <3):
                    if ( (dark_eth+obv_eth+sweat_eth) > 0 and (dark_eth+obv_eth+sweat_eth) <3):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth= 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                    elif ( (dark_eth+obv_eth+sweat_eth) ==0):
                        Down = False
                        Up = True

                        print("TP_SHORT ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=ps, quantity=ass,timeInForce='GTC')
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                elif (float(positionAmtShort) > 0 and float(positionAmtShort) < float(step_two_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

                        time.sleep(1)
                elif ( float(positionAmtShort) >= float(step_two_unite) and float(positionAmtShort) < float(step_three_unite) and (float(mPrices) >= float(pss))):
                    # client = MongoClient(port=27017)
                    # db = client.binance
                    # collection_alpha = db["count"]

                    # alpha_data = collection_alpha.find_one({"market": 'SXPUSDT'})   
                    # dark = alpha_data["dark"]
                    # obv = alpha_data["obv"]
                    # sweat = alpha_data["sweat"]
                    # if ((dark =="0" and obv =="0" and sweat =="0")):
                    if ((dark_eth ==0 and obv_eth ==0 and sweat_eth ==0)):
                        Down = True
                        Up = False

                        print("Down ",Down)
                        time.sleep(1)
                
                        print("take_order_short_full")

                        take_order_short = request_client.post_order(symbol="ETHUSDT",  side=OrderSide.SELL, positionSide=PositionSide.SHORT,ordertype=OrderType.MARKET,quantity=sale_unite)
                        PrintBasic.print_obj(take_order_short)
                        #update_obv("2",'SXPUSDT')
                        #update_dark("2",'SXPUSDT')
                        #update_sweat("2",'SXPUSDT')
                        dark_eth = 2
                        obv_eth = 2
                        sweat_eth = 2

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
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
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

    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
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
 
    client = MongoClient("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority")


    db = client.Binance
    collection_alpha = db["cut_loss"]



    collection_cound = db["count"]


    sxp_c_data = collection_cound.find_one({"market": 'SXPUSDT'})
    ada_c_data = collection_cound.find_one({"market": 'ADAUSDT'})
    alpha_c_data = collection_cound.find_one({"market": 'ALPHAUSDT'})
    grt_c_data = collection_cound.find_one({"market": 'GRTUSDT'})
    bnb_c_data = collection_cound.find_one({"market": 'BNBUSDT'})
    eth_c_data = collection_cound.find_one({"market": 'ETHUSDT'})
    bnbu_c_data = collection_cound.find_one({"market": 'BNBUSD_PERP'})
    
    
    
    alpha_data = collection_alpha.find_one({"market": 'ALPHAUSDT'})
    eth_data = collection_alpha.find_one({"market": 'ETHUSDT'})
 
    
    market ='ALPHAUSDT'
    dark_alpha = alpha_c_data["dark"]
    obv_alpha = alpha_c_data["obv"]
    sweat_alpha = alpha_c_data["sweat"]
    dark_ada = ada_c_data["dark"]
    obv_ada = ada_c_data["obv"]
    sweat_ada = ada_c_data["sweat"]
    dark_grt = grt_c_data["dark"]
    obv_grt = grt_c_data["obv"]
    sweat_grt = grt_c_data["sweat"]
    dark_sxp = sxp_c_data["dark"]
    obv_sxp = sxp_c_data["obv"]
    sweat_sxp = sxp_c_data["sweat"]
    dark_bnb = bnb_c_data["dark"]
    obv_bnb = bnb_c_data["obv"]
    sweat_bnb = bnb_c_data["sweat"]
    dark_eth = eth_c_data["dark"]
    obv_eth = eth_c_data["obv"]
    sweat_eth = eth_c_data["sweat"]


   
    stop_profit_rate_short = alpha_data["mgain_profit_percent_s"]
    stop_profit_rate_long = alpha_data["mgain_profit_percent"]
    stop_profit_rate_short_more = alpha_data["mgain_profit_percent_s"]
    stop_profit_rate_long_more = alpha_data["mgain_profit_percent"]
    min_profit_rate_short = alpha_data["fgain_profit_percent_s"]
    min_profit_rate_long = alpha_data["fgain_profit_percent"]
    step_two_profit_short = alpha_data["lgain_profit_percent_s"]
    step_two_profit_long = alpha_data["lgain_profit_percent"]
    stop_loss_rate_long = alpha_data["loss_percent"]
    stop_loss_rate_short = alpha_data["loss_percent_s"]
    buy_unit = alpha_data["buy"]
    sale_unit = alpha_data["sale"]
    step_one_unit = alpha_data["step_one_unit"]
    step_two_unit = alpha_data["step_two_unit"]
    step_three_unit = alpha_data["step_three_unit"]
    step_four_unit = alpha_data["step_four_unit"]


    buy_unite = eth_data["buy"]
    sale_unite = eth_data["sale"]
    step_one_unite = eth_data["step_one_unit"]
    step_two_unite = eth_data["step_two_unit"]
    step_three_unite = eth_data["step_three_unit"]
    step_four_unite = eth_data["step_four_unit"]
##    step_five_unit = alpha_data["step_five_unit"]
##    step_six_unit = alpha_data["step_six_unit"]
##    step_seven_unit = alpha_data["step_seven_unit"]
    guided = alpha_data["guided"]
    macd = alpha_data["macd"]

    #interval = alpha_data["interval"]
    reentry_unit = alpha_data["reentry_unit"]

    #update_dark(1,market)
    try:
        while True:
            thread1 = OkEx1(1,"get mail 1")
            thread2 = Bin33(2,"Count Candle")
            #thread3 = Bin333(3,"Count Candle")
            thread1.start()
            thread2.start()
            #thread3.start()
            thread1.join()
            thread2.join()
            #thread3.join()
            time.sleep(1)
    except IndexError as error:
        print("Exiting: with error" + "\n")
    except Exception as exception:
        print("Exiting: Exception error" +  "\n")

