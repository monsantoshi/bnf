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
import copy

import logging
import cal_aroon_adx5_kdj9t as cal

# from binance_f import SubscriptionClient
# from binance_f.constant.test import *
# from binance_f.model import *
# from binance_f.exception.binanceapiexception import BinanceApiException

#from binance_f.base.printobject import *
pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings('ignore')

import numpy as np

class calculate_signal:
    

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
            timeInterval = (
                listofCandidateWave[i]['z'][1] - listofCandidateWave[i]['z'][0]) * 0.4011
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
            timeInterval = (
                listofCandidateWave12[i]['z'][1] - listofCandidateWave12[i]['z'][0]) * 1.6989
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
            timeInterval = (
                listofCandidateWave123[i]['z'][1] - listofCandidateWave123[i]['z'][0]) * 0.4011
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
            timeInterval = (
                listofCandidateWave1234[i]['z'][1] - listofCandidateWave1234[i]['z'][0]) * 1.6989
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


    def supertrend(df, period=7, atr_multiplier=3):
        df['in_uptrendEW'] = 1
        haha= calculate_signal.Alternative_ElliottWave_label_upward(np.array(df['close'].values,dtype=np.double).flatten(order='C'))
        print(haha)

    #   
    #    print(haha)
    #   time.sleep(10)
        sosad= calculate_signal.Alternative_ElliottWave_label_downward(np.array(df[['close']].values,dtype=np.double).flatten(order='C'))
        print(sosad)
        if (haha) > 0:
            df['in_uptrendEW'] = 1
        else:
            df['in_uptrendEW'] = 0
        if (sosad) > 0:
            df['in_uptrendEW'] = 1
        else:
            df['in_uptrendEW'] = 0
    #time.sleep(10)
        hl2 = (df['high'] + df['low']) / 2
        calVwma = ta.vwma(hl2,df['volume'])
        wmah = df.ta.vwma(close=df['high'])
        wmal = df.ta.vwma(close=df['low'])
        df['atr'] = calculate_signal.atr(df, period)
        df['upperband'] = calVwma + (atr_multiplier * df['atr'])
        df['lowerband'] = calVwma - (atr_multiplier * df['atr'])
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
                    df['in_uptrendADX'][current]= df['in_uptrendADX'][previous]
            else:
                df['in_uptrendADX'][current]= df['in_uptrendADX'][previous]
            if df['in_uptrendEW'][current]==1:    
                if df['in_uptrendADX'][current]==True: 
                    df['in_uptrendAll'][current]=3
                else:
                    df['in_uptrendAll'][current] = df['in_uptrendAll'][previous]
                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
                #     #df['close_order'][current]=False
                #     df['in_uptrendAll'][current]=8
                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
                #     #df['close_order'][current]=False
                #     df['in_uptrendAll'][current]=1  
                # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
                #     df['in_uptrendAll'][current]=8
                #     #df['close_order'][current]=True      
                # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
                #     #df['close_order'][current]=True  
                #     df['in_uptrendAll'][current]=8
                # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
                #     #df['close_order'][current]=True
                #     df['in_uptrendAll'][current]=8  
            elif df['in_uptrendEW'][current]==0: 
                if df['in_uptrendADX'][current]==False: 
                    df['in_uptrendAll'][current]=11
                #     #df['close_order'][current]=True      
                # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
                #     #df['close_order'][current]=True  
                #     df['in_uptrendAll'][current]=6
                # elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
                #     #df['close_order'][current]=True
                #     df['in_uptrendAll'][current]=4
                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
                #     df['in_uptrendAll'][current]=6
                else:
                    df['in_uptrendAll'][current] = df['in_uptrendAll'][previous]
                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
                #     #df['close_order'][current]=False
                #     df['in_uptrendAll'][current]=6
                # elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
                #     #df['close_order'][current]=False
                #     df['in_uptrendAll'][current]=6       
         
        return df

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
            ass = str(round(float(positionAmtShort)*-1,0))
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
            a = str(round(float(positionAmtLong),4))
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
            ass = str(round(float(positionAmtShort)*-1,0))
            print("ass" ,ass)
            plostsf =  str(round(float(priceIns) +((3.00*float(priceIns))/20),4))

            if ((float(ass) <  1)):
            
                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.SELL,positionSide=PositionSide.SHORT, ordertype=OrderType.MARKET,  quantity=coin)
                PrintBasic.print_obj(take_profit_coin)
            if ((float(ass) >=  1)  and float(ass) < 40 and float(mPrices) > float(plostsf) ):
                
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
            a = str(round(float(positionAmtLong),0))
            print("a" ,a)
           # time.sleep(5)

    #         client = ("mongodb+srv://tedview33:MoN33189@cluster0.1lml2.mongodb.net/Binance?retryWrites=true&w=majority&ssl=true")


    #         db = client.Binance
    #         collection_coin = db["cut_loss"]
    #         coin_data = collection_coin.find_one({"market":markett})
            plostf =  str(round(float(priceIn) +((-3.00*float(priceIn))/20),4))

            if ((float(a) < 1) ):

                take_profit_coin = request_client.post_order(symbol=markett, side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=coin)

                PrintBasic.print_obj(take_profit_coin)
            if ((float(a) >= 1) and float(a) < 40 and float(mPrice)< float(plostf) ):
    
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

def supertrend(df, period=7, atr_multiplier=3):
    df['in_uptrendEW'] = 2
    haha= calculate_signal.Alternative_ElliottWave_label_upward(np.array(df['close'].values,dtype=np.double).flatten(order='C'))
    print(haha)

#   
#    print(haha)
#   time.sleep(10)
    sosad= calculate_signal.Alternative_ElliottWave_label_downward(np.array(df['close'].values,dtype=np.double).flatten(order='C'))
    print(sosad)
    if (haha) == 3:
        df['in_uptrendEW'] = 1
    else:
        df['in_uptrendEW'] = 2
    if (sosad) == -3:
        df['in_uptrendEW'] = 0
    else:
        df['in_uptrendEW'] = 2
#time.sleep(10)
    hl2 = (df['high'] + df['low']) / 2
    calVwma = ta.vwma(hl2,df['volume'])
    wmah = df.ta.vwma(close=df['high'])
    wmal = df.ta.vwma(close=df['low'])
    df['atr'] = calculate_signal.atr(df, period)
    df['upperband'] = calVwma + (atr_multiplier * df['atr'])
    df['lowerband'] = calVwma - (atr_multiplier * df['atr'])
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
        if df['in_uptrendEW'][current]==1:    
            if df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
                df['in_uptrendAll'][current]=3

            elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
                #df['close_order'][current]=False
                df['in_uptrendAll'][current]=8
            elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
                #df['close_order'][current]=False
                df['in_uptrendAll'][current]=1  
            elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
                df['in_uptrendAll'][current]=8
                #df['close_order'][current]=True      
            elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
                #df['close_order'][current]=True  
                df['in_uptrendAll'][current]=8
            elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
                #df['close_order'][current]=True
                df['in_uptrendAll'][current]=8  
        elif df['in_uptrendEW'][current]==0: 
            if df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==False: 
                df['in_uptrendAll'][current]=11
                #df['close_order'][current]=True      
            elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==True: 
                #df['close_order'][current]=True  
                df['in_uptrendAll'][current]=6
            elif df['in_uptrend'][current]==False and df['in_uptrendADX'][current]==None: 
                #df['close_order'][current]=True
                df['in_uptrendAll'][current]=4
            elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==True: 
                df['in_uptrendAll'][current]=6

            elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==False: 
                #df['close_order'][current]=False
                df['in_uptrendAll'][current]=6
            elif df['in_uptrend'][current]==True and df['in_uptrendADX'][current]==None: 
                #df['close_order'][current]=False
                df['in_uptrendAll'][current]=6       
        
    return df


in_position = False

def make_profit_long():
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)  
    result_open_order = request_client.get_open_orders()
    time.sleep(1)
    conts = 0
    object_list_open = []
    for reso in result_open_order:
        c = collections.defaultdict()
        #c['index'] = t
        c['symbol'] = reso.symbol
        c['orderId'] = reso.orderId
        c['side'] = reso.side
        c['origQty'] = reso.origQty
        c['positionSide'] = reso.positionSide
        c['status'] = reso.status
        c['type'] = reso.type
        #d['unRealizedProfit'] = res.unRealizedProfit
        #t = t+1
        object_list_open.append(c)
    time.sleep(1)
    for keys in object_list_open:
        #cont = 0
        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "C98USDT")  and (keys.get('type')=="LIMIT") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            conts = keys.get('origQty')
            print("market",markets)
            print("orderId",orderIds)
            print("origQty",conts)
    for keys in object_list_open:
        if ((keys.get('positionSide') =='LONG') and (keys.get('symbol') == "C98USDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "SELL")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            
            print("market",markets)
            print("orderId",orderIds)

            #time.sleep(1)
            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)
    result = request_client.get_position()

    time.sleep(1)

    object_list = []
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

        f = open ('profit.json', "r")

        data = json.loads(f.read())
        p = data['LONG']['p'] 
        pf = data['LONG']['pf'] 
        pff = data['LONG']['pff'] 
        puffs = data['LONG']['pfff'] 
        pffff = data['LONG']['pffff'] 
        plost = data['LONG']['plost'] 
        plostf = data['LONG']['plostf'] 
        plostl = data['LONG']['plostl'] 
        f.close()
        if (key.get('positionSide') =='LONG' and key.get('symbol') =='C98USDT' and key.get('positionAmt') > 0.0):
            sym = key.get('symbol')
            mPrice = key.get('markPrice')
            priceIn = key.get('entryPrice')
            positionAmtLong = key.get('positionAmt')
            a = str(round(float(positionAmtLong),0))
            try:
                p = str(round(float(priceIn) +((p* float(priceIn))/20),4))
                pf = str(round(float(priceIn) +((0.05* float(priceIn))/20),4))
                pff = str(round(float(priceIn) +((pff* float(priceIn))/20),4))
                puffs = str(round(float(priceIn) +((puffs* float(priceIn))/20),4))
                pffff = str(round(float(priceIn) +((pffff* float(priceIn))/20),4))
                ploss =  str(round(float(priceIn) +((plost*float(priceIn))/20),4))
                plostf =  str(round(float(priceIn) +((plostf*float(priceIn))/20),4))
                plostl =  str(round(float(priceIn) +((plostl*float(priceIn))/20),4))
                try:
                    cut_loss_long = request_client.post_order(symbol=sym, side=OrderSide.SELL,positionSide=PositionSide.LONG,stopPrice=plostl, ordertype=OrderType.STOP_MARKET,closePosition='True') 
                except IndexError as error:
                    print("Exiting: with error in try" + "\n")
                except Exception as exception:
                    print("Exiting: Exception error in try" +  "\n")                        
                if (mPrice >= Decimal(ploss) ):
                    try:
                        if float(conts) == 0:
                            take_profit_long = request_client.post_order(symbol=sym, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=pf, quantity=a,timeInForce='GTC')
                            #time.sleep(1)
                            conts = 0
                        if float(a) > float(conts):
                            print("conts",conts)
                            rest = float(a) - float(conts)
                            take_profit_long = request_client.post_order(symbol=sym, side=OrderSide.SELL,positionSide=PositionSide.LONG, ordertype=OrderType.LIMIT, price=pf, quantity=str(round(rest,4)),timeInForce='GTC')
                            #time.sleep(1) 
                            conts = 0
                    except IndexError as error:
                        print("Exiting: with error in try" + "\n")
                    except Exception as exception:
                        print("Exiting: Exception error in try" +  "\n")
            except IndexError as error:
                print("Exiting: with error in try" + "\n")
            except Exception as exception:
                print("Exiting: Exception error in try" +  "\n")
    return

def make_profit_short():
    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)  
    result_open_order = request_client.get_open_orders()
    time.sleep(1)
    conts = 0
    object_list_open = []
    stop_threads = False
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
        #time.sleep(1)                       



    for keys in object_list_open:
        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "C98USDT") and (keys.get('type')=="LIMIT") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            conts = keys.get('origQty')
            print("market",markets)
            print("orderId",orderIds)
            print("origQty",conts)
            #conts = keys.get('origQty')
            #print("origQty",conts)
            # conts = conts+conts
            #time.sleep(1)
    #         result_for_cancel_s = request_client.cancel_order(symbol=markets, orderId=orderIds)
        
    for keys in object_list_open:
        #cont = 0
        if ((keys.get('positionSide') =='SHORT') and (keys.get('symbol') == "C98USDT")  and (keys.get('type')=="STOP_MARKET") and (keys.get('status')=="NEW") and (keys.get('side') == "BUY")):
            markets = keys.get('symbol')
            orderIds = keys.get('orderId')
            
            print("market",markets)
            print("orderId",orderIds)

            #time.sleep(1)
            result_for_cancel_stop_market = request_client.cancel_order(symbol=markets, orderId=orderIds)   
###########################
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
        f = open ('profit.json', "r")

        data = json.loads(f.read())

        first_p = data['PROFIT']['first_profit'] 
        sec_p = data['PROFIT']['sec_profit'] 
        thr_p = data['PROFIT']['thr_profit'] 
        ps = data['SHORT']['ps'] 
        psf = data['SHORT']['psf'] 
        psff = data['SHORT']['psff'] 
        psfff = data['SHORT']['psfff'] 
        psffff = data['SHORT']['psffff'] 
        pslost = data['SHORT']['pslost'] 
        pslostf = data['SHORT']['pslostf'] 
        pslostl = data['SHORT']['pslostl'] 
        f.close()
        if (key.get('positionSide') =='SHORT' and key.get('symbol') =='C98USDT' and key.get('positionAmt') < 0.0):
            syms = key.get('symbol')
            mPrices = key.get('markPrice')
            priceIns = key.get('entryPrice')
            positionAmtShort = key.get('positionAmt')
            print(mPrices,'',priceIns,'',syms,'',positionAmtShort)
            #d = Decimal(str(mPrices))

            #pres = (d.as_tuple().exponent)*-1
            ass = str(round(float(positionAmtShort)*-1,0))
            time.sleep(1)
                
            try:
                psl=[]

                ps = str(round(float(priceIns) -((ps* float(priceIns))/20),4))

                psf = str(round(float(priceIns) -((0.05* float(priceIns))/20),4))
                psff = str(round(float(priceIns) -((psff* float(priceIns))/20),4))
                psfff = str(round(float(priceIns) -((psfff* float(priceIns))/20),4))
                psffff = str(round(float(priceIns) -((psffff* float(priceIns))/20),4))
                psloss = str(round(float(priceIns) +((pslost*float(priceIns))/20),4))
                pslostf = str(round(float(priceIns) +((pslostf*float(priceIns))/20),4))
                pslostl = str(round(float(priceIns) +((pslostl*float(priceIns))/20),4))
                try:
                    cut_loss_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT,stopPrice=pslostl,  ordertype=OrderType.STOP_MARKET, closePosition='True')
                except IndexError as error:
                    print("Exiting: with error in try" + "\n")
                except Exception as exception:
                    print("Exiting: Exception error in try" +  "\n")      

                if (mPrices <= Decimal(psloss)  and float(ass) > 0 ):
                    try:
                        if float(conts) == 0:
                            ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=psf, quantity=ass,timeInForce='GTC')
                            #ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.TRAILING_STOP_MARKET , price=psfff, quantity=ass,timeInForce='GTC')
                            #time.sleep(1)
                            conts = 0
                        if float(ass) > float(conts):
                            print("conts",conts)
                            rest = float(ass) - float(conts)
                            ake_profit_short = request_client.post_order(symbol=syms, side=OrderSide.BUY,positionSide=PositionSide.SHORT, ordertype=OrderType.LIMIT, price=psf, quantity=str(round(rest,4)),timeInForce='GTC')
                            #time.sleep(1)
                            conts = 0
                    except IndexError as error:
                        print("Exiting: with error in try" + "\n")
                    except Exception as exception:
                        print("Exiting: Exception error in try" +  "\n") 
            except IndexError as error:
                print("Exiting: with error in try" + "\n")
            except Exception as exception:
                print("Exiting: Exception error in try" +  "\n")
    return

   
def check_buy_sell_signals(df):
    global in_position
    self=None
    print("checking for buy and sell signals")
    print(df.tail(5))
    #print(df)
    last_row_index = len(df.index) - 1
    previous_row_index = last_row_index - 1

 
    if df['in_uptrendAll'][last_row_index] == 8:
        print("changed to uptrend, buy")
        if not in_position:
        
            if (df['in_uptrendAll'][previous_row_index]  != 8):
            #order = exchange.create_market_buy_order('ETH/USD', 0.05)
            #order = exchange.create_order(symbol='adausdt', side=OrderSide.BUY,positionSide=PositionSide.LONG, ordertype=OrderType.MARKET,  quantity=1)
                markett = "C98USDT"
                close_order_sell_coin_usdt(self,markett)

                order = take_order_buy_coin_adausdt(self,markett,20)
                print(order)
                in_position = True
                message = f"LONG C98USDT"

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
            if (df['in_uptrendAll'][previous_row_index] != 22):

                markett = "C98USDT"
                close_order_buy_coin_usdt(self,markett)

                order = take_order_sell_coin_adausdt(self,markett,20)
                print(order)
                in_position = False
                message = f"SHORT C98USDT"

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
    #         markett = "BTCUSDT"
    #         take_order_coin_perp.close_order_sell_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_buy_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = True
    #         message = f"LONG BTCUSDT"

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
    #         markett = "BTCUSDT"
    #         take_order_coin_perp.close_order_buy_coin_perp(self,markett)

    #         order = take_order_coin_perp.take_order_sell_coin_perp_p(self,markett,5)
    #         print(order)
    #         in_position = False
    #         message = f"SHORT BTCUSDT"

    #         payload = {
    #             "username": "SignalBot",
    #             "content": message
    #         }

    #         requests.post(WEBHOOK_URL, json=payload)
    #     else:
    #         print("You aren't in position, nothing to sell")

def run_bot():

    request_client = RequestClient(api_key=config.BINANCE_API_KEY, secret_key=config.BINANCE_SECRET_KEY)

    bars = request_client.get_candlestick_data(symbol="C98USDT", interval=CandlestickInterval.MIN3,startTime=None, endTime=None, limit=100)

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