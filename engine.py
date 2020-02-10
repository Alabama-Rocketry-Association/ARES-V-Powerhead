import valves as v
import sensors
import time

def set_close():
    v.p_valve(0)
    v.lox_valve(0)
    v.lox_vent(0)
    v.met_valve(0)
    v.met_vent(0)

def bit():
    set_close()

def safety_check():
    if sensors.read_pressure(0) > 500 #TODO determine actual engine pressure redlines
        shut_down()
    elif sensors.read_pressure(1) > 570
        shut_down()
    elif sensors.read_pressure(2) > 670
        shut_down()
    #TODO Jon

def power_on():
    bit()
    safety_check()

def fill_start(valve):
    if valve == 0:
        v.met_vent(1)
    else:
        v.lox_vent(1)
    #TODO Wills

def fill_stop(valve):
    if valve == 0:
        v.met_vent(0)
    else:
        v.lox_vent(0)

def start_up():
    v.p_valve(1)
    #TODO determine time to pressurization
    time.sleep(3)
    v.lox_valve(0.1)
    v.met_valve(0.1)
    while True:
        if sensors.read_pressure(0) > 50:
            break
    v.lox_valve(1)
    v.met_valve(1)

def shut_down():
    v.p_valve(0)
    v.lox_valve(0)
    v.met_valve(0)
    v.lox_vent(1)
    v.met_vent(1)
