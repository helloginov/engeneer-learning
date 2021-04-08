import time
import RPi.GPIO as GPIO
import numpy
import matplotlib.pyplot as plt
#import scipy 


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


frequency = int(input())
step = 1/255/frequency
time = [0] * 256
sin_value = [0] * 256
for i in range(1, 255):
    time[i] = time[i-1] + step 
    sin_value[i] = numpy.sin(time[step])
plt.plot(time, sin_value)
plt.show()
