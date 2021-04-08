import time
import RPi.GPIO as GPIO

def decToBinList(decNumber):
    '''
    transforms dec number to bin array
    '''
    binList = [0]*8
    i = 0
    while decNumber != 1:
        binList[i] = decNumber % 2
        i += 1
        decNumber //= 2
    binList[i] = 1
    return list(reversed(binList))


def num2dac(value):
    '''
    lights up the diods
    '''
    lightUp = list(reversed(decToBinList(value)))
    for a,b in zip(DAC, lightUp):
        GPIO.output(a, a*b)


def set_up_rasbery():
    global DAC, LEDS
    DAC = [10,9,11,5,6,13,19,26]
    LEDS = [24,25,8,7,12,16,20,21]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDS, GPIO.OUT)
    GPIO.setup(DAC, GPIO.OUT)
    GPIO.output(LEDS, 0) #turn off all the lights
    GPIO.output(DAC, 0)


print('Enter the number of repetitions:')
try:
    user_input = int(input())
    if type(user_input) != int or 255 < user_input or user_input < 0 :
        print('Input must a natural number! Please, try again:)')
    set_up_rasbery()
    for i in range(user_input):
        for j in range(1, 255):
            num2dac(j)
            time.sleep(0.005)
        for j in range(255, 1, -1):
            num2dac(j)
            time.sleep(0.005)
finally:
    GPIO.cleanup()
