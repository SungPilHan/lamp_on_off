from tkinter import *

class lamp:
    def __init__(self):
        self.status = 0

    def getstatus(self):
        return self.status

    def turnOn(self):
        self.status = 1

    def turnOff(self):
        self.status = 0

class interface:
    def __init__(self):
        tk = TK()
        tk.title("lamp_on_off")
        tk.resizable
