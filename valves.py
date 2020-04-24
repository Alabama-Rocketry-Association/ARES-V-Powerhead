# Valve Module
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import pandas as pd
import time

lox_valve = "P8_13"
lox_valve_df = pd.DataFrame(columns=['time', 'position'])

met_valve = "P8_19"
met_valve_df = pd.DataFrame(columns=['time', 'position'])

lox_vent = "P8_12"
GPIO.setup(lox_vent, GPIO.OUT)
lox_vent_df = pd.DataFrame(columns=['time', 'position'])

met_vent = "P8_14"
GPIO.setup(met_vent, GPIO.OUT)
met_vent_df = pd.DataFrame(columns=['time', 'position'])

p_valve = "P8_16"
GPIO.setup(p_valve, GPIO.OUT)
p_valve_df = pd.DataFrame(columns=['time', 'position'])



def operate_lox_valve(signal):
    t = time.process_time()
    global lox_valve_df
    global lox_valve
    if signal == 0:
        PWM.stop(lox_valve)
        print('LOX Valve Closed')
    elif signal == 0.1:
        PWM.start(lox_valve, 10)
        print('LOX Valve Partial Open')
    else:
        PWM.set_duty_cycle(lox_valve, 500)
        print('LOX Valve Full Open')
    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    lox_valve_df = lox_valve_df.append(df)


def operate_met_valve(signal):
    t = time.process_time()
    global met_valve_df
    global met_valve

    if signal == 0:
        PWM.stop(met_valve)
        print('Methane Valve Closed')
    elif signal == 0.1:
        PWM.start(met_valve, 10)
        print('Methane Valve Partial Open')
    else:
        PWM.set_duty_cycle(met_valve, 500)
        print('Methane Valve Full Open')

    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    met_valve_df = met_valve_df.append(df)


def operate_lox_vent(signal):
    global lox_vent_df
    # capture time
    t = time.process_time()
    # for testing purposes
    if signal == 0:
        GPIO.output(lox_vent, GPIO.LOW)
        print('LOX Vent Closed')
    else:
        GPIO.output(lox_vent, GPIO.HIGH)
        print('LOX Vent Open')
    # save time and signal in data frame
    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    # append to global data frame
    lox_vent_df.append(df)


def operate_met_vent(signal):
    t = time.process_time()
    global met_vent_df

    if signal == 0:
        GPIO.output(met_vent, GPIO.LOW)
        print('Methane Vent Closed')
    else:
        GPIO.output(met_vent, GPIO.HIGH)
        print('Methane Vent Open')
    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])

    met_vent_df = met_vent_df.append(df)


def operate_p_valve(signal):
    t = time.process_time()
    if signal == 0:
        GPIO.output(p_valve, GPIO.LOW)
        print('Pressurant Valve Closed')
    else:
        GPIO.output(p_valve, GPIO.HIGH)
        print('Pressurant Valve Open')
    df = pd.DataFrame([[t, signal]], columns=['time', 'position'])
    global p_valve_df
    p_valve_df = p_valve_df.append(df)


def save_data():
    global lox_valve_df
    lox_valve_df.to_pickle('lox_valve.pkl')
    global met_valve_df
    met_valve_df.to_pickle('met_valve.pkl')
    global lox_vent_df
    lox_vent_df.to_pickle('lox_vent.pkl')
    global met_vent_df
    met_vent_df.to_pickle('met_vent.pkl')
    global p_valve_df
    p_valve_df.to_pickle('p_valve.pkl')
