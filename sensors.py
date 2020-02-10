#Sensors Module
import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

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
    data = []
    data.append(150)

     #TODO Grant
def read_pressure(loc):
     #TODO Grant
def write_temperature(loc):
    #TODO Jon
def write_pressure(loc):
    #TODO Jon
def get_temperature(loc):
    #TODO Greg
def get_pressure(loc):
    #TODO Greg