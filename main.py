#ARES Engine Control Software
import engine

def main():
    engine.power_on()
    engine.fill_start(0)
    engine.fill_stop(0)
    engine.fill_start(1)
    engine.fill_stop(1)
    engine.start_up()
    while True == 1:
        engine.safety_check()
#TODO Greg

main()
