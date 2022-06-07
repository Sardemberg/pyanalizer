from tkinter import *
from tkinter import ttk
from ui.interface.home import Home
from ui.chart.chart_bar import ChartBar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# lib matplotlib
import matplotlib.pyplot as plt
# lib pandas
import numpy as np

# Iniciando aplicação
janela = Tk()
# janela principal
janela.geometry("500x500")


# criando gerenciador de abas
nb = ttk.Notebook(janela)
nb.place(x=0, y=0, width=500, height=500)

# criação de abas
tb1 = Frame(nb)
tb2 = Frame(nb)
tb3 = Frame(nb)

# adicionando aba
nb.add(tb1, text="Principal")
nb.add(tb2, text="Gráficos")
nb.add(tb3, text="Histórioco")


# adicionando conteúdo nas abas
Home(tb1)

# loop de execução
janela.mainloop()
