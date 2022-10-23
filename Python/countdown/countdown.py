""" 
 Write a function called countdown that accepts a number as a parameter and every 1000 milliseconds 
 decrements the value and console.logs it. Once the value is 0 it should log “DONE!” and stop.
 """

from time import sleep

def countdown(num):
    x = num
    while x > 0:
        print(x)
        sleep(1)
        if x == 1:
            print("Done!")
        x -= 1

countdown(10)
