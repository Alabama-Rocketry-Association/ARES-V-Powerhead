# Valve Module
# import Adafruit_BBIO.GPIO as GPIO
# import Adafruit_BBIO.PWM as PWM
import pandas as pd
import time

DF_lox_valve = pd.DataFrame(columns=['time', 'position'])
DF_met_valve = pd.DataFrame(columns=['time', 'position'])
DF_lox_vent = pd.DataFrame(columns=['time', 'position'])
DF_met_vent = pd.DataFrame(columns=['time', 'position'])
DF_p_valve = pd.DataFrame(columns=['time', 'position'])


def lox_valve(signal):
    t = time.process_time()

    if signal == 0:
        print('LOX Valve Closed')
    elif signal == 0.1:
        print('LOX Valve Partial Open')
    else:
        print('LOX Valve Full Open')

    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    global DF_lox_valve
    DF_lox_valve = DF_lox_valve.append(df)


def met_valve(signal):
    t = time.process_time()

    if signal == 0:
        print('Methane Valve Closed')
    elif signal == 0.1:
        print('Methane Valve Partial Open')
    else:
        print('Methane Valve Full Open')

    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    global DF_met_valve
    DF_met_valve = DF_met_valve.append(df)


def lox_vent(signal):
    # capture time
    t = time.process_time()
    # for testing purposes
    if signal == 0:
        print('LOX Vent Closed')
    else:
        print('LOX Vent Open')
    # save time and signal in data frame
    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    # append to global data frame
    global DF_lox_vent
    DF_lox_vent.append(df)


def met_vent(signal):
    t = time.process_time()
    if signal == 0:
        print('Methane Vent Closed')
    else:
        print('Methane Vent Open')
    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    global DF_met_vent
    DF_met_vent = DF_met_vent.append(df)


def p_valve(signal):
    t = time.process_time()
    if signal == 0:
        print('Pressurant Valve Closed')
    else:
        print('Pressurant Valve Open')
    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    global DF_p_valve
    DF_p_valve = DF_p_valve.append(df)


def save_data():
    global DF_lox_valve
    DF_lox_valve.to_pickle('lox_valve.pkl')
    global DF_met_valve
    DF_met_valve.to_pickle('met_valve.pkl')
    global DF_lox_vent
    DF_lox_vent.to_pickle('lox_vent.pkl')
    global DF_met_vent
    DF_met_vent.to_pickle('met_vent.pkl')
    global DF_p_valve
    DF_p_valve.to_pickle('p_valve.pkl')
