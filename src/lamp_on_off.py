import tkinter as tk
NOLAMP = 5

class Lamp:
    def __init__(self):
        self.state = 0

    def getState(self):
        return self.state

    def turnOn(self):
        self.state = 1

    def turnOff(self):
        self.state = 0

class Interface(tk.Tk):
    def __init__(self):
        self.inputValue = None

        super().__init__()

        self.labels = []

        self.title("Lamp_turn_On_Off")
        x_len = str(NOLAMP*64)
        self.geometry(x_len+"x100")

        self.turnOffimage = tk.PhotoImage(file="turnOff.gif")
        self.turnOnimage = tk.PhotoImage(file="turnOn.gif")

        for i in range(0,NOLAMP):
            turnOfflabel = tk.Label(image=self.turnOffimage)
            turnOfflabel.pack(side=tk.LEFT)
            self.labels.append(turnOfflabel)

        for i in range(0,NOLAMP):
            self.bind(str(i+1), self.userInput)

        self.setCloseValue = True
        self.protocol("WM_DELETE_WINDOW", self.setClose)

    def userInput(self, event=None):
        self.inputValue = event.char
        print("push: "+self.inputValue)
        return

    def drawLamp(self, lamps):
        if lamps == None:
            self.update()
        else:
            for label in self.labels:
                label.pack_forget()
                del label

            for lamp in lamps:
                if lamp.getState() == 0:
                    turnOfflabel = tk.Label(image=self.turnOffimage)
                    turnOfflabel.pack(side=tk.LEFT)
                    self.labels.append(turnOfflabel)
                else:
                    turnOnlabel = tk.Label(image=self.turnOnimage)
                    turnOnlabel.pack(side=tk.LEFT)
                    self.labels.append(turnOnlabel)

            self.update()

    def getInput(self):
        return self.inputValue

    def resetInput(self):
        self.inputValue = None

    def setClose(self):
        self.setCloseValue = False

    def getClose(self):
        return self.setCloseValue

class Controller:
    def __init__(self, lamps=None, inter=None):
        self.lamps = lamps
        self.interface = inter

    def control(self):
        choice = self.interface.getInput()
        if choice == None:
            return None
        elif self.lamps[int(choice)-1].getState() == 0:
            self.lamps[int(choice)-1].turnOn()
            self.interface.resetInput()
        else:
            self.lamps[int(choice)-1].turnOff()
            self.interface.resetInput()

        for i in range(0, NOLAMP):
            print(self.lamps[i].getState(), end=",")
        print("")

        return self.lamps

if __name__=="__main__":
    lamps=[]
    for i in range(0,NOLAMP):
        lamp = Lamp()
        lamps.append(lamp)

    inter = Interface()
    con = Controller(lamps, inter)

    while inter.getClose():
        lamps = con.control()
        inter.drawLamp(lamps)
