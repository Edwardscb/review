"""
Write a function called randomGame that selects a random number 
between 0 and 1 every 1000 milliseconds and each time that a random number 
is picked, add 1 to a counter. If the number is greater than .75, 
stop the timer and console.log the number of tries it took before we 
found a number greater than .75.
"""
from time import sleep
import random

def randomGame():
    counter = 0
    newNum = 0
    
    while (newNum < 0.75):
        newNum = random.random()
        print(newNum)
        counter += 1
        sleep(1)

    print(f"It took {counter} tries")
    
randomGame()
