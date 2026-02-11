from tkinter import messagebox
import pyautogui
import random
import time
ison = messagebox.askquestion("warningmessage","are ya shure ya wanna do this? \n this is preaty mutch just annoying malware")

def the_actual_thing():
    while True:
        time.sleep(0.1)
        pyautogui.move(random.randint(-100,100),random.randint(-100,100))


if ison == "yes":
    print("yippe")
    the_actual_thing()
else:
    print("stopped")