#!/usr/bin/python

import tkFont
import Tkinter as tk
import PyOBD2

class Application(tk.Frame):
        
    oneLabelVar = None
    twoLabelVar = None
    threeLabelVar = None
    fourLabelVar = None 
    fiveLabelVar = None
    sixLabelVar = None

    def __init__(self):

        self.root = tk.Tk()

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.font = tkFont.Font(size=36)

        tk.Frame.__init__(self, self.root)

        self.root.grid()
        self.createWidgets()


    def createWidgets(self):

        self.oneLabelVar = tk.StringVar()
        self.twoLabelVar = tk.StringVar()
        self.threeLabelVar = tk.StringVar()
        self.fourLabelVar = tk.StringVar()
        self.fiveLabelVar = tk.StringVar()
        self.sixLabelVar = tk.StringVar()

        self.oneLabel = tk.Label(
            self.root,
            font=self.font,
            relief=tk.SUNKEN,
            textvariable=self.oneLabelVar
        )
        self.oneLabel.grid(
            row=0,
            column=0,
            sticky=tk.N+tk.S+tk.E+tk.W
        )
        self.oneLabelVar.set('1')

        self.twoLabel = tk.Label(
            self.root,
            font=self.font,
            relief=tk.SUNKEN,
            textvariable=self.twoLabelVar
        )
        self.twoLabel.grid(
            row=0,
            column=1,
            sticky=tk.N+tk.S+tk.E+tk.W
        )
        self.twoLabelVar.set('2')

        self.threeLabel = tk.Label(
            self.root,
            font=self.font,
            relief=tk.SUNKEN,
            textvariable=self.threeLabelVar
        )
        self.threeLabel.grid(
            row=0,
            column=2,
            sticky=tk.N+tk.S+tk.E+tk.W
        )
        self.threeLabelVar.set('3')

        self.fourLabel = tk.Label(
            self.root,
            font=self.font,
            relief=tk.SUNKEN,
            textvariable=self.fourLabelVar
        )
        self.fourLabel.grid(
            row=1,
            column=0,
            sticky=tk.N+tk.S+tk.E+tk.W
        )
        self.fourLabelVar.set('4')

        self.fiveLabel = tk.Label(
            self.root,
            font=self.font,
            relief=tk.SUNKEN,
            textvariable=self.fiveLabelVar
        )
        self.fiveLabel.grid(
            row=1,
            column=1,
            sticky=tk.N+tk.S+tk.E+tk.W
        )
        self.fiveLabelVar.set('5')

        self.sixLabel = tk.Label(
            self.root,
            font=self.font,
            relief=tk.SUNKEN,
            textvariable=self.sixLabelVar
        )
        self.sixLabel.grid(
            row=1,
            column=2,
            sticky=tk.N+tk.S+tk.E+tk.W
        )
        self.sixLabelVar.set('6')

if __name__ == '__main__':

    pyobd2 = PyOBD2.PyOBD2(serialport='/dev/ttyUSB1')
    pyobd2.startInterface()

    app = Application()
    app.master.title('PyOBD Gauges')

    while True:
        data = pyobd2.runMonitor()
        if data:
            app.oneLabelVar.set(
                str(
                    data['engine_coolant_temp_degF']
                ).ljust(5, '0')[:5] +
                '\ndeg F'
            )
            app.twoLabelVar.set(
                str(
                    int(data['engine_rpm'])
                ) +
                '\nRPM'
            )
            app.threeLabelVar.set(
                str(
                    data['engine_consumption_gph']
                ).ljust(5, '0')[:5] +
                '\nGPH'
            )
            app.fourLabelVar.set(
                str(
                    data['average_mpg']
                ).ljust(6, '0')[:6] +
                '\nMPGc'
            )
            app.fiveLabelVar.set(
                str(
                    data['control_module_voltage']
                ).ljust(5, '0')[:5] +
                '\nV'
            )
            app.sixLabelVar.set(
                str(
                    data['velocity_mph']
                ).ljust(5, '0')[:5] +
                '\nMPH'
            )
            app.update()
