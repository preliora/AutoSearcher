import os
import pyautogui as pag # Needs to be installed
import keyboard as kb # Needs to be installed
import time
import random

usedNums = []

options = {
    "delay": 3,
    "maxTimes": 100
}

print("""\nInstructions:
Press Q to exit.
Delay in between searches can be customized.

""")

input("Press enter to continue. ")

for i in range(5):
    print(str(5 - i) + " second(s) until starting...")
    time.sleep(1)

print("Starting...")

running = True

while running:
    num = random.randint(0, options["maxTimes"])

    if not num in usedNums:
        os.system("start https://www.bing.com/search?q=" + str(num))
        usedNums.append(num)

    time.sleep(options["delay"])
    
    pag.hotkey('ctrl', 'w')

    if kb.is_pressed("q"):
        running = False
        print("exiting...")

print("exited")