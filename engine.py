import valves as v
import sensors
import time


# 0 and 1 will correlate to open and close position
# still not sure what signal will be sent for the valve positions

def set_close():
    # sets all valves to the close position and also verifies the connection to the valves
    v.p_valve(0)
    v.lox_valve(0)
    v.lox_vent(0)
    v.met_valve(0)
    v.met_vent(0)


# this needs to be fixed

def bit():
    # built in test function, designed to check if every electrical connection is available for communications
    if safety_check():
        print("Sensors Reading Correctly")
    else:
        print("Can't Read Sensors")
        shut_down()
    set_close()


def safety_check():
    # TODO Greg
    if sensors.get_pressure(0) > 500:  # TODO determine actual engine pressure redlines
        shut_down()
        return False
    elif sensors.get_pressure(1) > 570:
        shut_down()
        return False
    elif sensors.get_pressure(2) > 670:
        shut_down()
        return False
    else:
        return True


def power_on():
    bit()


def fill(valve):
    # TODO Wills
    if valve == 0:
        v.met_vent(1)
        while sensors.get_temperature(1) > 150:
            continue
        v.met_vent(0)
    else:
        v.lox_vent(1)
        while sensors.get_temperature(3) > 150:
            continue
        v.lox_vent(0)


def start_up():
    v.p_valve(1)
    # TODO determine time to pressurization
    time.sleep(3)
    v.lox_valve(0.1)
    v.met_valve(0.1)
    while True:
        if sensors.get_pressure(0) > 50:
            break
    v.lox_valve(1)
    v.met_valve(1)


def shut_down():
    v.p_valve(0)
    v.lox_valve(0)
    v.met_valve(0)
    v.lox_vent(1)
    v.met_vent(1)
    sensors.save_data()
    v.save_data()
