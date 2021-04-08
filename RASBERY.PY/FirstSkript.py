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

user_input = 0
try:
    set_up_rasbery()
    while user_input != -1:
        print('Enter number (-1 to exit):')
        user_input = input()
        if type(user_input) != int or 255 < user_input or user_input < -1 :
            print('Input must a natural number not over 255! Please, try again:)')
            continue
        elif user_input == -1:
            break
        num2dac(int(user_input))
        print('Press 0 to stop process')
        int(input())
        GPIO.output(DAC, 0)

finally:
    GPIO.cleanup()
