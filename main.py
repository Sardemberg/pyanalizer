# lib tkinter
from tkinter import *
from tkinter import ttk


# lib pandas
import numpy as np
from ui.tabs.charts_tab import ChartsTab

from ui.tabs.home_tab import HomeTab
from ui.tabs.problem_tab import ProblemTab

# Iniciando aplicação
janela = Tk()

# janela principal
janela.geometry("720x570")
janela.title("Pyanalise")


# criando gerenciador de abas
style = ttk.Style()
style.configure("TNotebook", highlightbackground="#d9d9d9")
nb = ttk.Notebook(janela, style="TNotebook")
nb.place(x=0, y=0, width=720, height=570,)

# criação de abas
tb1 = Frame(nb)
tb2 = Frame(nb)
tb3 = Frame(nb)

# adicionando aba
nb.add(tb1, text="Principal",)
nb.add(tb2, text="Gráficos")
nb.add(tb3, text="Problemas")


# adicionando conteúdo nas abas
HomeTab(tb1)
ChartsTab(tb2)
ProblemTab(tb3)


# loop de execução
janela.mainloop()
