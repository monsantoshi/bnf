#!/usr/bin/env python
import ccxt
import config
import schedule
import time
import pandas as pd
import pandas_ta as ta
import logging
import requests
import stockstats

from binance_f import RequestClient

from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

from binance_d import RequestClient as RequestClientD

from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *
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
import copy


import logging
import tempfile

# from binance_f import SubscriptionClient
# from binance_f.constant.test import *
# from binance_f.model import *
# from binance_f.exception.binanceapiexception import BinanceApiException

#from binance_f.base.printobject import *
pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np

exchange = ccxt.binanceusdm({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})
class calculate_signal:


    def wave2_fibonacci_check(wave2_end, wave1_start, wave1_end):
        # Wave 2 is typically 50%, 61.8%, 76.4%, or 85.4% of wave 1
        wave2_endabs = abs(wave2_end)
        wave1_startabs = abs(wave1_start)
        wave1_endabs = abs(wave1_end)
        fibonacci_ratio = [0.146, 0.236, 0.382, 0.5, 0.618, 0.764, 0.854]
        for ratio in fibonacci_ratio:
            if wave2_endabs <= (wave1_endabs - (wave1_endabs - wave1_startabs) * ratio) * 1.001 and wave2_endabs >= (wave1_endabs - (wave1_endabs - wave1_startabs) * ratio) * 0.995:
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
            if wave3_endabs <= (wave2_endabs - (wave2_endabs - wave2_startabs) * ratio) * 1.001 and wave3_endabs >= (wave2_endabs - (wave2_endabs - wave2_startabs) * ratio) * 0.995:
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
            if wave4_endabs <= (wave3_endabs - (wave3_endabs - wave3_startabs) * ratio) * 1.001 and wave3_endabs >= (wave3_endabs - (wave3_endabs - wave3_startabs) * ratio) * 0.995:
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

                diff4x = calculate_signal.diff(x)
                diff4x.insert(0, 1)

                diff4z = calculate_signal.diff(x)
                diff4z.insert(0, 1)

                x = calculate_signal.trimming(x, calculate_signal.otherThan(diff4x, otherthan=0))
                z = calculate_signal.trimming(z, calculate_signal.otherThan(diff4z, otherthan=0))

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
                if x[j] < listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[j] > listofCandidateWave[i]['x'][0] and calculate_signal.wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],listofCandidateWave[i]['x'][1]):
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
                if x[j] > listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and calculate_signal.wave3_fibonacci_check(x[j],listofCandidateWave12[i]['x'][1],listofCandidateWave12[i]['x'][2]):
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
                if x[j] < listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and x[j] > listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][3] <= wave3length and calculate_signal.wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],listofCandidateWave123[i]['x'][3]):
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
                if x[j] > listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][4] <= wave3length and calculate_signal.wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],listofCandidateWave1234[i]['x'][1],listofCandidateWave1234[i]['x'][2],listofCandidateWave1234[i]['x'][3],listofCandidateWave1234[i]['x'][4]):
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

                diff4x = calculate_signal.diff(x)
                diff4x.insert(0, 1)

                diff4z = calculate_signal.diff(x)
                diff4z.insert(0, 1)

                x = calculate_signal.trimming(x, calculate_signal.otherThan(diff4x, otherthan=0))
                z = calculate_signal.trimming(z, calculate_signal.otherThan(diff4z, otherthan=0))

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
            timeInterval = (listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
            for j in range(startSearchIndex, len(x)):
                # wave 2 is a drop and point should at around 0.382 and wave 2 drop destination is higher than start of wave 1
                if x[j] > listofCandidateWave[i]['x'][1] and z[j] - listofCandidateWave[i]['z'][1] <= timeInterval and x[j] < listofCandidateWave[i]['x'][0] and calculate_signal.wave2_fibonacci_check(x[j], listofCandidateWave[i]['x'][0],listofCandidateWave[i]['x'][1]):
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
            timeInterval = (listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
            for j in range(startSearchIndex, len(x)):
                # wave 3 is a rise and point should at around 1.618 and wave 3 must be the longest wave
                if x[j] < listofCandidateWave12[i]['x'][2] and z[j] - listofCandidateWave12[i]['z'][2] <= timeInterval and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0] and z[j] - listofCandidateWave12[i]['z'][2] >= listofCandidateWave12[i]['z'][2] - listofCandidateWave12[i]['z'][1] and calculate_signal.wave3_fibonacci_check(x[j],listofCandidateWave12[i]['x'][1],listofCandidateWave12[i]['x'][2]):
                    currWave = copy.deepcopy(listofCandidateWave12[i])
                    currWave['x'].append(x[j])
                    currWave['z'].append(z[j])
                    currWave['searchIndex'] = j
                    listofCandidateWave123.append(currWave)

                # end
            # end
        # end
        print(len(listofCandidateWave123))
        print('successfully filter out candidate wave123 Down')

        listofCandidateWave1234 = []
        for i in range(len(listofCandidateWave123)):
            startSearchIndex = listofCandidateWave123[i]['searchIndex']
            # forth point should be within 0.382+-5%? we take 0.382+*1.05=0.4011
            timeInterval = (listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
            wave3length = listofCandidateWave123[i]['z'][3] - listofCandidateWave123[i]['z'][2]
            for j in range(startSearchIndex, len(x)):
                # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
                if x[j] > listofCandidateWave123[i]['x'][3] and z[j] - listofCandidateWave123[i]['z'][3] <= timeInterval and x[j] < listofCandidateWave123[i]['x'][1] and z[j] - listofCandidateWave123[i]['z'][3] <= wave3length and calculate_signal.wave4_fibonacci_check(x[j], listofCandidateWave123[i]['x'][2],listofCandidateWave123[i]['x'][3]):
                    currWave = copy.deepcopy(listofCandidateWave123[i])
                    currWave['x'].append(x[j])
                    currWave['z'].append(z[j])
                    currWave['searchIndex'] = j
                    listofCandidateWave1234.append(currWave)

                # end
            # end
        # end

        print(len(listofCandidateWave1234))
        print('successfully filter out candidate wave1234 Down')

        listofCandidateWave12345 = []
        for i in range(len(listofCandidateWave1234)):
            startSearchIndex = listofCandidateWave1234[i]['searchIndex']
            # forth point should be within 01.618+-5%? we take 1.618+*1.05=0.4011
            timeInterval = (listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
            wave3length = listofCandidateWave1234[i]['z'][3] - listofCandidateWave1234[i]['z'][2]
            for j in range(startSearchIndex, len(x)):
                # wave 4 is a fall and point should at around 1.618 and wave 4 must not fall below the end of wave 1
                if x[j] < listofCandidateWave1234[i]['x'][4] and z[j] - listofCandidateWave1234[i]['z'][4] <= timeInterval and z[j] - listofCandidateWave1234[i]['z'][4] <= wave3length and calculate_signal.wave5_fibonacci_check(x[j], listofCandidateWave1234[i]['x'][0],listofCandidateWave1234[i]['x'][1],listofCandidateWave1234[i]['x'][2],listofCandidateWave1234[i]['x'][3],listofCandidateWave1234[i]['x'][4]):
                    currWave = copy.deepcopy(listofCandidateWave1234[i])
                    currWave['x'].append(x[j])
                    currWave['z'].append(z[j])
                    currWave['searchIndex'] = j
                    listofCandidateWave12345.append(currWave)

                # end
            # end
        # end
        print(len(listofCandidateWave12345))
        print('successfully filter out candidate wave12345 Down')
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

    def callKDJ(data):
        stock = stockstats.StockDataFrame.retype(data)

        data['D'] =  stock['kdjd']
        data['K'] =  stock['kdjd']
        data['J'] =  stock['kdjd']
        kdj = data[['K','D','J']].max(axis=1)
        return  kdj




    def tr(data):
        data['previous_close'] = data['close'].shift(1)
        data['high-low'] = abs(data['high'] - data['low'])
        data['high-pc'] = abs(data['high'] - data['previous_close'])
        data['low-pc'] = abs(data['low'] - data['previous_close'])

        tr = data[['high-low', 'high-pc', 'low-pc']].max(axis=1)

        return tr

    def atr(data, period):
        data['tr'] = calculate_signal.tr(data)
        atr = data['tr'].rolling(period).mean()

        return atr


    def supertrend(df, period=7, atr_multiplier=4):
        # request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)        
        # result = request_client.get_ticker_price_change_statistics()
        # object_list_ticket = []
        # for reso in result:
        #     c = collections.defaultdict()
        #     c['symbol'] = reso.symbol
        #     c['priceMax'] = reso.highPrice
        #     c['priceMin'] = reso.lowPrice
        #     c['lastPrice'] = reso.lastPrice
        #     c['priceChange'] = reso.priceChange

        #     object_list_ticket.append(c)

        # for keys in object_list_ticket:
        #     if ((keys.get('symbol') == market) ):
        #         print(keys)
        #         markets = keys.get('symbol')
        #         priceMax = keys.get('priceMax')
        #         priceMin = keys.get('priceMin')
        #         lastPrice = keys.get('lastPrice')
        #         priceChange = keys.get('priceChange')
        #         print("symbol",markets)
        #         print("priceMax",priceMax)
        #         print("priceMin",priceMin)
        #         print("lastPrice",lastPrice)
        #         print("priceChange",priceChange)
                
        # df['in_uptrendEW'] = 2
        # if (priceMax) > (priceMin) and priceChange > 0:
        #     haha= calculate_signal.Alternative_ElliottWave_label_upward(np.array(df['close'].values,dtype=np.double).flatten(order='C'))
        #     print(haha)
        
        #     if (haha) > 0 and (haha) != 5:
        #         df['in_uptrendEW'] = 5
        #     else:
        #         df['in_uptrendEW'] = 11

        #     if ((priceMax) > (priceMin) or (haha) == 5) and priceChange < 0:
        #         sosad= calculate_signal.Alternative_ElliottWave_label_downward(np.array(df['close'].values,dtype=np.double).flatten(order='C'))
        #         print(sosad)

        #         if (sosad) > 0 or (sosad) != -5:
        #             df['in_uptrendEW'] = 5
        #         else:
        #             df['in_uptrendEW'] = 11
    #time.sleep(10)
        #hl2 = (df['high'] + df['low']) / 2
        #calVwma = ta.vwma(hl2,df['volume'])
        #vhigh = ta.vwma(df['high'],df['volume'])
        #vlow = ta.vwma(df['low'],df['volume'])
        #vclose = ta.vwma(df['close'],df['volume'])
        #wmah = df.ta.vwma(close=df['high'])
        #wmal = df.ta.vwma(close=df['low'])
        #df['atr'] = calculate_signal.atr(df, period)
        #df['upperband'] = hl2 + (atr_multiplier * df['atr'])
        #df['lowerband'] = hl2 - (atr_multiplier * df['atr'])
        df['in_uptrendAll'] = 0
        df['in_uptrendADX'] = True
        df['in_uptrend'] = True
        df['in_uptrendKDJ'] = True    
        s = 0
        a = 2
        k = 2
            
        supert = df.ta.supertrend(length= period,multiplier=atr_multiplier)
        adx = df.ta.adx(length=5)
        kdj = df.ta.kdj(signal=3)
        df = pd.concat([df,adx,supert,kdj],axis=1)
        for current in range(1, len(df.index)):
            previous = current - 1

            # if df['close'][current] > df['upperband'][previous]:
            #     df['in_uptrend'][current] = True
            # elif df['close'][current] < df['lowerband'][previous]:
            #     df['in_uptrend'][current] = False
            # else:
            #     df['in_uptrend'][current] = df['in_uptrend'][previous]

            #     if df['in_uptrend'][current] and df['lowerband'][current] < df['lowerband'][previous]:
            #         df['lowerband'][current] = df['lowerband'][previous]

            #     if not df['in_uptrend'][current] and df['upperband'][current] > df['upperband'][previous]:
            #         df['upperband'][current] = df['upperband'][previous]

            if df['SUPERTd_7_4.0'][current]== 1:
                df['in_uptrend'][current] = True
                s=1
            elif df['SUPERTd_7_4.0'][current]== -1:
                df['in_uptrend'][current] = False
                s=0
            else:
                df['in_uptrend'][current] = df['in_uptrend'][previous]
            if df['ADX_5'][current] >= 20 : 
                if df['DMP_5'][current] > df['DMN_5'][current]: 
                    df['in_uptrendADX'][current]= True   
                    a =1   
                elif df['DMP_5'][current] < df['DMN_5'][current]:
                    df['in_uptrendADX'][current]= False
                    a=0
                else:
                    df['in_uptrendADX'][current]= df['in_uptrendADX'][previous]
            else:
                df['in_uptrendADX'][current]= df['in_uptrendADX'][previous]
                a=2
        
            if (df['J_9_3'][current] > df['K_9_3'][current]) and (df['J_9_3'][current] > df['D_9_3'][current]) and (df['K_9_3'][current] > df['D_9_3'][current]): 

                df['in_uptrendKDJ'][current]= True  
                k = 1    
            elif (df['J_9_3'][current] < df['K_9_3'][current]) and (df['J_9_3'][current] < df['D_9_3'][current]) and (df['K_9_3'][current] < df['D_9_3'][current]):
                df['in_uptrendKDJ'][current]= False
                k = 0
            else:
                df['in_uptrendKDJ'][current]= df['in_uptrendKDJ'][previous]
                k= 2

            # if df['in_uptrendKDJ'][current]==True and df['in_uptrendADX'][current]==True and df['in_uptrend'][current] == True :
            #     #if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
            #     df['in_uptrendAll'][current]=8
            # elif df['in_uptrendKDJ'][current]==False and df['in_uptrendADX'][current]==False and df['in_uptrend'][current] == True :
            #     #if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
            #     df['in_uptrendAll'][current]=22
            # else:
            #     df['in_uptrendAll'][current]= df['in_uptrendAll'][previous]                
            if ((s == 1) and (k==1) and (a==1)):
                #if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
                df['in_uptrendAll'][current]=8
            elif ((s == 0) and (k==0) and (a==0)):
                #if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
                df['in_uptrendAll'][current]=22
            else:
                df['in_uptrendAll'][current]= df['in_uptrendAll'][previous]  
            #     # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
            #     #     #df['close_order'][current]=False
            #     #     df['in_uptrendAll'][current]=13
            #     # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
            #     #     #df['close_order'][current]=False
            #     #     df['in_uptrendAll'][current]=6  
            #     # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
            #     #     df['in_uptrendAll'][current]=16
            #     #     #df['close_order'][current]=True      
            #     # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
            #     #     #df['close_order'][current]=True  
            #     #     df['in_uptrendAll'][current]=11
            #     # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
            #     #     #df['close_order'][current]=True
            #     #     df['in_uptrendAll'][current]=9  




            # elif df['in_uptrendKDJ'][current]==False: 
            #     if df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
            #         df['in_uptrendAll'][current]=22
            #     else:
            #         df['in_uptrendAll'][current]= df['in_uptrendAll'][previous]
                    #df['close_order'][current]=True      
                # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
                #     #df['close_order'][current]=True  
                #     df['in_uptrendAll'][current]=17
                # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
                #     #df['close_order'][current]=True
                #     df['in_uptrendAll'][current]=15
                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
                #     df['in_uptrendAll'][current]=14

                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
                #     #df['close_order'][current]=False
                #     df['in_uptrendAll'][current]=19
                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
                #     #df['close_order'][current]=False
                #     df['in_uptrendAll'][current]=12       
            # if df['in_uptrendKDJ'][current]==True:
            #     df['in_uptrendAll'][current]=8      
            # elif df['in_uptrendKDJ'][current]==False:   
            #     df['in_uptrendAll'][current]=22                
        return df
