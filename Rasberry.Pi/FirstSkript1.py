import FirstSkript
#import RPi.GPIO as GPIO


def main():
    try:
        FirstSkript.set_up_rasbery()
        max_voltage = 3 # V
        while True:

            n = int(input("Ask comparator (-1 to exit):"))
            if n == -1:
                exit()
            elif not (0 <= n < 256):
                print("Input must be a number from 0 to 255")
                continue
            print('{:d} = {:f} V'.format(n, n/255 * max_voltage))
            FirstSkript.num2dac(n)
            if GPIO.input(COMP):
                print("MORE")
            else:
                print("LESS")
                
    finally:
        GPIO.cleanup()

main()