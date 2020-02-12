# ARES Engine Control Software
import engine
import time
import data


def main():
    # TODO Greg
    t0 = time.time()

    engine.power_on()

    engine.fill(0)

    engine.fill(1)

    engine.start_up()

    for i in range(1000):
        engine.safety_check()

    engine.shut_down()

    # # Sensor data post processing
    # data.process_sensor_data('p0.pkl')
    # data.process_sensor_data('p1.pkl')
    # data.process_sensor_data('p2.pkl')
    # data.process_sensor_data('t0.pkl')
    data.process_sensor_data('t1.pkl')
    # data.process_sensor_data('t2.pkl')
    data.process_sensor_data('t3.pkl')

    # Valve data post processing
    # data.process_valve_data('lox_valve.pkl')
    # data.process_valve_data('met_valve.pkl')
    # data.process_valve_data('lox_vent.pkl')
    # data.process_valve_data('met_vent.pkl')
    # data.process_valve_data('p_valve.pkl')


main()
