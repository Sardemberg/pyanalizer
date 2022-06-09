from tkinter import *

from ui.charts.chart_bar import ChartBar
from ui.charts.chart_pie import ChartPie


class Charts:

    def __init__(self, master=None):

        self.cardFirst = Frame(master, borderwidth=1, relief="raised")
        self.cardFirst.place(x=20, y=20,  width=300, height=200,)

        self.cardSecond = Frame(master, borderwidth=1, relief="raised")
        self.cardSecond.place(x=330, y=20,  width=300, height=200,),

        self.cardThird = Frame(master, borderwidth=1, relief="raised")
        self.cardThird.place(x=20, y=240,  width=610, height=250,)

        self.firstContainer = Frame(self.cardFirst)
        self.firstContainer.place(x=0, y=10,)
        ChartPie(self.firstContainer)

        self.secondContainer = Frame(self.cardSecond)
        self.secondContainer.place(x=0, y=10,)
        ChartPie(self.secondContainer)

        self.thirdContainer = Frame(self.cardThird)
        self.thirdContainer.place(x=20, y=10,)
        ChartBar(self.thirdContainer)
