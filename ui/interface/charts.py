from tkinter import *

from ui.charts.chart_bar import ChartBar
from ui.charts.chart_pie import ChartPie


class Charts:

    def __init__(self, master=None):

        self.cardFirst = Frame(master, borderwidth=1, relief="raised")
        self.cardFirst.place(x=10, y=20,  width=480, height=280,)

        self.cardSecond = Frame(master, borderwidth=1, relief="raised")
        self.cardSecond.place(x=10, y=320,  width=480, height=240,)

        self.firstContainer = Frame(self.cardFirst)
        self.firstContainer.place(x=0, y=10,)
        ChartBar(self.firstContainer)

        self.secondContainer = Frame(self.cardSecond)
        self.secondContainer.place(x=0, y=10,)
        ChartPie(self.secondContainer)
