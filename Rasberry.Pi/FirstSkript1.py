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
        while True:

            n = int(input("Ask comparator (-1 to exit):"))
            if n == -1:
                exit()
            elif not (0 <= n < 256):
                print("Input must be a number from 0 to 255")
                continue
            print('{:d} = {:f} mV'.format(n, n/255 * max_voltage))
            FirstSkript.num2dac(n)
            time.sleep(0.001)
            if GPIO.input(COMP):
                print("MORE")
            else:
                print("LESS")
                
    finally:
        GPIO.cleanup()

