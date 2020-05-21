from valve import Valve
import sensors
import time
from tkinter import *
import time


# 0 and 1 will correlate to open and close position
# still not sure what signal will be sent for the valve positions
def main():
    window = Tk()
    window.title('Powerhead Control Program')
    window.geometry('1000x720')
    lbl0 = Label(window, text='Chamber Pressure: ')
    lbl0.grid(column=0, row=7)
    p0lbl = Label(window, text='Unknown')
    p0lbl.grid(column=1, row=7)

    lbl1 = Label(window, text='Methane Pressure: ')
    lbl1.grid(column=0, row=8)
    p1lbl = Label(window, text='Unknown')
    p1lbl.grid(column=1, row=8)

    lbl2 = Label(window, text='LOX Pressure: ')
    lbl2.grid(column=0, row=9)
    p2lbl = Label(window, text='Unknown')
    p2lbl.grid(column=1, row=9)

    lbl3 = Label(window, text='Methane Base Temp: ')
    lbl3.grid(column=0, row=2)
    t0lbl = Label(window, text='Unknown')
    t0lbl.grid(column=1, row=2)

    lbl4 = Label(window, text='Methane Fill Line Temp: ')
    lbl4.grid(column=0, row=3)
    t1lbl = Label(window, text='Unknown')
    t1lbl.grid(column=1, row=3)

    lbl5 = Label(window, text='LOX Base Temp: ')
    lbl5.grid(column=0, row=4)
    t2lbl = Label(window, text='Unknown')
    t2lbl.grid(column=1, row=4)

    lbl6 = Label(window, text='LOX Fill Line Temp: ')
    lbl6.grid(column=0, row=5)
    t3lbl = Label(window, text='Unknown')
    t3lbl.grid(column=1, row=5)

    lox_main = Valve('LOX Propellant Valve', 'P8_13', 'Prop')
    met_main = Valve('Methane Propellant Valve', 'P8_19', 'Prop')
    lox_vent = Valve('LOX Vent Valve', 'P8_12', 'Solenoid')
    met_vent = Valve('Methane Vent Valve', 'P8_14', 'Solenoid')
    p_valve = Valve('Pressurant Valve', 'P8_16', 'Solenoid')

    def set_close():
        # sets all valves to the close position and also verifies the
        # connection to the valves
        lox_main.close()
        met_main.close()
        lox_vent.close()
        met_vent.close()
        p_valve.close()
        lox_main.get_state()

    # this needs to be fixed

    def bit():
        # built in test function, designed to check if every electrical
        # connection is available for communications
        if safety_check():
            print("Sensors Reading Correctly")
        else:
            print("Can't Read Sensors")
            shut_down()
        set_close()

    def safety_check():
        # TODO Greg
        data = [sensors.get_pressure(0), sensors.get_pressure(1),
                sensors.get_pressure(2)]
        if data[0] > 500:  # TODO determine actual engine pressure red-lines
            p0lbl.configure(text=data[0])
            shut_down()
            return False
        elif data[1] > 570:
            p1lbl.configure(text=data[1])
            shut_down()
            return False
        elif data[2] > 670:
            p2lbl.configure(text=data[2])
            shut_down()
            return False
        else:
            return True

    def fill(valve):
        # TODO Wills
        if valve == 0:
            v.met_vent(1)
            x = sensors.get_temperature(1)
            while x > 150:
                t1lbl.configure(text=x)
                t0lbl.configure(text=sensors.get_temperature(1))
                x = sensors.get_temperature(1)
            v.met_vent(0)
        else:
            v.lox_vent(1)
            x = sensors.get_temperature(3)
            while x > 150:
                t3lbl.configure(text=x)
                t2lbl.configure(text=sensors.get_temperature(1))
                x = sensors.get_temperature(3)
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

    def launch():
        start_up()
        for i in range(1000):
            safety_check()

    Btn1 = Button(window, text='Launch BIT', command=lambda: bit(), bg='blue')
    Btn1.grid(column=0, row=0)
    Btn2 = Button(window, text='Methane Fill', command=lambda: fill(0),
                  bg='yellow')
    Btn2.grid(column=0, row=1)
    Btn3 = Button(window, text='LOX Fill', command=lambda: fill(1),
                  bg='yellow')
    Btn3.grid(column=1, row=1)
    Btn4 = Button(window, text='Engine Start-Up', command=lambda: launch(),
                  bg='green')
    Btn4.grid(column=0, row=6)
    Btn5 = Button(window, text='Engine Shut-Down', command=lambda: shut_down(),
                  bg='red')
    Btn5.grid(column=1, row=6)
    window.mainloop()

    # # Sensor data post processing
    # data.process_sensor_data('p0.pkl')
    # data.process_sensor_data('p1.pkl')
    # data.process_sensor_data('p2.pkl')
    # data.process_sensor_data('t0.pkl')
    # data.process_sensor_data('t1.pkl')
    # data.process_sensor_data('t2.pkl')
    # data.process_sensor_data('t3.pkl')

    # Valve data post processing
    # data.process_valve_data('lox_valve.pkl')
    # data.process_valve_data('met_valve.pkl')
    # data.process_valve_data('lox_vent.pkl')
    # data.process_valve_data('met_vent.pkl')


main()
