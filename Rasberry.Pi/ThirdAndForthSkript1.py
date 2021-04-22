import FirstSkript
import RPi.GPIO as GPIO
import time


def num2dac(value):
    '''
    lights up the diods
    '''
    LEDS = [24, 25, 8, 7, 12, 16, 20, 21]
    lightUp = reversed(FirstSkript.decToBinList(value))
    for a,b in zip(LEDS, lightUp):
        GPIO.output(a, a*b)

def level(value):
    l = value // 32
    if value >= 250:
        num2dac(255)
    elif value < 32:
        num2dac(0)
    elif value > 31:
        num2dac(2 ** l - 1)
    

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
            l = 0
            r = 255
            while r - l > 1:
                m = (r + l)//2
                FirstSkript.num2dac(m)
                time.sleep(0.001)
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
            time.sleep(0.001)
    finally:
        GPIO.cleanup()


main()
