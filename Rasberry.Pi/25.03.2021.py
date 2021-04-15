import RPi.GPIO as GPIO
import time

def lightUp(ledNumber, period):
    GPIO.output(LEDS[ledNumber], 1)
    time.sleep(period)
    GPIO.output(LEDS[ledNumber], 0)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)

def runningLight(count, period, runner=1):
    GPIO.output(LEDS, not runner)
    for i in range(count):
        for e in LEDS:
            GPIO.output(e, runner)
            time.sleep(period)
            GPIO.output(e, not runner)

def runningDark(count, period):
    runningLight(count, period, runner=0)

def decToBinList(decNumber):
    binList = [0]*8
    i = 0
    while decNumber != 1:
        binList[i] = decNumber % 2
        i += 1
        decNumber //= 2
    binList[i] = 1
    return list(reversed(binList))

def lightNumber(number):
    lightUp = list(reversed(decToBinList(number)))
    for a,b in zip(LEDS, lightUp):
        GPIO.output(a, a*b)






DAC = [10,9,11,5,6,13,19,26]
LEDS = [24,25,8,7,12,16,20,21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS, GPIO.OUT)
GPIO.setup(DAC, GPIO.OUT)
GPIO.output(LEDS, 0) #turn off all the lights
GPIO.output(DAC, 0)
runningPattern(5, 1)
finally:
    GPIO.cleanup()