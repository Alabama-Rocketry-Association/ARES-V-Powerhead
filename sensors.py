# Sensors Module
import Adafruit_BBIO.ADC as ADC
import csv
import time
import pandas as pd


DF_p_0 = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])
p_0 = ['P9_36', 'P9_38', 'P9_40']
DF_p_1 = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])
p_1 = ['P9_33', 'P9_35', 'P9_37']
DF_p_2 = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])
p_2 = ['P9_39', 'P9_32', 'P9_34']
DF_t_0 = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])
DF_t_1 = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])
DF_t_2 = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])
DF_t_3 = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])


def test_data_open():
    with open("temptestdata.csv", 'rU') as f:
        my_list = [list(map(int, rec)) for rec in csv.reader(f, delimiter=',')]
    return my_list


TEMPDATA = test_data_open()

Iter = 0


def average(data):
    return sum(data) / len(data)


def vote(data):
    # TODO Greg
    list_avg = average(data)
    diff = [abs(list_avg - data[0]), abs(list_avg - data[1]), abs(list_avg - data[2])]
    del data[diff.index(max(diff))]
    return average(data)


def read_temperature(loc):
    global Iter
    # Place holder example
    t = time.process_time()
    temps = []
    # the appends are test data, these need to be replaced
    # with actual pin readings
    if loc == 0:  # bottom of methane tank
        temps.append(TEMPDATA[Iter][0])
        temps.append(TEMPDATA[Iter][1])
        temps.append(TEMPDATA[Iter][2])
    elif loc == 1:  # top of methane tank
        temps.append(TEMPDATA[Iter][0])
        temps.append(TEMPDATA[Iter][1])
        temps.append(TEMPDATA[Iter][2])
    elif loc == 2:  # bottom of LOX tank
        temps.append(150)
        temps.append(175)
        temps.append(152)
    elif loc == 3:  # Top of lox tank
        temps.append(TEMPDATA[Iter][0])
        temps.append(TEMPDATA[Iter][1])
        temps.append(TEMPDATA[Iter][2])
    else:
        print('Invalid Location')
    t_dat = [t, temps]
    Iter += 1
    return t_dat
    # TODO Grant


def volt_to_psi(val):
    return (1715.465955 * (val*1.8) - 312.506433)

def calc_pressure(loc):
    # TODO fix this function
    df = pd.DataFrame(columns=['time', 'sensor0', 'sensor1', 'sensor2'])
    df.time = time.process_time()
    df.sensor0 = volt_to_psi(ADC.read(loc[0]))
    df.sensor1 = volt_to_psi(ADC.read(loc[1]))
    df.sensor2 = volt_to_psi(ADC.read(loc[2]))
    return df


def read_pressure(loc):
    # TODO Grant
    t = time.process_time()
    press = []
    # the appends are test data, these need to be replaced
    # with actual pin readings
    if loc == 0:  # Combustion Chamber
        DF_p_0.append(calc_pressure(p_0))
    elif loc == 1:  # Methane Tank
        DF_p_1.append(calc_pressure(p_1))
    elif loc == 2:  # LOX tank
        DF_p_2.append(calc_pressure(p_1))
    else:
        print('Invalid Location')
    p_dat = [t, press]
    return p_dat


def write_temperature(loc, t_dat):
    df = pd.DataFrame([[t_dat[0], t_dat[1][0], t_dat[1][1], t_dat[1][2]]], columns=['time', 'sensor0', 'sensor1',
                                                                                    'sensor2'])
    if loc == 0:
        global DF_t_0
        DF_t_0 = DF_t_0.append(df)
    elif loc == 1:
        global DF_t_1
        DF_t_1 = DF_t_1.append(df)
    elif loc == 2:
        global DF_t_2
        DF_t_2 = DF_t_2.append(df)

    elif loc == 3:
        global DF_t_3
        DF_t_3 = DF_t_3.append(df)


def write_pressure(loc, p_dat):
    df = pd.DataFrame([[p_dat[0], p_dat[1][0], p_dat[1][1], p_dat[1][2]]], columns=['time', 'sensor0', 'sensor1',
                                                                                    'sensor2'])
    if loc == 0:
        global DF_p_0
        DF_p_0 = DF_p_0.append(df)

    elif loc == 1:
        global DF_p_1
        DF_p_1 = DF_p_1.append(df)

    elif loc == 2:
        global DF_p_2
        DF_p_2 = DF_p_2.append(df)


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


def save_data():
    global DF_t_0
    DF_t_0.to_pickle('t0.pkl')
    global DF_t_1
    DF_t_1.to_pickle('t1.pkl')
    global DF_t_2
    DF_t_2.to_pickle('t2.pkl')
    global DF_t_3
    DF_t_3.to_pickle('t3.pkl')
    global DF_p_0
    DF_p_0.to_pickle('p0.pkl')
    global DF_p_1
    DF_p_1.to_pickle('p1.pkl')
    global DF_p_2
    DF_p_2.to_pickle('p2.pkl')
