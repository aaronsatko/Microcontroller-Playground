from machine import Pin
import utime
import random
import sys

# Initiate LED pin
led = Pin("LED", Pin.OUT)

newRecord = sys.maxsize
repetitions = 0
totalMS = 0
averageResponseTime = 0

print("When the LED lights up, press 'Enter'.")
print("LED will flash three times before each round then the game will start.")
ready = input("Ready? Y/N\n").upper()

# Make sure user is ready before starting
if ready == "Y":
    # Repeat until break
    while (True):
        # Start countdown warning
        for num in range(3):
            led.value(1)
            utime.sleep(0.25)
            led.value(0)
            utime.sleep(0.25)
        led.value(0)
        
        # Set an interval that LED may light
        randTime = random.randint(1, 10)
        
        utime.sleep(randTime + 1)
        led.value(1)
        start_time = utime.ticks_ms()
        
        # input to stop timer
        try:
            input("")
        except KeyboardInterrupt:
            # Handle Ctrl-C interrupt
            print("Interrupted by user.")
            break

        end_time = utime.ticks_ms()
        
        led.value(0)

        # Calculate the interval between the LED output and the user input
        interval = (end_time - start_time)
        
        # Calculate stats
        repetitions += 1
        totalMS += interval
        averageResponseTime = totalMS / repetitions
        
        if interval < newRecord:
            print("New newRecord:", interval, "miliseconds!")
            newRecord = interval
        else:
            print("Your response time was", interval, "miliseconds.")
        print("")
        print("You have played", repetitions, "rounds with an average of", averageResponseTime, "\b.")
        print("")
        playAgain = input("Would you like to play again? Y/N \n").upper()
        print("")

        if playAgain != "Y":
            print("Thanks for playing!")
            break
        
    

