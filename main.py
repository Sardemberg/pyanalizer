from tkinter import *
from ui.chart.chart_bar import ChartBar

from ui.interface.interface import Application
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# lib matplotlib
import matplotlib.pyplot as plt
# lib pandas
import numpy as np

# Iniciando aplicação
janela = Tk()
janela.geometry("500x500")
Application(janela)


janela.mainloop()
