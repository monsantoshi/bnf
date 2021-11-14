#!/usr/bin/env python
from binance_f import RequestClient

from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
from make_order_coin_bnb import take_order_coin_perp


from datetime import datetime
from binance.client import Client


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



detach_dir = 'c:\db'
class OkEx1(threading.Thread):
    def __init__(self,threadId,name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
     
    def run(self):
        print("Starting: 1 " + self.name + "\n")
        k1 = getmail(market)
        k1.two_way_email("imap.gmail.com", "tedview33@gmail.com", "bbgadrmdzbglzhfk")
        print("Exiting: 1 " + self.name + "\n")

def update_ada_long1(p1):
    
    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ADA']['LONGADA'] = p1 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_ada_long2(p2):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ADA']['longada'] = p2 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_ada_short1(p3):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ADA']['SHORTADA'] = p3 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_ada_short2(p4):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ADA']['shortada'] = p4

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()
def update_xrp_long1(p1):
    
    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XRP']['LONGXRP'] = p1 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_xrp_long2(p2):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XRP']['longxrp'] = p2 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_xrp_short1(p3):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XRP']['SHORTXRP'] = p3 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_xrp_short2(p4):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XRP']['shortxrp'] = p4

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()
def update_xmr_long1(p1):
    
    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XMR']['LONGXMR'] = p1 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_xmr_long2(p2):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XMR']['longxmr'] = p2 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_xmr_short1(p3):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XMR']['SHORTXMR'] = p3 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_xmr_short2(p4):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['XMR']['shortxmr'] = p4

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_eth_long1(p1):
    
    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ETH']['LONGETH'] = p1 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_eth_long2(p2):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ETH']['longeth'] = p2 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_eth_short1(p3):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ETH']['SHORTETH'] = p3 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_eth_short2(p4):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['ETH']['shorteth'] = p4

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_bch_long1(p1):
    
    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['BCH']['LONGBCH'] = p1 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_bch_long2(p2):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['BCH']['longbch'] = p2 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_bch_short1(p3):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['BCH']['SHORTBCH'] = p3 

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_bch_short2(p4):

    with open("order.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['BCH']['shortbch'] = p4

    with open("order.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()

def update_long1(p1,markett):

    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['LONG'] = p1 
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['LONG'] = p1 
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['LONG'] = p1 
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['LONG'] = p1 
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['LONG'] = p1 
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['LONG'] = p1 
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['LONG'] = p1 
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['LONG'] = p1 
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['LONG'] = p1 
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['LONG'] = p1 
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['LONG'] = p1 
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['LONG'] = p1 
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['LONG'] = p1 
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['LONG'] = p1 
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['LONG'] = p1 
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['LONG'] = p1 
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['LONG'] = p1 
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['LONG'] = p1 
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['LONG'] = p1 
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['LONG'] = p1 
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['LONG'] = p1 
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['LONG'] = p1 
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    return

def update_long2(p2,markett):
    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['long'] = p2
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['long'] = p2
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['long'] = p2
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['long'] = p2
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['long'] = p2
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['long'] = p2
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['long'] = p2
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['long'] = p2
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['long'] = p2
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['long'] = p2
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['long'] = p2
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['long'] = p2
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['long'] = p2
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['long'] = p2
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['long'] = p2
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['long'] = p2
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['long'] = p2
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['long'] = p2
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['long'] = p2
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['long'] = p2
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['long'] = p2
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['long'] = p2
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    return

def update_short1(p3,markett):
    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['SHORT'] = p3
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['SHORT'] = p3
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['SHORT'] = p3
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['SHORT'] = p3
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['SHORT'] = p3
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['SHORT'] = p3
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['SHORT'] = p3
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['SHORT'] = p3 
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['SHORT'] = p3
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['SHORT'] = p3 
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['SHORT'] = p3
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['SHORT'] = p3
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['SHORT'] = p3
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['SHORT'] = p3
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['SHORT'] = p3 
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['SHORT'] = p3
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['SHORT'] = p3
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['SHORT'] = p3
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['SHORT'] = p3
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['SHORT'] = p3 
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['SHORT'] = p3
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['SHORT'] = p3 
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    return

def update_short2(p4,markett):

    if (markett == "AAVEUSDT"):
        with open("aave.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AAVE']['short'] = p4
        with open("aave.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ADAUSDT"):
        with open("ada.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ADA']['short'] = p4
        with open("ada.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "AXSUSDT"):
        with open("axs.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['AXS']['short'] = p4
        with open("axs.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BNBUSDT"):
        with open("bnb.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BNB']['short'] = p4
        with open("bnb.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BCHUSDT"):
        with open("bch.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BCH']['short'] = p4
        with open("bch.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "BTCUSDT"):
        with open("btc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['BTC']['short'] = p4
        with open("btc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "COMPUSDT"):
        with open("comp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['COMP']['short'] = p4
        with open("comp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "DASHUSDT"):
        with open("dash.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['DASH']['short'] = p4
        with open("dash.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETCUSDT"):
        with open("etc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETC']['short'] = p4
        with open("etc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ETHUSDT"):
        with open("eth.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ETH']['short'] = p4
        with open("eth.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LINKUSDT"):
        with open("link.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LINK']['short'] = p4
        with open("link.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "LTCUSDT"):
        with open("ltc.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['LTC']['short'] = p4
        with open("ltc.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close() 
    elif (markett == "MKRUSDT"):
        with open("mkr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['MKR']['short'] = p4
        with open("mkr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "NEOUSDT"):
        with open("neo.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['NEO']['short'] = p4
        with open("neo.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "QTUMUSDT"):
        with open("qtum.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['QTUM']['short'] = p4 
        with open("qtum.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "SOLUSDT"):
        with open("sol.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['SOL']['short'] = p4
        with open("sol.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "UNIUSDT"):
        with open("uni.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['UNI']['short'] = p4
        with open("uni.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XMRUSDT"):
        with open("xmr.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XMR']['short'] = p4
        with open("xmr.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "XRPUSDT"):
        with open("xrp.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['XRP']['short'] = p4
        with open("xrp.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIUSDT"):
        with open("yfi.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFI']['short'] = p4 
        with open("yfi.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "YFIIUSDT"):
        with open("yfii.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['YFII']['short'] = p4
        with open("yfii.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    elif (markett == "ZECUSDT"):
        with open("zec.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data['ZEC']['short'] = p4
        with open("zec.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            #json.close()
    return



def take_order_sell_mon(self):

    short_amount_in = 0

    result = request_client_mon.get_position()

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
        if (key.get('positionSide') =='SHORT' and key.get('positionAmt') =='BNBUSD_PERP' and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
           # time.sleep(5)

            client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")
            db = client.Binance
            collection_alpha = db["cut_loss"]
       
            bnb_data = collection_alpha.find_one({"market": 'BNBUSD_PERP'})


            step_two_unit = bnb_data["step_two_unit"]


            if ((float(ass) >=  0) and (float(ass) <= float(step_two_unit))):

                take_profit_bnb = request_client_mon.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=1)
                PrintBasic.print_obj(take_profit_bnb)
                time.sleep(1)

                time.sleep(1)

    return
def take_order_buy_mon(self):

    long_amount_in = 0
    long_amount_out = 0
 
    result = request_client_mon.get_position()

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
        if (key.get('positionSide') =='LONG' and key.get('positionAmt') =='BNBUSD_PERP' and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
           # time.sleep(5)

            client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


            db = client.Binance
            collection_bnb = db["cut_loss"]
            bnb_data = collection_bnb.find_one({"market": 'BNBUSD_PERP'})


            step_two_unit = bnb_data["step_two_unit"]

            if ((float(a) >= 0) and (float(a) <= float(step_two_unit))):

                take_profit_bnb = request_client_mon.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
                PrintBasic.print_obj(take_profit_bnb)
                time.sleep(1)

                time.sleep(1)
    # if ((short_amount_in > 0) and (count_l > limit_l)):
    #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
    #     time.sleep(1)
    return
def take_order_sell(self):


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
        if (key.get('positionSide') =='SHORT' and key.get('positionAmt') =='BNBUSD_PERP' and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
           # time.sleep(5)

            client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")
            db = client.Binance
            collection_alpha = db["cut_loss"]

            bnb_data = collection_alpha.find_one({"market": 'BNBUSD_PERP'})


            step_two_unit = bnb_data["step_two_unit"]


            if ((float(ass) >=  0) and (float(ass) <= float(step_two_unit))):

                take_profit_bnb = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=1)
                PrintBasic.print_obj(take_profit_bnb)
                time.sleep(1)

                time.sleep(1)

    return
def take_order_buy(self):

 
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
        if (key.get('positionSide') =='LONG' and key.get('positionAmt') =='BNBUSD_PERP' and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
           # time.sleep(5)

            client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


            db = client.Binance
            collection_bnb = db["cut_loss"]
            bnb_data = collection_bnb.find_one({"market": 'BNBUSD_PERP'})


            step_two_unit = bnb_data["step_two_unit"]

            if ((float(a) >= 0) and (float(a) <= float(step_two_unit))):

                take_profit_bnb = request_client.post_order(symbol="BNBUSD_PERP", side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=15)
                PrintBasic.print_obj(take_profit_bnb)
                time.sleep(1)

                time.sleep(1)
            # if ((short_amount_in > 0) and (count_l > limit_l)):
            #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
            #     time.sleep(1)
    return

def take_order_sell_coin_bnbusdt(self,markett):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,2))
            print("ass" ,ass)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")
    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
       
    #         coin_data = collection_coin.find_one({"market":markett})


    #         step_two_unit = coin_data["step_two_unit"]


            if ((float(ass) >=  0) ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=0.1)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None

    #time.sleep(1)

    return
def take_order_buy_coin_bnbusdt(self,markett):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),2))
            print("a" ,a)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})


    #         step_two_unit = coin_data["step_two_unit"]

            if ((float(a) >= 0) ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=0.1)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return

    return



def take_order_sell_coin_adausdt(self,markett):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")
    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
       
    #         coin_data = collection_coin.find_one({"market":markett})


    #         step_two_unit = coin_data["step_two_unit"]


            if ((float(ass) >=  0) and (float(ass) <= 100)):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=20)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return

    #time.sleep(1)

    return
def take_order_buy_coin_adausdt(self,markett):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})


    #         step_two_unit = coin_data["step_two_unit"]

            if ((float(a) >= 0) and (float(a) <= 100)):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=20)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return

    #time.sleep(1)
# if ((short_amount_in > 0) and (count_l > limit_l)):
#     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
#     time.sleep(1)
    return

def take_order_sell_coin(self,markett):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
           # time.sleep(5)
            if ((float(ass) >=  0) and (float(ass) <= 100)):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=15)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)


    return
def take_order_buy_coin(self,markett):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)


            if ((float(a) >= 0) and (float(a) <= 120)):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=15)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
# if ((short_amount_in > 0) and (count_l > limit_l)):
#     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
#     time.sleep(1)
    return

def take_order_sell_coin_dogeusdt(self,markett,coin):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)

            if ((float(ass) >=  0) and (float(ass) < 20)):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DOGEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            else:
                e = None
                r = None

    #time.sleep(1)

    return
def take_order_buy_coin_dogeusdt(self,markett,coin):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})


    #         step_two_unit = coin_data["step_two_unit"]

            if ((float(a) >= 0) and (float(a) < 20)):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DOGEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None
    return



def take_order_sell_coin_ethusdt(self,markett,coin):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,2))
            print("ass" ,ass)

        
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 


            if ((float(ass) < 0.01) and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None

    return
def take_order_buy_coin_ethusdt(self,markett,coin):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),2))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 

            if ((float(a) < 0.01) and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None
    
    return


def take_order_sell_coin_btcusdt(self,markett,coin):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,3))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 

            if ((float(ass) < 0.001) and res_val == 11 ):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None

    return
def take_order_buy_coin_btcusdt(self,markett,coin):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),3))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close()           

            if ((float(a) < 0.001) and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None
    return


def take_order_sell_coin_bnbusdt(self,markett,coin):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,2))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close()        


            if ((float(ass) < 0.1) and res_val == 11 ):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None

    return
def take_order_buy_coin_bnbusdt(self,markett,coin):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),2))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 

            if ((float(a) >= 0) and (float(a) <= 0.1) and res_val == 3):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None
    return



def take_order_sell_coin_linkusdt(self,markett,coin):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 


            if ((float(ass) <  1) and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AXSUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None

    return
def take_order_buy_coin_linkusdt(self,markett,coin):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close()          

            if ((float(a) < 1) and res_val == 3):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AXSUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None
    return


def take_order_sell_coin_adausdt(self,markett,coin):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 


    #         step_two_unit = coin_data["step_two_unit"]



            if ((float(ass) <  40) and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AXSUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None

    return
def take_order_buy_coin_adausdt(self,markett,coin):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})


            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 

            if ((float(a) < 40) and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AXSUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None
    return



def take_order_sell_coin_xrpusdt(self,markett,coin):
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
           # time.sleep(5)

            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['SHORT'] + data['ETH']['short']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['SHORT'] + data['BCH']['short']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['SHORT'] + data['AAVE']['short']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['SHORT'] + data['ADA']['short']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['SHORT'] + data['AXS']['short']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['SHORT'] + data['BNB']['short']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['SHORT'] + data['BTC']['short']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['SHORT'] + data['COMP']['short']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['SHORT'] + data['DASH']['short']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['SHORT'] + data['ETC']['short']
                f.close() 
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['SHORT'] + data['LINK']['short']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['SHORT'] + data['LTC']['short']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['SHORT'] + data['MKR']['short']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['SHORT'] + data['NEO']['short']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['SHORT'] + data['QTUM']['short']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['SHORT'] + data['SOL']['short']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['SHORT'] + data['UNI']['short']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['SHORT'] + data['XMR']['short']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['SHORT'] + data['XRP']['short']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['SHORT'] + data['YFI']['short']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['SHORT'] + data['YFII']['short']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['SHORT'] + data['ZEC']['short']
                f.close() 


            if ((float(ass) <  40) and res_val == 11):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AXSUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None

    return
def take_order_buy_coin_xrpusdt(self,markett,coin):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
            if (markett=="ETHUSDT"):
                f = open ('eth.json', "r")

                data = json.loads(f.read())
                res_val = data['ETH']['LONG'] + data['ETH']['long']
                f.close() 
            elif (markett == "BCHUSDT"):
                f = open ('bch.json', "r")

                data = json.loads(f.read())                
                res_val = data['BCH']['LONG'] + data['BCH']['long']
                f.close()     
            elif (markett == "AAVEUSDT"):
                f = open ('aave.json', "r")

                data = json.loads(f.read())
                res_val = data['AAVE']['LONG'] + data['AAVE']['long']
                f.close() 
            elif (markett == "ADAUSDT"):
                f = open ('ada.json', "r")

                data = json.loads(f.read())
                res_val = data['ADA']['LONG'] + data['ADA']['long']
                f.close() 
            elif (markett == "AXSUSDT"):
                f = open ('axs.json', "r")

                data = json.loads(f.read())
                res_val = data['AXS']['LONG'] + data['AXS']['long']
                f.close() 
            elif (markett == "BNBUSDT"):
                f = open ('bnb.json', "r")

                data = json.loads(f.read())
                res_val = data['BNB']['LONG'] + data['BNB']['long']
                f.close() 
            elif (markett == "BTCUSDT"):
                f = open ('btc.json', "r")

                data = json.loads(f.read())
                res_val = data['BTC']['LONG'] + data['BTC']['long']
                f.close() 
            elif (markett == "COMPUSDT"):
                f = open ('comp.json', "r")

                data = json.loads(f.read())
                res_val = data['COMP']['LONG'] + data['COMP']['long']
                f.close() 
            elif (markett == "DASHUSDT"):
                f = open ('dash.json', "r")

                data = json.loads(f.read())
                res_val = data['DASH']['LONG'] + data['DASH']['long']
                f.close() 
            elif (markett == "ETCUSDT"):
                f = open ('etc.json', "r")

                data = json.loads(f.read())
                res_val = data['ETC']['LONG'] + data['ETC']['long']
                f.close()
            elif (markett == "LINKUSDT"):
                f = open ('link.json', "r")

                data = json.loads(f.read())
                res_val = data['LINK']['LONG'] + data['LINK']['long']
                f.close() 
            elif (markett == "LTCUSDT"):
                f = open ('ltc.json', "r")

                data = json.loads(f.read())
                res_val = data['LTC']['LONG'] + data['LTC']['long']
                f.close() 
            elif (markett == "MKRUSDT"):
                f = open ('mkr.json', "r")

                data = json.loads(f.read())
                res_val = data['MKR']['LONG'] + data['MKR']['long']
                f.close() 

            elif (markett == "NEOUSDT"):
                f = open ('neo.json', "r")

                data = json.loads(f.read())
                res_val = data['NEO']['LONG'] + data['NEO']['long']
                f.close() 
            elif (markett == "QTUMUSDT"):
                f = open ('qtum.json', "r")

                data = json.loads(f.read())
                res_val = data['QTUM']['LONG'] + data['QTUM']['long']
                f.close() 
            elif (markett == "SOLUSDT"):
                f = open ('sol.json', "r")

                data = json.loads(f.read())
                res_val = data['SOL']['LONG'] + data['SOL']['long']
                f.close() 
            elif (markett == "UNIUSDT"):
                f = open ('uni.json', "r")

                data = json.loads(f.read())
                res_val = data['UNI']['LONG'] + data['UNI']['long']
                f.close() 
            elif (markett == "XMRUSDT"):
                f = open ('xmr.json', "r")

                data = json.loads(f.read())
                res_val = data['XMR']['LONG'] + data['XMR']['long']
                f.close() 
            elif (markett == "XRPUSDT"):
                f = open ('xrp.json', "r")

                data = json.loads(f.read())
                res_val = data['XRP']['LONG'] + data['XRP']['long']
                f.close() 
            elif (markett == "YFIUSDT"):
                f = open ('yfi.json', "r")

                data = json.loads(f.read())
                res_val = data['YFI']['LONG'] + data['YFI']['long']
                f.close() 
            elif (markett == "YFIIUSDT"):
                f = open ('yfii.json', "r")

                data = json.loads(f.read())
                res_val = data['YFII']['LONG'] + data['YFII']['long']
                f.close() 
            elif (markett == "ZECUSDT"):
                f = open ('zec.json', "r")

                data = json.loads(f.read())
                res_val = data['ZEC']['LONG'] + data['ZEC']['long']
                f.close() 

            if ((float(a) < 40) and res_val == 3 ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
            if (markett=="BCHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ETHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LTCUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ADAUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_adausdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XLMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_s_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dogeusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="LINKUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="BNBUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XRPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xrpusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AAVEUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_aaveusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ATOMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="COMPUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="DASHUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="MKRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_mkrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="NEOUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_neousdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="QTUMUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="SOLUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="UNIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="XMRUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="YFIIUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_yfiiusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="ZECUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif (markett=="AXSUSDT"):
                s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(1)
                e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_axsusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                e = None
                r = None
    return


def take_order_sell_coin_ada(self,markett):
    #request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


    # result = request_client.get_position()

    # time.sleep(1)
    # object_list = []
    # #i = 0
    # for res in result:
    #     d = collections.defaultdict()
    #     #d['index'] = i
    #     d['symbol'] = res.symbol
    #     d['positionAmt'] = res.positionAmt
    #     d['entryPrice'] = res.entryPrice
    #     d['markPrice'] = res.markPrice
    #     d['positionSide'] = res.positionSide
    #     #d['unRealizedProfit'] = res.unRealizedProfit
    # # i = i+1
    #     object_list.append(d)

    # for key in object_list:
    #     if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') <= 0.0):
    #         syms = key.get('symbol')
    #         mPrices = key.get('markPrice')
    #         priceIns = key.get('entryPrice')
    #         positionAmtShort = key.get('positionAmt')
    #         print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
    #         ##time.sleep()
    #         ass = str(round(float(positionAmtShort)*-1,0))
    #         print("ass" ,ass)
    #        # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")
    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
       
    #         coin_data = collection_coin.find_one({"market":markett})


    #         step_two_unit = coin_data["step_two_unit"]


    #         if ((float(ass) >=  0) and (float(ass) <= float(step_two_unit))):

    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=15)
    PrintBasic.print_obj(take_profit_coin)
    time.sleep(1)

    #time.sleep(1)

    return
def take_order_buy_coin_ada(self,markett):


 
    # result = request_client.get_position()

    # time.sleep(1)
    # object_list = []
    # #i = 0
    # for res in result:
    #     d = collections.defaultdict()
    #     #d['index'] = i
    #     d['symbol'] = res.symbol
    #     d['positionAmt'] = res.positionAmt
    #     d['entryPrice'] = res.entryPrice
    #     d['markPrice'] = res.markPrice
    #     d['positionSide'] = res.positionSide
    #     #d['unRealizedProfit'] = res.unRealizedProfit
    # # i = i+1
    #     object_list.append(d)

    # for key in object_list:
    #     if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') >= 0.0):
    #         sym = key.get('symbol')
    #         mPrice = key.get('markPrice')
    #         priceIn = key.get('entryPrice')
    #         positionAmtLong = key.get('positionAmt')
    #         print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
    #         ##time.sleep()
    #         a = str(round(float(positionAmtLong),0))
    #         print("a" ,a)
    #        # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})


    #         step_two_unit = coin_data["step_two_unit"]

    #         if ((float(a) >= 0) and (float(a) <= float(step_two_unit))):

    take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=15)
    PrintBasic.print_obj(take_profit_coin)
    time.sleep(1)

    time.sleep(1)
# if ((short_amount_in > 0) and (count_l > limit_l)):
#     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
#     time.sleep(1)
    return


def take_order_sell_coin_mon(self,markett):
   


    result = request_client_mon.get_position()

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
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
           # time.sleep(5)

            client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")
            db = client.Binance
            collection_coin = db["cut_loss"]
       
            coin_data = collection_coin.find_one({"market":markett})


            step_two_unit = coin_data["step_two_unit"]


            if ((float(ass) >=  0) and (float(ass) <= float(step_two_unit))):

                take_profit_coin = request_client_mon.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=1)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)

                time.sleep(1)

    return
def take_order_buy_coin_mon(self,markett):


 
    result = request_client_mon.get_position()

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
           # time.sleep(5)

            client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


            db = client.Binance
            collection_coin = db["cut_loss"]
            coin_data = collection_coin.find_one({"market":markett})


            step_two_unit = coin_data["step_two_unit"]

            if ((float(a) >= 0) and (float(a) <= float(step_two_unit))):

                take_profit_coin = request_client_mon.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)

                time.sleep(1)
            # if ((short_amount_in > 0) and (count_l > limit_l)):
            #     cut_loss_alpha = request_client.post_order(symbol="ALPHAUSDT", side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=short_amount_in)
            #     time.sleep(1)
    return

def take_order_buy_bnbbtc(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='BNBBTC',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.1)
    PrintBasic.print_obj(order)

def take_order_sell_bnbbtc(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='BNBBTC',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.1)
    PrintBasic.print_obj(order)


def take_order_buy_bnbeth(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='BNBETH',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.1)
    PrintBasic.print_obj(order)

def take_order_sell_bnbeth(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='BNBETH',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.1)
    PrintBasic.print_obj(order)

def take_order_buy_ethbtc(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='ETHBTC',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.02)
    PrintBasic.print_obj(order)

def take_order_sell_ethbtc(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='ETHBTC',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.02)
    PrintBasic.print_obj(order)
def take_order_buy_dogebtc(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='DOGEBTC',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=200)
    PrintBasic.print_obj(order)

def take_order_sell_dogebtc(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='DOGEBTC',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=200)
    PrintBasic.print_obj(order)




def close_order_sell_coin_usdt(self,markett):
   
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') < 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,3))
            print("ass" ,ass)



            if (float(ass) >  0):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=ass)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return


    return
def close_order_buy_coin_usdt(self,markett):

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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') > 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),3))
            print("a" ,a)


            if (float(a) > 0):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=a)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return

    return



def close_order_sell_coin(self,markett):
   
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
        if (key.get('positionSide') =='SHORT' and key.get('symbol') == markett and key.get('positionAmt') < 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(syms,'',mPrices,'',priceIns,'',positionAmtShort)
            ##time.sleep()
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)



            if (float(ass) >  0):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=ass)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)


    return
def close_order_buy_coin(self,markett):
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
        if (key.get('positionSide') =='LONG' and key.get('symbol') ==markett and key.get('positionAmt') > 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            print(sym,'',mPrice,'',priceIn,'',positionAmtLong)
            ##time.sleep()
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)


            if (float(a) > 0):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=a)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)

    return





def close_order_sell_coin_mon(self,markett):
   


    result = request_client_mon.get_position()

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



            if (float(ass) >  0):

                take_profit_coin = request_client_mon.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=ass)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)


    return
def close_order_buy_coin_mon(self,markett):


 
    result = request_client_mon.get_position()

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


            if (float(a) > 0):

                take_profit_coin = request_client_mon.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=a)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)

    return

def take_order_buy_ethusdt(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='ETHUSDT',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.004)
    PrintBasic.print_obj(order)

def take_order_sell_ethusdt(self):
       
    api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    client = Client(api_key, api_secret)
    order = client.create_order(symbol='ETHUSDT',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.004)
    PrintBasic.print_obj(order)
    

# def take_order_buy_bnbusdt(self):
       
#     api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
#     api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
#     client = Client(api_key, api_secret)
#     order = client.create_order(symbol='BNBUSDT',side=Client.SIDE_BUY,type=Client.ORDER_TYPE_MARKET,quantity=0.02)
#     PrintBasic.print_obj(order)

# def take_order_sell_bnbusdt(self):
       
#     api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
#     api_secret = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
#     client = Client(api_key, api_secret)
#     order = client.create_order(symbol='BNBUSDT',side=Client.SIDE_SELL,type=Client.ORDER_TYPE_MARKET,quantity=0.02)
#     PrintBasic.print_obj(order)

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
                    if (s1.find('BUYBNB') != -1):
            
                        print ("Contains BUY  substring ")
                        markett = "BNBUSD_PERP"


                        take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                        take_order_coin_perp.take_order_buy_coin_perp_bnb(self,markett)
                        #take_order_coin_perp.take_order_sell_coin_perp_bnb(self,markett)
                        time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SELLBNB') != -1):
                        print ("Contains SELL substring ")


                        markett = "BNBUSD_PERP"

                        take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                        take_order_coin_perp.take_order_sell_coin_perp_bnb(self,markett)
                        #take_order_coin_perp.take_order_buy_coin_perp_bnb(self,markett)
                        time.sleep(1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('BUYDOGE') != -1):
                    
                        print ("Contains BUY  substring ")
                        markett = "DOGEUSD_PERP"


                        #take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                        take_order_coin_perp.take_order_buy_coin_perp(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        #time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SELLDOGE') != -1):
                        print ("Contains SELL substring ")


                        markett = "DOGEUSD_PERP"

                        take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                        take_order_coin_perp.take_order_sell_coin_perp_p(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('BUYBTC') != -1):
                        
                        print ("Contains BUY  substring ")
                        markett = "BTCUSD_PERP"


                        take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                        take_order_coin_perp.take_order_buy_coin_perp(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SELLBTC') != -1):
                        print ("Contains SELL substring ")


                        markett = "BTCUSD_PERP"

                        take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                        take_order_coin_perp.take_order_sell_coin_perp(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('BUYETH') != -1):
                        
                        print ("Contains BUY  substring ")
                        markett = "ETHUSD_PERP"


                        take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                        take_order_coin_perp.take_order_buy_coin_perp_p(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SELLETH') != -1):
                        print ("Contains SELL substring ")


                        markett = "ETHUSD_PERP"

                        take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                        take_order_coin_perp.take_order_sell_coin_perp_p(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)




                    elif (s1.find('SBBNT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BNBUSDT"
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        #take_order_sell_coin_bnbusdt(self,markett,0.1)
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SSBNT') != -1):
                        print ("Contains SELL substring ")

                        markett = "BNBUSDT"
                        
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SBXLT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "XLMUSDT"
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_dogeusdt(self,markett,40)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSXLT') != -1):
                        print ("Contains SELL substring ")

                        markett = "XLMUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_dogeusdt(self,markett,40)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('LONGADA') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ADAUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_adausdt(self,markett,20)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longada') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ADAUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_adausdt(self,markett,20)
                        ##update_ada_long2(0)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTADA') != -1):
                        print ("Contains SELL substring ")

                        markett = "ADAUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_adausdt(self,markett,20)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortada') != -1):
                        print ("Contains SELL substring ")

                        markett = "ADAUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_adausdt(self,markett,20)
                        #update_ada_short2(0)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('LONGXRP') != -1):
                        print ("Contains BUY  substring ")

                        markett = "XRPUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_xrpusdt(self,markett,20)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longxrp') != -1):
                        print ("Contains BUY  substring ")

                        markett = "XRPUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_xrpusdt(self,markett,20)
                        #update_xrp_long2(0)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTXRP') != -1):
                        print ("Contains SELL substring ")

                        markett = "XRPUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_xrp_short1(4)
                        take_order_sell_coin_xrpusdt(self,markett,20)
                        update_xrp_long1(0)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortxrp') != -1):
                        print ("Contains SELL substring ")

                        markett = "XRPUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_xrpusdt(self,markett,20)
                        #update_xrp_short2(0)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                        
                        
                        
                        
                    elif (s1.find('LONGXMR') != -1):
                        print ("Contains BUY  substring ")

                        markett = "XMRUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longxmr') != -1):
                        print ("Contains BUY  substring ")

                        markett = "XMRUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        #update_xmr_long2(0)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTXMR') != -1):
                        print ("Contains SELL substring ")

                        markett = "XMRUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortxmr') != -1):
                        print ("Contains SELL substring ")

                        markett = "XMRUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        #update_xmr_short2(0)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()

                    elif (s1.find('LONGBCH') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BCHUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longbch') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BCHUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        #update_bch_long2(0)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTBCH') != -1):
                        print ("Contains SELL substring ")

                        markett = "BCHUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortbch') != -1):
                        print ("Contains SELL substring ")

                        markett = "BCHUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        #update_bch_short2(0)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()                        
                        
                    elif (s1.find('LONGETH') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ETHUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longeth') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ETHUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        #update_eth_long2(0)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTETH') != -1):
                        print ("Contains SELL substring ")

                        markett = "ETHUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shorteth') != -1):
                        print ("Contains SELL substring ")

                        markett = "ETHUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        #update_eth_short2(0)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()                           
                        
                    elif (s1.find('LONGAAVE') != -1):
                        print ("Contains BUY  substring ")

                        markett = "AAVEUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longaave') != -1):
                        print ("Contains BUY  substring ")

                        markett = "AAVEUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTAAVE') != -1):
                        print ("Contains SELL substring ")

                        markett = "AAVEUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortaave') != -1):
                        print ("Contains SELL substring ")

                        markett = "AAVEUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()                           


                    elif (s1.find('LONGAXS') != -1):
                        print ("Contains BUY  substring ")

                        markett = "AXSUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longaxs') != -1):
                        print ("Contains BUY  substring ")

                        markett = "AXSUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_linkusdt(self,markett,1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTAXS') != -1):
                        print ("Contains SELL substring ")

                        markett = "AXSUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortaxs') != -1):
                        print ("Contains SELL substring ")

                        markett = "AXSUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()    

                    elif (s1.find('LONGBTC') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BTCUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_btcusdt(self,markett,0.001)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longbtc') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BTCUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_btcusdt(self,markett,0.001)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTBTC') != -1):
                        print ("Contains SELL substring ")

                        markett = "BTCUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_btcusdt(self,markett,0.001)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortbtc') != -1):
                        print ("Contains SELL substring ")

                        markett = "BTCUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_btcusdt(self,markett,0.001)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()  

                    elif (s1.find('LONGBNB') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BNBUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longbnb') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BNBUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTBNB') != -1):
                        print ("Contains SELL substring ")

                        markett = "BNBUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortbnb') != -1):
                        print ("Contains SELL substring ")

                        markett = "BNBUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 
                        
                        

                    elif (s1.find('LONGETC') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ETCUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longetc') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ETCUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_linkusdt(self,markett,1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTETC') != -1):
                        print ("Contains SELL substring ")

                        markett = "ETCUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortetc') != -1):
                        print ("Contains SELL substring ")

                        markett = "ETCUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGLINK') != -1):
                        print ("Contains BUY  substring ")

                        markett = "LINKUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longlink') != -1):
                        print ("Contains BUY  substring ")

                        markett = "LINKUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_linkusdt(self,markett,1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTLINK') != -1):
                        print ("Contains SELL substring ")

                        markett = "LINKUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortlink') != -1):
                        print ("Contains SELL substring ")

                        markett = "LINKUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGLTC') != -1):
                        print ("Contains BUY  substring ")

                        markett = "LTCUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longltc') != -1):
                        print ("Contains BUY  substring ")

                        markett = "LTCUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTLTC') != -1):
                        print ("Contains SELL substring ")

                        markett = "LTCUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortltc') != -1):
                        print ("Contains SELL substring ")

                        markett = "LTCUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGMKR') != -1):
                        print ("Contains BUY  substring ")

                        markett = "MKRUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longmkr') != -1):
                        print ("Contains BUY  substring ")

                        markett = "MKRUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTMKR') != -1):
                        print ("Contains SELL substring ")

                        markett = "MKRUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortmkr') != -1):
                        print ("Contains SELL substring ")

                        markett = "MKRUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 
                        

                    elif (s1.find('LONGNEO') != -1):
                        print ("Contains BUY  substring ")

                        markett = "NEOUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longneo') != -1):
                        print ("Contains BUY  substring ")

                        markett = "NEOUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_linkusdt(self,markett,1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTNEO') != -1):
                        print ("Contains SELL substring ")

                        markett = "NEOUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortneo') != -1):
                        print ("Contains SELL substring ")

                        markett = "NEOUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGQTUM') != -1):
                        print ("Contains BUY  substring ")

                        markett = "QTUMUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longqtum') != -1):
                        print ("Contains BUY  substring ")

                        markett = "QTUMUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_linkusdt(self,markett,1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTQTUM') != -1):
                        print ("Contains SELL substring ")

                        markett = "QTUMUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortqtum') != -1):
                        print ("Contains SELL substring ")

                        markett = "QTUMUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGSOL') != -1):
                        print ("Contains BUY  substring ")

                        markett = "SOLUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longsol') != -1):
                        print ("Contains BUY  substring ")

                        markett = "SOLUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_linkusdt(self,markett,1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTSOL') != -1):
                        print ("Contains SELL substring ")

                        markett = "SOLUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortsol') != -1):
                        print ("Contains SELL substring ")

                        markett = "SOLUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGUNI') != -1):
                        print ("Contains BUY  substring ")

                        markett = "UNiUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longuni') != -1):
                        print ("Contains BUY  substring ")

                        markett = "UNIUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_linkusdt(self,markett,1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTUNI') != -1):
                        print ("Contains SELL substring ")

                        markett = "UNIUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortuni') != -1):
                        print ("Contains SELL substring ")

                        markett = "UNIUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 
                        
                    elif (s1.find('LONGYFIT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "YFIUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_btcusdt(self,markett,0.001)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longyfit') != -1):
                        print ("Contains BUY  substring ")

                        markett = "YFIUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_btcusdt(self,markett,0.001)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTYFIT') != -1):
                        print ("Contains SELL substring ")

                        markett = "YFIUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_btcusdt(self,markett,0.001)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortyfit') != -1):
                        print ("Contains SELL substring ")

                        markett = "YFIUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_btcusdt(self,markett,0.001)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()

                    elif (s1.find('LONGYFII') != -1):
                        print ("Contains BUY  substring ")

                        markett = "YFIIUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longyfii') != -1):
                        print ("Contains BUY  substring ")

                        markett = "YFIIUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTYFII') != -1):
                        print ("Contains SELL substring ")

                        markett = "YFIIUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortyfii') != -1):
                        print ("Contains SELL substring ")

                        markett = "YFIIUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGZEC') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ZECUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longzec') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ZECUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTZEC') != -1):
                        print ("Contains SELL substring ")

                        markett = "ZECUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortzec') != -1):
                        print ("Contains SELL substring ")

                        markett = "ZECUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 

                    elif (s1.find('LONGCOMP') != -1):
                        print ("Contains BUY  substring ")

                        markett = "COMPUSDT"
                        update_long1(1,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        update_short1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('longcomp') != -1):
                        print ("Contains BUY  substring ")

                        markett = "COMPUSDT"
                        update_long2(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        #update_long2(0,markett)
                        update_short2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('SHORTCOMP') != -1):
                        print ("Contains SELL substring ")

                        markett = "COMPUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short1(4,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        update_long1(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()
                    elif (s1.find('shortcomp') != -1):
                        print ("Contains SELL substring ")

                        markett = "COMPUSDT"
                        close_order_buy_coin_usdt(self,markett)
                        update_short2(7,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        #update_short2(0,markett)
                        update_long2(0,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge() 
 
                    elif (s1.find('SBAXT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "AXSUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                        mail.expunge()

                    elif (s1.find('SSAXT') != -1):
                        print ("Contains SELL substring ")

                        markett = "AXSUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBXRT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "XRPUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_dogeusdt(self,markett,20)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SSXRT') != -1):
                        print ("Contains SELL substring ")

                        markett = "XRPUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_dogeusdt(self,markett,20)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBDGT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "DOGEUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_dogeusdt(self,markett,40)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SSDGT') != -1):
                        print ("Contains SELL substring ")

                        markett = "DOGEUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_dogeusdt(self,markett,40)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBLKT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "LINKUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSLKT') != -1):
                        print ("Contains SELL substring ")

                        markett = "LINKUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBUNT') != -1):
                        print ("Contains BUY  substring ")
                        markett = "UNIUSDT"                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSUNT') != -1):
                        print ("Contains SELL substring ")

                        markett = "UNIUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBATT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ATOMUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSATT') != -1):
                        print ("Contains SELL substring ")

                        markett = "ATOMUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)


                    elif (s1.find('SBQTT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "QTUMUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSQTT') != -1):
                        print ("Contains SELL substring ")

                        markett = "QTUMUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)




                    elif (s1.find('SBBTT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BTCUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_btcusdt(self,markett,0.001)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSBTT') != -1):
                        print ("Contains SELL substring ")

                        markett = "BTCUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_btcusdt(self,markett,0.001)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBETT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ETHUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSETT') != -1):
                        print ("Contains SELL substring ")

                        markett = "ETHUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBETCT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ETCUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSETCT') != -1):
                        print ("Contains SELL substring ")

                        markett = "ETCUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SBZET') != -1):
                        print ("Contains BUY  substring ")

                        markett = "ZECUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSZET') != -1):
                        print ("Contains SELL substring ")

                        markett = "ZECUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)


                    elif (s1.find('SBBCT') != -1):

                        print ("Contains BUY  substring ")

                        markett = "BCHUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSBCT') != -1):
                        print ("Contains SELL substring ")

                        markett = "BCHUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBLTT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "LTCUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSLTT') != -1):
                        print ("Contains SELL substring ")

                        markett = "LTCUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    elif (s1.find('SBCOMT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "COMPUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSCOMT') != -1):
                        print ("Contains SELL substring ")

                        markett = "COMPUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBXMT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "XMRUSDT"
                        #update_obv(2,marTkett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSXMT') != -1):
                        print ("Contains SELL substring ")

                        markett = "XMRUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBDAT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "DASHUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSDAT') != -1):
                        print ("Contains SELL substring ")

                        markett = "DASHUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBSOT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "SOLUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SSSOT') != -1):
                        print ("Contains SELL substring ")

                        markett = "SOLUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_linkusdt(self,markett,1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                        s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(1)
                        e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    elif (s1.find('SBNET') != -1):
                        print ("Contains BUY  substring ")

                        markett = "NEOUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.5)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SSNET') != -1):
                        print ("Contains SELL substring ")

                        markett = "NEOUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.5)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SBYFT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "YFIUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_btcusdt(self,markett,0.001)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SSYFT') != -1):
                        print ("Contains SELL substring ")

                        markett = "YFIUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_btcusdt(self,markett,0.001)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBMKT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "MKRUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SSMKT') != -1):
                        print ("Contains SELL substring ")

                        markett = "MKRUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBYFIT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "YFIIUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SSYFIT') != -1):
                        print ("Contains SELL substring ")

                        markett = "YFIIUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_ethusdt(self,markett,0.01)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBAAVT') != -1):
                        print ("Contains BUY  substring ")

                        markett = "AAVEUSDT"
                        #update_obv(2,markett)
                        #update_sweatd(2,markett)
                        close_order_sell_coin_usdt(self,markett)
                        take_order_buy_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SSAAVT') != -1):
                        print ("Contains SELL substring ")

                        markett = "AAVEUSDT"
                        #update_obv(1,markett)
                        #update_sweatd(1,markett)
                        close_order_buy_coin_usdt(self,markett)
                        take_order_sell_coin_bnbusdt(self,markett,0.1)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SBB') != -1):
                        print ("Contains BUY  substring ")

                        markett = "BNBUSD_PERP"
                        #update_sweat(2,markett)
                        #update_sweatd(2,markett)
                        take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SSB') != -1):
                        print ("Contains SELL substring ")

                        markett = "BNBUSD_PERP"
                        #update_sweat(1,markett)
                        #update_sweatd(1,markett)
                        take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('BBNBBTC') != -1):
                        print ("Contains SELL substring ")

                        #markett = "BNBBTC"
                        take_order_buy_bnbbtc(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBNBBTC') != -1):
                        print ("Contains SELL substring ")

                        #markett = "BNBBTC"
                        take_order_sell_bnbbtc(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('BBNBETH') != -1):
                        print ("Contains SELL substring ")

                        #markett = "BNBBTC"
                        take_order_buy_bnbeth(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBNBETH') != -1):
                        print ("Contains SELL substring ")

                        #markett = "BNBBTC"
                        take_order_sell_bnbeth(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('BDOGEBTC') != -1):
                        print ("Contains SELL substring ")

                        take_order_buy_dogebtc(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()

                    elif (s1.find('SDOGEBTC') != -1):
                        print ("Contains SELL substring ")

                        take_order_sell_dogebtc(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('BETHBTC') != -1):
                        print ("Contains SELL substring ")

                        take_order_buy_ethbtc(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SETHBTC') != -1):
                        print ("Contains SELL substring ")

                        take_order_sell_ethbtc(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('BBNBUSDT') != -1):
                        print ("Contains SELL substring ")
                        #markett = "BNBBTC"
                        take_order_buy_bnbusdt(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SBNBUSDT') != -1):
                        print ("Contains SELL substring ")

                        #markett = "BNBBTC"
                        take_order_sell_bnbusdt(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('BETHUSDT') != -1):
                        print ("Contains SELL substring ")

                        take_order_buy_ethusdt(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    elif (s1.find('SETHUSDT') != -1):
                        print ("Contains SELL substring ")

                        take_order_sell_ethusdt(self)
                        mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                        mail.expunge()
                    else:
                        print ("Doesn't contains given substring")
                        #take_order_buy()
                        time.sleep(1)

                    break
            else:
                print('Subject:', email_message['Subject'])
                s1 = email_message['Subject']
                if (s1.find('BUYBNB') != -1):
    
                    print ("Contains BUY  substring ")
                    markett = "BNBUSD_PERP"


                    take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                    take_order_coin_perp.take_order_buy_coin_perp_bnb(self,markett)
                    #take_order_coin_perp.take_order_sell_coin_perp_bnb(self,markett)
                    time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SELLBNB') != -1):
                    print ("Contains SELL substring ")


                    markett = "BNBUSD_PERP"

                    take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                    take_order_coin_perp.take_order_sell_coin_perp_bnb(self,markett)
                    #take_order_coin_perp.take_order_buy_coin_perp_bnb(self,markett)
                    time.sleep(1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_bnb'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('BUYDOGE') != -1):
                
                    print ("Contains BUY  substring ")
                    markett = "DOGEUSD_PERP"


                    #take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                    take_order_coin_perp.take_order_buy_coin_perp(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    #s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    #time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SELLDOGE') != -1):
                    print ("Contains SELL substring ")


                    markett = "DOGEUSD_PERP"

                    take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                    take_order_coin_perp.take_order_sell_coin_perp_p(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_doge'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('BUYBTC') != -1):
                    
                    print ("Contains BUY  substring ")
                    markett = "BTCUSD_PERP"


                    take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                    take_order_coin_perp.take_order_buy_coin_perp(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SELLBTC') != -1):
                    print ("Contains SELL substring ")


                    markett = "BTCUSD_PERP"

                    take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                    take_order_coin_perp.take_order_sell_coin_perp(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_btc'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('BUYETH') != -1):
                    
                    print ("Contains BUY  substring ")
                    markett = "ETHUSD_PERP"


                    take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                    take_order_coin_perp.take_order_buy_coin_perp_p(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SELLETH') != -1):
                    print ("Contains SELL substring ")


                    markett = "ETHUSD_PERP"

                    take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                    take_order_coin_perp.take_order_sell_coin_perp_p(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_c_s_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_c_s_profit_eth'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('LONGXRP') != -1):
                    print ("Contains BUY  substring ")

                    markett = "XRPUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_xrpusdt(self,markett,20)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longxrp') != -1):
                    print ("Contains BUY  substring ")

                    markett = "XRPUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_xrpusdt(self,markett,20)
                    #update_xrp_long2(0)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTXRP') != -1):
                    print ("Contains SELL substring ")

                    markett = "XRPUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_xrpusdt(self,markett,20)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortxrp') != -1):
                    print ("Contains SELL substring ")

                    markett = "XRPUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_xrpusdt(self,markett,20)
                    #update_xrp_short2(0)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()

                elif (s1.find('LONGXMR') != -1):
                    print ("Contains BUY  substring ")

                    markett = "XMRUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longxmr') != -1):
                    print ("Contains BUY  substring ")

                    markett = "XMRUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    #update_xmr_long2(0)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTXMR') != -1):
                    print ("Contains SELL substring ")

                    markett = "XMRUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortxmr') != -1):
                    print ("Contains SELL substring ")

                    markett = "XMRUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    #update_xmr_short2(0)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()

                elif (s1.find('LONGBCH') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BCHUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longbch') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BCHUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    #update_bch_long2(0)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTBCH') != -1):
                    print ("Contains SELL substring ")

                    markett = "BCHUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortbch') != -1):
                    print ("Contains SELL substring ")

                    markett = "BCHUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    #update_bch_short2(0)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()                        
                    
                elif (s1.find('LONGETH') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ETHUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longeth') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ETHUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    #update_eth_long2(0)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTETH') != -1):
                    print ("Contains SELL substring ")

                    markett = "ETHUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shorteth') != -1):
                    print ("Contains SELL substring ")

                    markett = "ETHUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    #update_eth_short2(0)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()     

                elif (s1.find('SBBNT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BNBUSDT"
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    #take_order_sell_coin_bnbusdt(self,markett,0.1)
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SSBNT') != -1):
                    print ("Contains SELL substring ")

                    markett = "BNBUSDT"
                    
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bnbusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SBXLT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "XLMUSDT"
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_dogeusdt(self,markett,40)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xlmusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSXLT') != -1):
                    print ("Contains SELL substring ")

                    markett = "XLMUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_dogeusdt(self,markett,40)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('LONGADA') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ADAUSDT"
                    update_ada_long1(1)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_adausdt(self,markett,20)
                    update_ada_short1(0)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longada') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ADAUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_adausdt(self,markett,20)
                    #update_ada_long2(0)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTADA') != -1):
                    print ("Contains SELL substring ")

                    markett = "ADAUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_adausdt(self,markett,20)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortada') != -1):
                    print ("Contains SELL substring ")

                    markett = "ADAUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_adausdt(self,markett,20)
                    #update_ada_short2(0)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()

                elif (s1.find('LONGAAVE') != -1):
                    print ("Contains BUY  substring ")

                    markett = "AAVEUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longaave') != -1):
                    print ("Contains BUY  substring ")

                    markett = "AAVEUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTAAVE') != -1):
                    print ("Contains SELL substring ")

                    markett = "AAVEUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortaave') != -1):
                    print ("Contains SELL substring ")

                    markett = "AAVEUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()                           


                elif (s1.find('LONGAXS') != -1):
                    print ("Contains BUY  substring ")

                    markett = "AXSUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longaxs') != -1):
                    print ("Contains BUY  substring ")

                    markett = "AXSUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_linkusdt(self,markett,1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTAXS') != -1):
                    print ("Contains SELL substring ")

                    markett = "AXSUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortaxs') != -1):
                    print ("Contains SELL substring ")

                    markett = "AXSUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()    

                elif (s1.find('LONGBTC') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BTCUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_btcusdt(self,markett,0.001)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longbtc') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BTCUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_btcusdt(self,markett,0.001)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTBTC') != -1):
                    print ("Contains SELL substring ")

                    markett = "BTCUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_btcusdt(self,markett,0.001)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortbtc') != -1):
                    print ("Contains SELL substring ")

                    markett = "BTCUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_btcusdt(self,markett,0.001)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()  

                elif (s1.find('LONGBNB') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BNBUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longbnb') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BNBUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTBNB') != -1):
                    print ("Contains SELL substring ")

                    markett = "BNBUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortbnb') != -1):
                    print ("Contains SELL substring ")

                    markett = "BNBUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 
                    
                    

                elif (s1.find('LONGETC') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ETCUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longetc') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ETCUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_linkusdt(self,markett,1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTETC') != -1):
                    print ("Contains SELL substring ")

                    markett = "ETCUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortetc') != -1):
                    print ("Contains SELL substring ")

                    markett = "ETCUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGLINK') != -1):
                    print ("Contains BUY  substring ")

                    markett = "LINKUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longlink') != -1):
                    print ("Contains BUY  substring ")

                    markett = "LINKUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_linkusdt(self,markett,1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTLINK') != -1):
                    print ("Contains SELL substring ")

                    markett = "LINKUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortlink') != -1):
                    print ("Contains SELL substring ")

                    markett = "LINKUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGLTC') != -1):
                    print ("Contains BUY  substring ")

                    markett = "LTCUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longltc') != -1):
                    print ("Contains BUY  substring ")

                    markett = "LTCUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTLTC') != -1):
                    print ("Contains SELL substring ")

                    markett = "LTCUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortltc') != -1):
                    print ("Contains SELL substring ")

                    markett = "LTCUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGMKR') != -1):
                    print ("Contains BUY  substring ")

                    markett = "MKRUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longmkr') != -1):
                    print ("Contains BUY  substring ")

                    markett = "MKRUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTMKR') != -1):
                    print ("Contains SELL substring ")

                    markett = "MKRUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortmkr') != -1):
                    print ("Contains SELL substring ")

                    markett = "MKRUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 
                    

                elif (s1.find('LONGNEO') != -1):
                    print ("Contains BUY  substring ")

                    markett = "NEOUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longneo') != -1):
                    print ("Contains BUY  substring ")

                    markett = "NEOUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_linkusdt(self,markett,1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTNEO') != -1):
                    print ("Contains SELL substring ")

                    markett = "NEOUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortneo') != -1):
                    print ("Contains SELL substring ")

                    markett = "NEOUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGQTUM') != -1):
                    print ("Contains BUY  substring ")

                    markett = "QTUMUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longqtum') != -1):
                    print ("Contains BUY  substring ")

                    markett = "QTUMUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_linkusdt(self,markett,1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTQTUM') != -1):
                    print ("Contains SELL substring ")

                    markett = "QTUMUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortqtum') != -1):
                    print ("Contains SELL substring ")

                    markett = "QTUMUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGSOL') != -1):
                    print ("Contains BUY  substring ")

                    markett = "SOLUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longsol') != -1):
                    print ("Contains BUY  substring ")

                    markett = "SOLUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_linkusdt(self,markett,1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTSOL') != -1):
                    print ("Contains SELL substring ")

                    markett = "SOLUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortsol') != -1):
                    print ("Contains SELL substring ")

                    markett = "SOLUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGUNI') != -1):
                    print ("Contains BUY  substring ")

                    markett = "UNiUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longuni') != -1):
                    print ("Contains BUY  substring ")

                    markett = "UNIUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_linkusdt(self,markett,1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTUNI') != -1):
                    print ("Contains SELL substring ")

                    markett = "UNIUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortuni') != -1):
                    print ("Contains SELL substring ")

                    markett = "UNIUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 
                    
                elif (s1.find('LONGYFIT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "YFIUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_btcusdt(self,markett,0.001)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longyfit') != -1):
                    print ("Contains BUY  substring ")

                    markett = "YFIUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_btcusdt(self,markett,0.001)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTYFIT') != -1):
                    print ("Contains SELL substring ")

                    markett = "YFIUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_btcusdt(self,markett,0.001)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortyfit') != -1):
                    print ("Contains SELL substring ")

                    markett = "YFIUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_btcusdt(self,markett,0.001)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()

                elif (s1.find('LONGYFII') != -1):
                    print ("Contains BUY  substring ")

                    markett = "YFIIUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longyfii') != -1):
                    print ("Contains BUY  substring ")

                    markett = "YFIIUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTYFII') != -1):
                    print ("Contains SELL substring ")

                    markett = "YFIIUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortyfii') != -1):
                    print ("Contains SELL substring ")

                    markett = "YFIIUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGZEC') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ZECUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longzec') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ZECUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTZEC') != -1):
                    print ("Contains SELL substring ")

                    markett = "ZECUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortzec') != -1):
                    print ("Contains SELL substring ")

                    markett = "ZECUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 

                elif (s1.find('LONGCOMP') != -1):
                    print ("Contains BUY  substring ")

                    markett = "COMPUSDT"
                    update_long1(1,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    update_short1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('longcomp') != -1):
                    print ("Contains BUY  substring ")

                    markett = "COMPUSDT"
                    update_long2(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    #update_long2(0,markett)
                    update_short2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('SHORTCOMP') != -1):
                    print ("Contains SELL substring ")

                    markett = "COMPUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short1(4,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    update_long1(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()
                elif (s1.find('shortcomp') != -1):
                    print ("Contains SELL substring ")

                    markett = "COMPUSDT"
                    close_order_buy_coin_usdt(self,markett)
                    update_short2(7,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    #update_short2(0,markett)
                    update_long2(0,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge() 



                elif (s1.find('SBAXT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "AXSUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')

                    mail.expunge()

                elif (s1.find('SSAXT') != -1):
                    print ("Contains SELL substring ")

                    markett = "AXSUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBXRT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "XRPUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_dogeusdt(self,markett,20)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SSDGT') != -1):
                    print ("Contains SELL substring ")

                    markett = "DOGEUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_dogeusdt(self,markett,40)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBDGT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "DOGEUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_dogeusdt(self,markett,40)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SSXRT') != -1):
                    print ("Contains SELL substring ")

                    markett = "XRPUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_dogeusdt(self,markett,20)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBLKT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "LINKUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSLKT') != -1):
                    print ("Contains SELL substring ")

                    markett = "LINKUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_linkusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBUNT') != -1):
                    print ("Contains BUY  substring ")
                    markett = "UNIUSDT"                        #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSUNT') != -1):
                    print ("Contains SELL substring ")

                    markett = "UNIUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_uniusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBATT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ATOMUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSATT') != -1):
                    print ("Contains SELL substring ")

                    markett = "ATOMUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_atomusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBQTT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "QTUMUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSQTT') != -1):
                    print ("Contains SELL substring ")

                    markett = "QTUMUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_qtumusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SBBTT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BTCUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_btcusdt(self,markett,0.001)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSBTT') != -1):
                    print ("Contains SELL substring ")

                    markett = "BTCUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_btcusdt(self,markett,0.001)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_btcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBETT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ETHUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSETT') != -1):
                    print ("Contains SELL substring ")

                    markett = "ETHUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ethusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBETCT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ETCUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSETCT') != -1):
                    print ("Contains SELL substring ")

                    markett = "ETCUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_etcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SBZET') != -1):
                    print ("Contains BUY  substring ")

                    markett = "ZECUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSZET') != -1):
                    print ("Contains SELL substring ")

                    markett = "ZECUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_zecusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBBCT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BCHUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_ethusdt(self,markett,0.02)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSBCT') != -1):
                    print ("Contains SELL substring ")

                    markett = "BCHUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.02)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_bchusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBLTT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "LTCUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSLTT') != -1):
                    print ("Contains SELL substring ")

                    markett = "LTCUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_ltcusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                elif (s1.find('SBCOMT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "COMPUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSCOMT') != -1):
                    print ("Contains SELL substring ")

                    markett = "COMPUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_compusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBXMT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "XMRUSDT"
                    #update_obv(2,marTkett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSXMT') != -1):
                    print ("Contains SELL substring ")

                    markett = "XMRUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_xmrusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBDAT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "DASHUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSDAT') != -1):
                    print ("Contains SELL substring ")

                    markett = "DASHUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_dashusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBSOT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "SOLUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SSSOT') != -1):
                    print ("Contains SELL substring ")

                    markett = "SOLUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_linkusdt(self,markett,1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                    s = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    time.sleep(1)
                    e = subprocess.Popen(['schtasks.exe', '/End', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    r = subprocess.Popen(['schtasks.exe', '/Run', '/TN', 'binance_n_profit_s_solusdt_perp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif (s1.find('SBNET') != -1):
                    print ("Contains BUY  substring ")

                    markett = "NEOUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.5)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SSNET') != -1):
                    print ("Contains SELL substring ")

                    markett = "NEOUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.5)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBYFT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "YFIUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_btcusdt(self,markett,0.001)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SSYFT') != -1):
                    print ("Contains SELL substring ")

                    markett = "YFIUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_btcusdt(self,markett,0.001)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBMKT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "MKRUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SSMKT') != -1):
                    print ("Contains SELL substring ")

                    markett = "MKRUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBYFIT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "YFIIUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_ethusdt(self,markett,0.01)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SSYFIT') != -1):
                    print ("Contains SELL substring ")

                    markett = "YFIIUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_ethusdt(self,markett,0.01)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBAAVT') != -1):
                    print ("Contains BUY  substring ")

                    markett = "AAVEUSDT"
                    #update_obv(2,markett)
                    #update_sweatd(2,markett)
                    close_order_sell_coin_usdt(self,markett)
                    take_order_buy_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SSAAVT') != -1):
                    print ("Contains SELL substring ")

                    markett = "AAVEUSDT"
                    #update_obv(1,markett)
                    #update_sweatd(1,markett)
                    close_order_buy_coin_usdt(self,markett)
                    take_order_sell_coin_bnbusdt(self,markett,0.1)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()




                elif (s1.find('SBB') != -1):
                    print ("Contains BUY  substring ")

                    markett = "BNBUSD_PERP"
                    #update_sweat(2,markett)
                    #update_sweatd(2,markett)
                    take_order_coin_perp.close_order_sell_coin_perp(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SSB') != -1):
                    print ("Contains SELL substring ")

                    markett = "BNBUSD_PERP"
                    #update_sweat(1,markett)
                    #update_sweatd(1,markett)
                    take_order_coin_perp.close_order_buy_coin_perp(self,markett)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('BBNBBTC') != -1):
                    print ("Contains SELL substring ")

                    #markett = "BNBBTC"
                    take_order_buy_bnbbtc(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBNBBTC') != -1):
                    print ("Contains SELL substring ")

                    #markett = "BNBBTC"
                    take_order_sell_bnbbtc(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('BBNBETH') != -1):
                    print ("Contains SELL substring ")

                    #markett = "BNBBTC"
                    take_order_buy_bnbeth(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBNBETH') != -1):
                    print ("Contains SELL substring ")

                    #markett = "BNBBTC"
                    take_order_sell_bnbeth(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('BDOGEBTC') != -1):
                    print ("Contains SELL substring ")

                    take_order_buy_dogebtc(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()

                elif (s1.find('SDOGEBTC') != -1):
                    print ("Contains SELL substring ")

                    take_order_sell_dogebtc(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('BETHBTC') != -1):
                    print ("Contains SELL substring ")

                    take_order_buy_ethbtc(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SETHBTC') != -1):
                    print ("Contains SELL substring ")

                    take_order_sell_ethbtc(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('BBNBUSDT') != -1):
                    print ("Contains SELL substring ")
                    #markett = "BNBBTC"
                    take_order_buy_bnbusdt(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SBNBUSDT') != -1):
                    print ("Contains SELL substring ")

                    #markett = "BNBBTC"
                    take_order_sell_bnbusdt(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('BETHUSDT') != -1):
                    print ("Contains SELL substring ")

                    take_order_buy_ethusdt(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                elif (s1.find('SETHUSDT') != -1):
                    print ("Contains SELL substring ")

                    take_order_sell_ethusdt(self)
                    mail.uid('store',most_recent, '+FLAGS', '\Deleted')
                    mail.expunge()
                else:
                    print ("Doesn't contains given substring")
                    #take_order_buy()
                    time.sleep(1)



        except IndexError:
            print("No new email")
        return


if __name__ == '__main__':

    g_api_key = 'mcaqArSaMAFvWHpG7ccUWsGFJdrFTvki9xzzhEV38N43kzgISWvjetCGnuipubaq'
    g_secret_key = 'DMnp9HQTloth5ERT2uahLIYDMNXRANQDpiGeWQomwFtSG9t6zb9w7OWdKhlWth93'
    o_api_key = 'Amcxty7dFik7GoIQKcEstnBUGUcizWru3KTebh41tYFJPxdLnwY9dTEAYmKxHkX2'
    o_secret_key = '4K5UxYMY6QAwRQygwVFbIl2FjG1cOXjkaUeyxO71AcWqpbuyoC1TmqqQE3hSYjQP'
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    #request_client_mon = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    market = "BNBUSDT"
    try:
        while True:
            thread1 = OkEx1(1,"get mail")
            #thread2 = Bin33(2,"Count Candle")
            #thread3 = Bin333(3,"Count Candle")
            thread1.start()
            #thread2.start()
            #thread3.start()
            thread1.join()
            #thread2.join()
            #thread3.join()
            #time.sleep(1)
            print(datetime.datetime.today())

    except IndexError as error:
        print("Exiting: with error" + "\n")
    except Exception as exception:
        print("Exiting: Exception error" +  "\n")
