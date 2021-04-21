import FirstSkript
import RPi.GPIO as GPIO
import time


def level(value):
    l = value // 32
    FirstSkript.num2dac(32 * l - 1)

def main():
    try:
        FirstSkript.set_up_rasbery()
        max_voltage = 3  #V
        while True:
            GPIO.output(COMP, 0)
            l = 0
            r = 255
            while r - l > 1:
                m = (r + l)//2
                FirstSkript.num2dac(m)
                if GPIO.input(COMP):
                    l = m
                else:
                    r = m
            if GPIO.input(COMP):
                ans = l
            else:
                ans = r
            print('digital value: {:d}; analog value: {:f}'.format(ans, ans * max_voltage / 255))
            level(ans)
            time.sleep(0.01)
    finally:
        GPIO.cleanup()
