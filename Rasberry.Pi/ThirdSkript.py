import time
import numpy
import matplotlib.pyplot as plt
import FirstSkript


def main():
    FirstSkript.set_up_rasbery()
    frequency = float(input('Signal frequency:'))
    times = [0] * 510
    voltage = [i for i in range(256)]
    
    for i in range(256):
        times[i] = (1/2/3.141592/frequency) * numpy.arccos(1 - voltage[i]/127.5)

    for i in range(256, 510):
        times[i] = 1/frequency - times[511 - i]

    voltage += voltage[254:0:-1]
    plt.plot(times, voltage)
    plt.show()

    how_long = float(input('Signal duration:'))
    start_time = time.time()
    output_voltage = []
    output_time = []

    while time.time() - start_time < how_long:
        new_period_starts_at = time.time()
        for t, v in zip(times, voltage):
            while time.time() - new_period_starts_at < t:
                if time.time() - start_time >= how_long:
                    break
                else:
                    continue
            FirstSkript.num2dac(v)
            output_time.append(time.time() - start_time)
            output_voltage.append(v)
    print(output_voltage)
    print(output_time)
    plt.plot(output_time, output_voltage)
    plt.show()


main()
