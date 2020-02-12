import pandas as pd
import matplotlib.pyplot as plt


def plot_sensor_data(data):
    a = data.plot(x='time', y='sensor0')
    b = data.plot(x='time', y='sensor1')
    c = data.plot(x='time', y='sensor2')
    plt.show()


def plot_valve_data(data):
    data.plot.scatter(x='time', y='position')
    plt.show()

# def write_to_excel(data):
#     data.to_excel('foot.xlsx')


def process_sensor_data(file):
    data = pd.read_pickle(file)
    plot_sensor_data(data)
    # write_to_excel(data)


def process_valve_data(file):
    data = pd.read_pickle(file)
    plot_valve_data(data)