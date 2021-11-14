#!/usr/bin/env python
import ccxt
import config
import schedule
import time
import pandas as pd
import pandas_ta as ta
import logging
import requests
import tempfile
import copy
from binance_f import RequestClient

from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
#from make_order_coin_bnb import take_order_coin_perp
#from make_order_coin_bitkub import take_order_bitkub


from datetime import datetime
from binance.client import Client


from decimal import *
import email
import imaplib
import collections
import os

import array as arr
import threading

import math
import json


import logging
import cal_aroon_adx5_kdj9 as cal


# from binance_f import SubscriptionClient
# from binance_f.constant.test import *
# from binance_f.model import *
# from binance_f.exception.binanceapiexception import BinanceApiException

#from binance_f.base.printobject import *
pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np
# #from datetime import datetime
# #import time


# logger = logging.getLogger("binance-futures")
# logger.setLevel(level=logging.INFO)
# handler = logging.StreamHandler()
# handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# logger.addHandler(handler)

# sub_client = SubscriptionClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)


# def callback(data_type: 'SubscribeMessageType', event: 'any'):
#     if data_type == SubscribeMessageType.RESPONSE:
#         print("Event ID: ", event)
#     elif  data_type == SubscribeMessageType.PAYLOAD:
#         print("Event type: ", event.eventType)
#         print("Event time: ", event.eventTime)
#         print("Symbol: ", event.symbol)
#         print("Data:")
#         PrintBasic.print_obj(event.data)
#         sub_client.unsubscribe_all()
#     else:
#         print("Unknown Data:")
#     print()


# def error(e: 'BinanceApiException'):
#     print(e.error_code + e.error_message)

def wave2_fibonacci_check(wave2_end, wave1_start, wave1_end):
    # Wave 2 is typically 50%, 61.8%, 76.4%, or 85.4% of wave 1
    wave2_endabs = abs(wave2_end)
    wave1_startabs = abs(wave1_start)
    wave1_endabs = abs(wave1_end)
    fibonacci_ratio = [0.146, 0.236, 0.382, 0.5, 0.618, 0.764, 0.854]
    for ratio in fibonacci_ratio:
        if wave2_endabs <= (wave1_endabs - (wave1_endabs - wave1_startabs) * ratio) * 1.001 and wave2_endabs >= (
                wave1_endabs - (wave1_endabs - wave1_startabs) * ratio) * 0.995:
            return True
        # endif
    # endfor
    return False


def wave3_fibonacci_check(wave3_end, wave2_start, wave2_end):
    # Wave 3 is typically 161.8% of wave 1
    wave3_endabs = abs(wave3_end)
    wave2_startabs = abs(wave2_start)
    wave2_endabs = abs(wave2_end)
    fibonacci_ratio = [1.236, 1.618, 2.00, 2.618, 3.236, 4.236]
    for ratio in fibonacci_ratio:
        if wave3_endabs <= (wave2_endabs - (wave2_endabs - wave2_startabs) * ratio) * 1.001 and wave3_endabs >= (
                wave2_endabs - (wave2_endabs - wave2_startabs) * ratio) * 0.995:
            return True
        # endif
    # endfor
    return False


def wave4_fibonacci_check(wave4_end, wave3_start, wave3_end):
    # Wave 3 is typically 161.8% of wave 1
    wave4_endabs = abs(wave4_end)
    wave3_startabs = abs(wave3_start)
    wave3_endabs = abs(wave3_end)
    fibonacci_ratio = [0.146, 0.236, 0.382, 0.5, 0.618, 0.764, 0.854]
    for ratio in fibonacci_ratio:
        if wave4_endabs <= (wave3_endabs - (wave3_endabs - wave3_startabs) * ratio) * 1.001 and wave3_endabs >= (
                wave3_endabs - (wave3_endabs - wave3_startabs) * ratio) * 0.995:
            return True
        # endif
    # endfor
    return False


def wave5_fibonacci_check(wave5_end, wave1_start, wave1_end, wave3_start, wave3_end, wave4_end):
    wave5_endabs = abs(wave5_end)
    wave1_startabs = abs(wave1_start)
    wave1_endabs = abs(wave1_end)
    wave3_startabs = abs(wave3_start)
    wave3_endabs = abs(wave3_end)
    wave4_endabs = abs(wave4_end)

    wave5_y = wave5_endabs - wave4_endabs
    wave1_y = wave1_endabs - wave1_startabs
    wave4_y = abs(wave4_endabs - wave3_endabs)
    wave1plus3_y = wave1_y + (wave3_endabs - wave3_startabs)
    if wave5_y >= wave4_y and wave5_y <= (wave4_y * 2):
        return True
    if wave5_y >= wave1_y * 0.95 and wave5_y <= wave1_y * 1.05:
        return True
    fibonacci_ratio = [0.382, 0.618, 0.764]
    for ratio in fibonacci_ratio:
        if wave5_y <= wave1plus3_y * ratio * 1.05 and wave5_y >= wave1plus3_y * ratio * 0.95:
            return True
        # end
    # end
    return False


def diff(data):
    # accept list of any number
    output_diff = []
    for i in range(1, len(data)):
        output_diff.append((data[i - 1] - data[i]))
    # return list of number
    return output_diff


def otherThan(data, otherthan=0):
    # accept list and a anytype option
    output_otherthan = []
    for i in range(len(data)):
        if data[i] != otherthan:
            output_otherthan.append(True)
        else:
            output_otherthan.append(False)
    # return list of boolean
    return output_otherthan


def trimming(data, determineArray):
    # accept list of any type and list of boolean
    if len(data) != len(determineArray):
        raise Exception('array/list size not equal')
    filtered_data = []
    for i in range(len(data)):
        if determineArray[i]:
            filtered_data.append(data[i])
    return filtered_data


##############################################
def Alternative_ElliottWave_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave Up')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[j] > listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12 Up')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (
            listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] > listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],listofCandidateWave12[i]['x'][1],listofCandidateWave12[i]['x'][2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123 Up')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234 Up')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (
            listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],listofCandidateWave1234[i]['x'][1],listofCandidateWave1234[i]['x'][2],listofCandidateWave1234[i]['x'][3],listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345 Up')
    wavecount = 0
    if len(listofCandidateWave) >0:
        wavecount = 1
    if len(listofCandidateWave12) >0:
        wavecount = -2
    if len(listofCandidateWave123) >0:
        wavecount = 3
    if len(listofCandidateWave1234) >0:
        wavecount = -4
    if len(listofCandidateWave12345) >0:
        wavecount = 5
    return wavecount


########################################
##############################################
def Alternative_ElliottWave_label_downward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] > x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave Down')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] > listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[j] < listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12 Down')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (
            listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] < listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],listofCandidateWave12[i]['x'][1],listofCandidateWave12[i]['x'][2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and x[j] < listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (
            listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],listofCandidateWave1234[i]['x'][1],listofCandidateWave1234[i]['x'][2],listofCandidateWave1234[i]['x'][3],listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345')
    wavecount = 0
    if len(listofCandidateWave) >0:
        wavecount = -1
    if len(listofCandidateWave12) >0:
        wavecount = 2
    if len(listofCandidateWave123) >0:
        wavecount = -3
    if len(listofCandidateWave1234) >0:
        wavecount = 4
    if len(listofCandidateWave12345) >0:
        wavecount = -5
    return wavecount
########################################
# Traditional only make use of fibonacci retracement level, time interval does not necessary follow fibonacci series

##############################################


def Traditional_ElliottWave_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        # timeInterval=(listofCandidateWave[i]['z'][1]-listofCandidateWave[i]['z'][0])*0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and x[j] > listofCandidateWave[i]['x'][
                    0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0], listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        # timeInterval=(listofCandidateWave12[i]['z'][1]-listofCandidateWave12[i]['z'][0])*1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] > listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - \
                    listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - \
                    listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j], listofCandidateWave12[i]['x'][1],
                                                                               listofCandidateWave12[i]['x'][2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - \
            listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (
            listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - \
            listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][
                4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][
                4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],
                                                            listofCandidateWave1234[i]['x'][1],
                                                            listofCandidateWave1234[i]['x'][2],
                                                            listofCandidateWave1234[i]['x'][3],
                                                            listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345')
    return listofCandidateWave12345


########################################
##############################################
def Traditional_ElliottWave_label_downward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] > x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        # timeInterval=(listofCandidateWave[i]['z'][1]-listofCandidateWave[i]['z'][0])*0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and wave 2 drop destination is higher than start of wave 1
            if x[j] > listofCandidateWave[i]['x'][1] and x[j] < listofCandidateWave[i]['x'][
                    0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0], listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        # timeInterval=(listofCandidateWave12[i]['z'][1]-listofCandidateWave12[i]['z'][0])*1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and wave 3 must be the longest wave
            if x[j] < listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - \
                    listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - \
                    listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j], listofCandidateWave12[i]['x'][1],
                                                                               listofCandidateWave12[i]['x'][2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - \
            listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and wave 4 must not fall below the end of wave 1
            if x[j] > listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    listofCandidateWave12345 = []
    for i in range(len(listofCandidateWave1234)):
        startSearchIndex = listofCandidateWave1234[i]['searchIndex']
        # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
        timeInterval = (
            listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
        wave3length = listofCandidateWave1234[i]['z'][3] - \
            listofCandidateWave1234[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][
                4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][
                4] <= wave3length and wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],
                                                            listofCandidateWave1234[i]['x'][1],
                                                            listofCandidateWave1234[i]['x'][2],
                                                            listofCandidateWave1234[i]['x'][3],
                                                            listofCandidateWave1234[i]['x'][4]):
                currWave = copy.deepcopy(listofCandidateWave1234[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12345.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12345))
    print('successfully filter out candidate wave12345')
    return listofCandidateWave12345
########################################
##############################################


def Practical_ElliottWave3_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] > listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    return listofCandidateWave12


########################################
##############################################
def Practical_ElliottWave4_label_downward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] > x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] > listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] < listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (
            listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] < listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and \
                    z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - \
                    listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      1],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')
    return listofCandidateWave123
########################################
##############################################


def Practical_ElliottWave5_label_upward(data):
    v = data
    j = range(len(data))
    x = []
    z = []
    b = []
    # finding the high point and low point
    for i in range(1, len(v) - 1):
        if (v[i] <= v[i + 1] and v[i - 1] >= v[i]) or (v[i] >= v[i + 1] and v[i - 1] <= v[i]):
            # finding peaks and valleys and then place in a new matrix
            x.append(v[i])
            z.append(j[i])

            diff4x = diff(x)
            diff4x.insert(0, 1)

            diff4z = diff(x)
            diff4z.insert(0, 1)

            x = trimming(x, otherThan(diff4x, otherthan=0))
            z = trimming(z, otherThan(diff4z, otherthan=0))

            b = [x, z]
        # end
    # end
    # for each point find the first wave
    listofCandidateWave = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] < x[j]:
                wave = {
                    'x': [x[i], x[j]],
                    'z': [z[i], z[j]],
                    'searchIndex': j,
                }
                listofCandidateWave.append(wave)
            # end
        # end
    # end

    print(len(listofCandidateWave))
    print('successfully filter out candidate wave')

    listofCandidateWave12 = []

    for i in range(len(listofCandidateWave)):
        startSearchIndex = listofCandidateWave[i]['searchIndex']
        # third point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
        for j in range(startSearchIndex, len(x)):
            # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
            if x[j] < listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[
                j] > listofCandidateWave[i]['x'][0] and wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],
                                                                              listofCandidateWave[i]['x'][1]):
                currWave = copy.deepcopy(listofCandidateWave[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave12.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave12))
    print('successfully filter out candidate wave 12')
    listofCandidateWave123 = []
    for i in range(len(listofCandidateWave12)):
        startSearchIndex = listofCandidateWave12[i]['searchIndex']
        # forth point should be within 1.618+-5%? we take 1.618+*1.05=1.6989
        timeInterval = (
            listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
        for j in range(startSearchIndex, len(x)):
            # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
            if x[j] > listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and \
                    z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - \
                    listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= \
                    listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and wave3_fibonacci_check(x[j],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      1],
                                                                                                                  listofCandidateWave12[
                                                                                                                      i][
                                                                                                                      'x'][
                                                                                                                      2]):
                currWave = copy.deepcopy(listofCandidateWave12[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave123.append(currWave)

            # end
        # end
    # end
    print(len(listofCandidateWave123))
    print('successfully filter out candidate wave123')

    listofCandidateWave1234 = []
    for i in range(len(listofCandidateWave123)):
        startSearchIndex = listofCandidateWave123[i]['searchIndex']
        # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
        timeInterval = (
            listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
        wave3length = listofCandidateWave123[i]['z'][3] - \
            listofCandidateWave123[i]['z'][2]
        for j in range(startSearchIndex, len(x)):
            # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
            if x[j] < listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and \
                    x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][
                3] <= wave3length and wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],
                                                            listofCandidateWave123[i]['x'][3]):
                currWave = copy.deepcopy(listofCandidateWave123[i])
                currWave['x'].append(x[j])
                currWave['z'].append(z[j])
                currWave['searchIndex'] = j
                listofCandidateWave1234.append(currWave)

            # end
        # end
    # end

    print(len(listofCandidateWave1234))
    print('successfully filter out candidate wave1234')

    return listofCandidateWave1234
########################################

def close_order_sell_coin_usdt(self,markett):
   
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

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



            if (float(ass) >  0 and float(mPrices) < float(priceIns)):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=ass)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return


    return
def close_order_buy_coin_usdt(self,markett):

    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)
 
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


            if (float(a) > 0 and float(mPrice) > float(priceIn)):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=a)
                PrintBasic.print_obj(take_profit_coin)
                time.sleep(1)
                return

    return

def take_order_sell_coin_adausdt(self,markett,coin):
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)


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
            plostsf =  str(round(float(priceIns) +((3.00*float(priceIns))/20),5))

            if ((float(ass) <  20)):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
            if ((float(ass) >=  20) and float(ass) < 2 and float(mPrices) > float(plostsf) ):
                
                
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)

    return
def take_order_buy_coin_adausdt(self,markett,coin):
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

 
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
            plostf =  str(round(float(priceIn) +((-3.00*float(priceIn))/20),5))

            if ((float(a) < 20) ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
            if ((float(a) >= 20)  and float(a) < 40 and float(mPrice) < float(plostf)):
    
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
    return

exchange = ccxt.binanceusdm({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})

def tr(data):
    data['previous_close'] = data['close'].shift(1)
    data['high-low'] = abs(data['high'] - data['low'])
    data['high-pc'] = abs(data['high'] - data['previous_close'])
    data['low-pc'] = abs(data['low'] - data['previous_close'])

    tr = data[['high-low', 'high-pc', 'low-pc']].max(axis=1)

    return tr

def atr(data, period):
    data['tr'] = tr(data)
    atr = data['tr'].rolling(period).mean()

    return atr


def supertrend(df, period=7, atr_multiplier=4):
    #hl2 = (df['high'] + df['low']) / 2
    df['in_uptrendEW'] = True
    haha= Alternative_ElliottWave_label_upward(np.array(df[['close']].values,dtype=np.double).flatten(order='C'))
    #print(haha)

#   
#    print(haha)
 #   time.sleep(10)
    sosad= Alternative_ElliottWave_label_downward(np.array(df[['close']].values,dtype=np.double).flatten(order='C'))
    #print(sosad)
    if (haha) > 0:
        df['in_uptrendEW'] = True
    else:
        df['in_uptrendEW'] = False
    if (sosad) > 0:
        df['in_uptrendEW'] = True
    else:
        df['in_uptrendEW'] = False
    #time.sleep(10)
    wmah = df.ta.vwma(close=df['high'])
    wmal = df.ta.vwma(close=df['low'])
    df['atr'] = atr(df, period)
    df['upperband'] = wmah + (atr_multiplier * df['atr'])
    df['lowerband'] = wmal - (atr_multiplier * df['atr'])
    df['in_uptrend'] = True
    df['in_uptrendADX'] = True
    df['in_uptrendAll'] = 0

    adx = df.ta.adx()
    df = pd.concat([df,adx],axis=1)
    for current in range(1, len(df.index)):
        previous = current - 1

        if df['close'][current] > df['upperband'][previous]:
            df['in_uptrend'][current] = True
        elif df['close'][current] < df['lowerband'][previous]:
            df['in_uptrend'][current] = False
        else:
            df['in_uptrend'][current] = df['in_uptrend'][previous]

            if df['in_uptrend'][current] and df['lowerband'][current] < df['lowerband'][previous]:
                df['lowerband'][current] = df['lowerband'][previous]

            if not df['in_uptrend'][current] and df['upperband'][current] > df['upperband'][previous]:
                df['upperband'][current] = df['upperband'][previous]
        if df['ADX_14'][current] >= 14 : 
            if df['DMP_14'][current] > df['DMN_14'][current]: 
                df['in_uptrendADX'][current]= True      
            elif df['DMP_14'][current] < df['DMN_14'][current]:
                df['in_uptrendADX'][current]= False
            else:
                df['in_uptrendADX'][current]= None
        else:
            df['in_uptrendADX'][current]= None
            
        if df['in_uptrendEW'][current]==True and df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
            df['in_uptrendAll'][current]=3
            #df['close_order'][current]=False
        elif df['in_uptrendEW'][current]==False and df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
            df['in_uptrendAll'][current]=11
            #df['close_order'][current]=True
        elif df['in_uptrendEW'][current]==True and df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
            #df['close_order'][current]=False
            df['in_uptrendAll'][current]=8
        elif df['in_uptrendEW'][current]==True and df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
            #df['close_order'][current]=False
            df['in_uptrendAll'][current]=1        
        elif df['in_uptrendEW'][current]==False and df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
            #df['close_order'][current]=True  
            df['in_uptrendAll'][current]=6
        elif df['in_uptrendEW'][current]==False and df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
            #df['close_order'][current]=True
            df['in_uptrendAll'][current]=4
        elif df['in_uptrendEW'][current]==True: 
            df['in_uptrendAll'][current]=3
        elif df['in_uptrendEW'][current]==False: 
            df['in_uptrendAll'][current]=11
            #df['close_order'][current]=True               
    return df


in_position = False
    
def check_buy_sell_signals(df):
    global in_position
    self=None
    print("checking for buy and sell signals")
    print(df.tail(5))
    #print(df)
    last_row_index = len(df.index) - 1
    previous_row_index = last_row_index - 1

    # if (df['in_uptrendAll'][last_row_index] != 8):# or df['in_uptrendAll'][last_row_index] == 4) :
    #     if (df['in_uptrendAll'][previous_row_index] == 8):# or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 1):
    #         #order = exchange.create_market_buy_order('ETH/USD', 0.05)
    #     #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         close_order_buy_coin_usdt(self,'XLMUSDT')  
    #         in_position = False
    #         message = f"CLOSE POSITION LONG XLMUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("already close position, nothing to do")
    # if (df['in_uptrendAll'][last_row_index] != 22):# or df['in_uptrendAll'][last_row_index] == 1) :   
    #     if (df['in_uptrendAll'][previous_row_index] == 22):# or df['in_uptrendAll'][previous_row_index] == 6 or df['in_uptrendAll'][previous_row_index] == 4):
    #         #order = exchange.create_market_buy_order('ETH/USD', 0.05)
    #     #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         close_order_sell_coin_usdt(self,'XLMUSDT')  
    #         in_position = False
    #         message = f"CLOSE POSITION SHORT XLMUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("already close position, nothing to do")

  
    if df['in_uptrendAll'][last_row_index] == 8:
        print("changed to uptrend, buy")
        if not in_position:
        
            if (df['in_uptrendAll'][previous_row_index] != 8):# or df['in_uptrendAll'][previous_row_index] == 11 or df['in_uptrendAll'][previous_row_index] == 4 or df['in_uptrendAll'][previous_row_index] == 0 or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 1):
            #order = exchange.create_market_buy_order('ETH/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
                markett = "XLMUSDT"
                close_order_sell_coin_usdt(self,markett)

                order = take_order_buy_coin_adausdt(self,markett,20)
                print(order)
                in_position = True
                message = f"LONG XLMUSDT"

                payload = {
                    "username": "SignalBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("already in position, nothing to do")
            
    if df['in_uptrendAll'][last_row_index] == 22:
        if in_position:
            print("changed to downtrend, sell")
            if (df['in_uptrendAll'][previous_row_index] != 22 ):#or df['in_uptrendAll'][previous_row_index] == 8 or df['in_uptrendAll'][previous_row_index] == 3 or df['in_uptrendAll'][previous_row_index] == 0 or df['in_uptrendAll'][previous_row_index] == 6 or df['in_uptrendAll'][previous_row_index] == 4):
    
                markett = "XLMUSDT"
                close_order_buy_coin_usdt(self,markett)

                order = take_order_sell_coin_adausdt(self,markett,20)
                print(order)
                in_position = False
                message = f"SHORT XLMUSDT"

                payload = {
                    "username": "SignalBot",
                    "content": message
                }

                requests.post(WEBHOOK_URL, json=payload)
            else:
                print("You aren't in position, nothing to sell")
    # if (not df['in_uptrendAll'][previous_row_index] and df['in_uptrendAll'][last_row_index]) and  df['in_uptrendAll'][last_row_index] != 0 :
    #     print("changed to uptrend, buy")
    #     if not in_position:
    #         #order = exchange.create_market_buy_order('ETH/USD', 0.05)
    #         #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
    #         markett = "XLMUSDT"
    #         take_order_coin_perp.close_order_sell_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = True
    #         message = f"LONG XLMUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("already in position, nothing to do")
    
    # if (df['in_uptrendAll'][previous_row_index] and not df['in_uptrendAll'][last_row_index]) and  df['in_uptrendAll'][last_row_index] != 0 :
    #     if in_position:
    #         print("changed to downtrend, sell")
    #         markett = "XLMUSDT"
    #         take_order_coin_perp.close_order_buy_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = False
    #         message = f"SHORT XLMUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("You aren't in position, nothing to sell")

def run_bot():
    # print(f"Fetching new bars for {datetime.now().isoformat()}")
    # bars = exchange.fetch_ohlcv('XLMUSDT', timeframe='5m', limit=140)
    # #bars = sub_client.subscribe_candlestick_event("bnbusdt", CandlestickInterval.MIN30, callback, error)
    # df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    # df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')

    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

    bars = request_client.get_candlestick_data(symbol="XLMUSDT", interval=CandlestickInterval.MIN3,startTime=None, endTime=None, limit=100)

    object_list_open = []
    for reso in bars:
        c = collections.defaultdict()
        c['timestamp'] = float(reso.openTime)
        c['open'] = float(reso.open)
        c['high'] = float(reso.high)
        c['low'] = float(reso.low)
        c['close'] = float(reso.close)
        c['volume'] = float(reso.volume)
        object_list_open.append(c)
    df = pd.DataFrame(object_list_open[:-1])
    df['timestamp'] = pd.to_datetime(df['timestamp']+25200000, unit='ms')    
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    supertrend_data = cal.calculate_signal.supertrend(df)
    
    check_buy_sell_signals(supertrend_data)
    temp = tempfile.TemporaryFile()
    tempdir = tempfile.gettempdir()
    print(f"tempdir: {tempdir}")
    print(f"temp : {temp}")
    print(f"temp name : {temp.name}")
    temp.close()
    time.sleep(1)
    print("in position",in_position)
    time.sleep(1)

schedule.every(10).seconds.do(run_bot)
WEBHOOK_URL = "https://discord.com/api/webhooks/897722855448530974/xm9DeP4PM4vlcUpv95b5aiZ7iqIapi1uSryTbxh1vOR5IVHhl6YPQFFCI51ulycBlIDC"


while True:
    schedule.run_pending()
    time.sleep(1)