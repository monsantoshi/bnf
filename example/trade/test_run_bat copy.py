from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
from decimal import *
from pymongo import MongoClient
import email
import imaplib
import collections
import os
import time
import array as arr
import threading
import datetime
import math
"""
Python script to interact with existing Windows Task Scheduler tasks.
CLI usage:
    python windows_task_scheduler.py {enable|disable|run} -t "TaskName"
import usage:
    import windows_task_scheduler as wts
    wts.enable_task(task_name='TaskName')
    wts.disable_task(task_name='TaskName')
    wts.run_task(task_name='TaskName')
There are many more possibilities; at the command prompt, type 'schtasks.exe /?' or e.g. 'schtasks.exe /Change /?' for details.
"""

import logging
import argparse
import subprocess


logger = logging.getLogger(__name__)


def get_parser():
    # Parse inputs
    parser = argparse.ArgumentParser(
        description="Provide task name", add_help=False)

    parser.add_argument("-t", "--task", dest="task_name",
                        required=False, help="Task name (in Windows Task Scheduler)")

    # Choose functionality
    subparsers = parser.add_subparsers()

    parser_enable = subparsers.add_parser(
        "enable", parents=[parser], help="Enable the task")
    parser_enable.set_defaults(func=enable_task)

    parser_disable = subparsers.add_parser(
        "disable", parents=[parser], help="Disable the task")
    parser_disable.set_defaults(func=disable_task)

    parser_run = subparsers.add_parser(
        "run", parents=[parser], help="Run the task")
    parser_run.set_defaults(func=run_task)

    return parser


def enable_task(args=None, task_name=None):
    """ Enable existing Windows Task Scheduler task.
    """
    if args is not None:
        task_name = args.task_name

    p = subprocess.Popen(['schtasks.exe', '/Change', '/TN', task_name,
                          '/ENABLE'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info("Enabled task: {0}".format(task_name))
    return


def disable_task(args=None, task_name=None):
    """ Disable existing Windows Task Scheduler task.
    """
    if args is not None:
        task_name = args.task_name

    p = subprocess.Popen(['schtasks.exe', '/Change', '/TN', task_name,
                          '/DISABLE'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info("Disabled task: {0}".format(task_name))
    return


def run_task(args=None, task_name=None):
    """ Run existing Windows Task Scheduler task.
    """
    if args is not None:
        task_name = args.task_name

    p = subprocess.Popen(['schtasks.exe', '/Run', '/TN', task_name],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info("Run task: {0}".format(task_name))
    return


def main(args=None):
    logger.info("\n" + "=" * 72 + "\n{0} begun ...".format(__name__))

    # Handle arguments
    if args is None:
        args = get_parser().parse_args()
        args.func(args)
    else:
        # Use externally-provided arguments
        if args.disable_flag:
            disable_task(task_name=args.task_name)
        elif args.enable_flag:
            enable_task(task_name=args.task_name)
        elif args.run_flag:
            run_task(task_name=args.task_name)


if __name__ == '__main__':
    g_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    g_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    o_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    o_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP' 
    try:
        while True:
            request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
            result = request_client.get_position()


            
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
                object_list.append(d)
            for key in object_list:
    
                if (key.get('positionSide') =='SHORT' and key.get('symbol') =='BCHUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BCHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='BTCUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BTCUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='LTCUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "LTCUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='ETHUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ETHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='ETCUSDT' and key.get('positionAmt') == 0.0):
    
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ETCUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='ATOMUSDT' and key.get('positionAmt') == 0.0):
        
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ATOMUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='QTUMUSDT' and key.get('positionAmt') == 0.0):
        
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "QTUMUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 


                        

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='LINKUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "LINKUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='BNBUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BNBUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

 

                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='COMPUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "COMPUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='UNIUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "UNIUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                  
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='SOLUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "SOLUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                   
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='ZECUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ZECUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='XMRUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "XMRUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                    
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='DASHUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "DASHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                   
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='NEOUSDT' and key.get('positionAmt') == 0.0):
        
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "NEOUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='MKRUSDT' and key.get('positionAmt') == 0.0):
            
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "MKRUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='AAVEUSDT' and key.get('positionAmt') == 0.0):
            
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "AAVEUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='YFIUSDT' and key.get('positionAmt') == 0.0):
            
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "YFIUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='SHORT' and key.get('symbol') =='YFIIUSDT' and key.get('positionAmt') == 0.0):
            
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "YFIIUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

               
                
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='BCHUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BCHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='BTCUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BTCUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='LTCUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "LTCUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='ETHUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ETHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='LINKUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "LINKUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='BNBUSDT' and key.get('positionAmt') == 0.0):

                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BNBUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                    
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='COMPUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "COMPUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            time.sleep(100)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='UNIUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "UNIUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                  
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='SOLUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "SOLUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                   
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='ZECUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ZECUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='XMRUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "XMRUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                    
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='DASHUSDT' and key.get('positionAmt') == 0.0):
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "DASHUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)                   

                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='ATOMUSDT' and key.get('positionAmt') == 0.0):
        
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ATOMUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='QTUMUSDT' and key.get('positionAmt') == 0.0):
        
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "QTUMUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='ETCUSDT' and key.get('positionAmt') == 0.0):
        
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ETCUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='NEOUSDT' and key.get('positionAmt') == 0.0):
            
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "NEOUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='MKRUSDT' and key.get('positionAmt') == 0.0):
                
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "MKRUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='YFIUSDT' and key.get('positionAmt') == 0.0):
                
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "YFIUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='YFIIUSDT' and key.get('positionAmt') == 0.0):
                
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "YFIIUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                elif (key.get('positionSide') =='LONG' and key.get('symbol') =='AAVEUSDT' and key.get('positionAmt') == 0.0):
                    
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    result_open_order = request_client.get_open_orders()
                    ##time.sleep(1)
                    object_list_open = []
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
                        time.sleep(1)                       


                        
                    for keys in object_list_open:
                        #cont = 0
                        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "AAVEUSDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                            markets = keys.get('symbol')
                            orderIds = keys.get('orderId')
                            
                            print("market",markets)
                            print("orderId",orderIds)

                            ##time.sleep(1)
                            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                                       
                                                                                


        time.sleep(10)
           
    except IndexError as error:
        print("Exiting: with error" + "\n")
    except Exception as exception:
        print("Exiting: Exception error" +  "\n")


   
