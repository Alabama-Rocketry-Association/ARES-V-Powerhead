# ARES Engine Control Software
import main
import time
from tkinter import *

def gui(

def main():
    # TODO Greg
    window = Tk()
    window.title('Powerhead Control Program')
    window.geometry('720x720')
    lbl1 = Label(window, text='Combustion Chamber Pressure')
    lbl1.grid(column=0, row=0)
    p0lbl = Label(window, text='Unknown')
    p0lbl.grid(column=0, row=1)
    Btn1 = Button(window, text='Launch BIT', command=lambda: main.bit())
    Btn1.grid(column=3, row=0)
    Btn2 = Button(window, text='Methane Fill', command=lambda: main.fill(0, window))
    Btn2.grid(column=4, row=0)
    Btn3 = Button(window, text='LOX Fill', command=lambda: main.fill(1))
    Btn3.grid(column=5, row=0)

    def launch():
        main.start_up()
        for i in range(1000):
            data = main.safety_check()
            print(data[0])
            p0lbl.configure(text=data[0])
            window.update()

    Btn4 = Button(window, text='Engine Start-Up', command=lambda: launch())
    Btn4.grid(column=6, row=0)
    Btn5 = Button(window, text='Engine Shut-Down', command=lambda: main.shut_down())
    Btn5.grid(column=7, row=0)

    # data.process_valve_data('p_valve.pkl')
    window.mainloop()


main()
