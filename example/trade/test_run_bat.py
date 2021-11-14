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
import tempfile
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
            result_open_order = request_client.get_open_orders()
            time.sleep(5)


            
            object_list = []
            object_list_open = []
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
            for key in object_list:

                if (key.get('positionSide') =='SHORT'  and key.get('positionAmt') == 0.0):
                    if (key.get('symbol') =='BCHUSDT'):
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BCHUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "BCHUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='DEFIUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "DEFIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "DEFIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='LUNAUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "LUNAUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "LUNAUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='OMGUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "OMGUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "OMGUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='KSMUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "KSMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "KSMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='EGLDUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "EGLDUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "EGLDUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='BELUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BELUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "BELUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='REEFUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "REEFUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "REEFUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='KEEPUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "KEEPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "KEEPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='MATICUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "MATICUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "MATICUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='HUTUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "HNTUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "HNTUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='SFPUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "SFPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "SFPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='1000SHIBUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "1000SHIBUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "1000SHIBUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='BAKESDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BAKESDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "BAKESDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='C98USDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "C98USDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "C98USDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='XLMUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "XLMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "XLMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='ADAUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ADAUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "ADAUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n") 
                    elif (key.get('symbol') =='XRPUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "XRPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "XRPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n") 
                    elif (key.get('symbol') =='DOGEUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "DOGEUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "DOGEUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n") 
                    elif (key.get('symbol') =='BTCUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BTCUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "BTCUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ATOMUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ATOMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "BCHUSDT"):
                                    markets = "ATOMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='AAVEUSDT'):   
                        
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "AAVEUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "AAVEUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")                                   
                                
                                
                                
                    elif (key.get('symbol') =='DASHUSDT'):   
                        
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "DASHUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "DASHUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)            
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='DOTUSDT'):   
                        
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dotusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "DOTUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "DOTUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)            
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='BNBUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "BNBUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "BNBUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='COMPUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "COMPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "COMPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ETCUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ETCUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ETCUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ETHUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ETHUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ETHUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='LINKUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "LINKUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "LINKUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='LTCUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "LTCUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "LTCUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='MKRUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "MKRUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "MKRUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='NEOUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "NEOUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "NEOUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='QTUMUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "QTUMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "QTUMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='SOLUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "SOLUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "SOLUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='UNIUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "UNIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "UNIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='XMRUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "XMRUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "XMRUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='YFIUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "YFIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "YFIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='YFIIUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "YFIIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "YFIIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ZECUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "ZECUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ZECUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        

                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='AXSUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "AXSUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "AXSUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        

                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='WAVESUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_wavesusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "WAVESUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "WAVESUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        

                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   

                elif (key.get('positionSide') =='LONG'  and key.get('positionAmt') == 0.0):
                    if (key.get('symbol') =='BCHUSDT'):
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BCHUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "BCHUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='DEFIUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "DEFIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "DEFIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='KSMUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "KSMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "KSMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n") 
                    elif (key.get('symbol') =='LUNAUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "LUNAUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "LUNAUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n") 
                    elif (key.get('symbol') =='OMGUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "OMGUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "OMGUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n") 
                    elif (key.get('symbol') =='EGLDUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "EGLDUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "EGLDUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='BELUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BELUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "BELUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='REEFUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "REEFUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "REEFUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='KEEPUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "KEEPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "KEEPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='MATICUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "MATICUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "MATICUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='HNTUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "HNTUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "HNTUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='SFPUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "SFPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "SFPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='1000SHIBUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "1000SHIBUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "1000SHIBUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='BAKEUSDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BAKEUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "BAKEUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='C98USDT'):   
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "C98USDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "C98USDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  

                    elif (key.get('symbol') =='ADAUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ADAUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ADAUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='XRPUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "XRPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "XRPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")  
                    elif (key.get('symbol') =='DOGEUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "DOGEUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "DOGEUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")    
                    elif (key.get('symbol') =='DOTUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dotusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "DOTUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "DOTUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='BTCUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BTCUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "BTCUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ATOMUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ATOMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ATOMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='AAVEUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "AAVEUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "AAVEUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 

                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")                       
                    elif (key.get('symbol') =='DASHUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "DASHUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "DASHUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='BNBUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "BNBUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "BNBUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='COMPUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "COMPUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "COMPUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ETCUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ETCUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ETCUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ETHUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ETHUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ETHUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='LINKUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "LINKUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "LINKUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='LTCUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "LTCUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "LTCUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='MKRUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "MKRUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "MKRUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='NEOUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "NEOUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "NEOUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='QTUMUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "QTUMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "QTUMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='SOLUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "SOLUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "SOLUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='UNIUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "UNIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "UNIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='XMRUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "XMRUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "XMRUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='YFIUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "YFIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "YFIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='YFIIUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "YFIIUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "YFIIUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds) 
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")   
                    elif (key.get('symbol') =='ZECUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "ZECUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "ZECUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")               
                    elif (key.get('symbol') =='AXSUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "AXSUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "AXSUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")    
                    elif (key.get('symbol') =='WAVESUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_wavesusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "WAVESUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "WAVESUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")    
                    elif (key.get('symbol') =='XLMUSDT'):   
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        try:
                            for keys in object_list_open:
                                    #cont = 0
                                if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "XLMUSDT") and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
                                    #if (keys.get('symbol') == "AAVEUSDT"):
                                    markets = "XLMUSDT"
                                    orderIds = keys.get('orderId')
                                    
                                    print("market",markets)
                                    print("orderId",orderIds)

                                    ##time.sleep(1)
                                    result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
                        except IndexError as error:
                            print("Exiting: with error" + "\n")
                        except Exception as exception:
                            print("Exiting: Exception error" +  "\n")    

            time.sleep(10)                    
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


   
