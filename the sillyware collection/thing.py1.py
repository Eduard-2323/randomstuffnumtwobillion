from tkinter import messagebox
ison = messagebox.askquestion("warningmessage","are ya shure ya wanna do this?")
if ison == "yes":
    print("started")
else:
    print("stopped")