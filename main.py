#ARES Engine Control Software
import engine
import time
def main():
    # TODO Greg
    t0 = time.time()

    engine.power_on()

    t1 = time.time()
    t_power_on = t1 - t0


    engine.fill_start(0)

    t2 = time.time()
    t_fill_start0 = t2-t1


    engine.fill_stop(0)

    t3 = time.time()
    t_fill_stop0 = t3 - t2


    engine.fill_start(1)

    t4 = time.time()
    t_fill_start1 = t4 - t3


    engine.fill_stop(1)

    t5 = time.time()
    t_fill_stop1 = t5 - t4


    engine.start_up()

    t6 = time.time()
    t_engine_start_up = t6 - t5

    engine.safety_check()

    t7 = time.time()
    t_engine_safety_check = t7- t6

    print(t_power_on)
    print(t_fill_start0)
    print(t_fill_stop0)
    print(t_fill_start1)
    print(t_fill_stop1)
    print(t_engine_start_up)
    print(t_engine_safety_check)

main()
