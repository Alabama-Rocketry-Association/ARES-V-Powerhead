#Sensors Module
import time
import csv
# import Adafruit_BBIO.GPIO as GPIO
# import Adafruit_BBIO.PWM as PWM

def average(data):
    return sum(data) / len(data)

def vote(data):
    #TODO Greg
    list_avg = average(data)

    diff = []
    diff.append(abs(list_avg - data[0]))
    diff.append(abs(list_avg - data[1]))
    diff.append(abs(list_avg - data[2]))
    del data[diff.index(max(diff))]

    return average(data)

def read_temperature(loc):
    #Place holder example
    t = time.time()
    temps = []
    # the appends are test data, these need to be replaced
    # with actual pin readings
    if loc == 0: #bottom of methane tank
        temps.append(150)
        temps.append(175)
        temps.append(152)
    elif loc == 1: #top of methane tank
        temps.append(150)
        temps.append(175)
        temps.append(152)
    elif loc == 2: #bottom of LOX tank
        temps.append(150)
        temps.append(175)
        temps.append(152)
    elif loc == 3: #Top of lox tank
        temps.append(150)
        temps.append(175)
        temps.append(152)
    else:
        print ('Invalid Location')
    t_dat = [t, temps]
    return t_dat
     #TODO Grant

def read_pressure(loc):
    #TODO Grant
    t = time.time()
    press = []
    #the appends are test data, these need to be replaced
    #with actual pin readings
    if loc == 0: #Combustion Chamber
        press.append(400)
        press.append(402)
        press.append(401)
    elif loc == 1: #Methane Tank
        press.append(526)
        press.append(540)
        press.append(519)
    elif loc == 2: #LOX tank
        press.append(626)
        press.append(630)
        press.append(650)
    else:
        print ('Invalid Location')
    p_dat = [t, press]
    return p_dat

def write_temperature(loc, t_dat):
    with open('temp_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        print("t_dat[1][0]: ", t_dat[1][0])
        writer.writerow({t_dat[0], t_dat[1][0], t_dat[1][1], t_dat[1][2]})

def write_pressure(loc, p_dat):
    with open('press_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        print("p_dat[1][0]: ", p_dat[1][0])
        print("p_dat[1][1]: ", p_dat[1][1])
        print("p_dat[1][2]: ", p_dat[1][2])

        writer.writerow({p_dat[0], p_dat[1][0], p_dat[1][1], p_dat[1][2]})

def get_temperature(loc):
    # TODO Greg
    t_dat = read_temperature(loc)
    write_temperature(loc, t_dat)
    return vote(t_dat[1])

def get_pressure(loc):
    # TODO Greg
    p_dat = read_pressure(loc)
    write_pressure(loc, p_dat)
    return vote(p_dat[1])
