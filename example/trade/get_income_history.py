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
g_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
g_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'

res_tour = "None"
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_income_history(symbol="adausd_perp",limit= 5)
object_list = []

for res in result:
    d = collections.defaultdict()
    d['symbol'] = res.symbol
    d['incomeType'] = res.incomeType
    d['income'] = res.income
    object_list.append(d)   
for key in object_list:
    if (key.get('incomeType') =='REALIZED_PNL' and (key.get('symbol') == "ADAUSD_PERP")):
        incomeRes = key.get('income')
        if float(incomeRes) > 0: 
            print("Win")
            #print(incomeRes)
            res_tour = "WinRes"
        else:
            print("Loss")
            #print(incomeRes)
            res_tour = "LossRes"
        #print(incomeRes)

print(res_tour)
