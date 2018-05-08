#!/usr/bin/env python
import Tkinter as tk
from Tkinter import *
import RPi.GPIO as GPIO

class Application(tk.Frame):
    def __init__(self, master=None):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def setIndividualLED(self, pin):
        if(self.selectedLED.get() == pin):
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
    
    def setLEDs(self):
        self.setIndividualLED(16)
        self.setIndividualLED(20)
        self.setIndividualLED(21)
        
    def createWidgets(self):
        self.selectedLED = IntVar()
        self.redButton = tk.Radiobutton(self, text='Red', command=self.setLEDs, variable=self.selectedLED, value=20)
        self.greenButton = tk.Radiobutton(self, text='Green', command=self.setLEDs, variable=self.selectedLED, value=16)
        self.yellowButton = tk.Radiobutton(self, text='Yellow', command=self.setLEDs, variable=self.selectedLED, value=21)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
                
        self.redButton.grid()
        self.greenButton.grid()
        self.yellowButton.grid()
        self.quitButton.grid()

app = Application()
app.master.title('SIT210 5.1P GUI')
app.mainloop()
GPIO.cleanup()