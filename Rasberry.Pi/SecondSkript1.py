import FirstSkript
import RPi.GPIO as GPIO
import time


def main():
    try:
        COMP = 4
        POT = 17   
        FirstSkript.set_up_rasbery()
        GPIO.setup(COMP, GPIO.IN)
        GPIO.setup(POT, GPIO.OUT)
        GPIO.output(POT, 1)
        max_voltage = 3.3 # mV
        dig_vol = 0
        while True:
            for i in range(256):
                FirstSkript.num2dac(i)
                time.sleep(0.001)
                if GPIO.input(COMP):
                    dig_vol = i
            print('digital value: {:d}; analog value: {:f} mV'.format(dig_vol, dig_vol * max_voltage / 255))
            time.sleep(0.001)
    finally:
        GPIO.cleanup()


main()