import FirstSkript
import RPi.GPIO as GPIO
import time


def main():
    try:
        FirstSkript.set_up_rasbery()
        max_voltage = 3  #V
        dig_vol = 0
        while True:
            GPIO.output(COMP, 0)
            for i in range(256):
                FirstSkript.num2dac(i)
                if not GPIO.input(COMP):
                    dig_vol = i
            print('digital value: {:d}; analog value: {:f}'.format(dig_vol, dig_vol * max_voltage / 255))
            time.sleep(0.01)
    finally:
        GPIO.cleanup()