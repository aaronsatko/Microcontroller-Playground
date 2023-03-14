from machine import Pin
import utime

# Initiate LED pin
led = Pin("LED", Pin.OUT)

speed = input("How fast do you want the output? \n 1 : Normal \n 2 : Fast (2x) \n Answer: ")

# Define times in seconds for LED output
ledTimesF = {'.' : 0.5, '-' : 1.5, ' ' : 1.5, '/' : 3.5}
ledTimesS = {'.' : 1, '-' : 3, ' ' : 3, '/' : 7}

# Morse code dictionary
morseDict = {'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-', ' ':'/'}

# Translate message into morse code and output text and LED
def translate(message):
    message = message.upper()
    
    # Convert text to mc string
    morse = ' '.join(morseDict.get(char, '') for char in message)
    print(morse)
    
    # Get times for user selected speed
    if speed == '1':
        ledTimes = ledTimesN
    else:
        ledTimes = ledTimesF
    
    # Output LED
    for symbol in morse:
        if symbol == '.':
            led.value(1)
            utime.sleep(ledTimes['.'])
            led.value(0)
            utime.sleep(ledTimes[' '])
           
        elif symbol == '-':
            led.value(1)
            utime.sleep(ledTimes['-'])
            led.value(0)
            utime.sleep(ledTimes[' '])
           
        elif symbol == ' ':
            led.value(0)
            utime.sleep(ledTimes[' '])
           
        elif symbol == '/':
            led.value(0)
            utime.sleep(ledTimes['/'])

while (True):
    inputMessage = input("Type your message here. ")
    translate(inputMessage)
    
    

        




