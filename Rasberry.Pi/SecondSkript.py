import time
import FirstSkript
import RPi.GPIO as GPIO


def main():
    print('Enter the number of repetitions:')
    try:
        user_input = int(input())
        if type(user_input) != int or 255 < user_input or user_input < 0 :
            print('Input must a natural number! Please, try again:)')

        FirstSkript.set_up_rasbery()

        for i in range(user_input):
            for j in range(1, 255):
                FirstSkript.num2dac(j)
                time.sleep(0.005)
            for j in range(255, 1, -1):
                FirstSkript.num2dac(j)
                time.sleep(0.005)
    finally:
        GPIO.cleanup()
