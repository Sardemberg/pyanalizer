# lib tkinter
from tkinter import *
from tkinter import ttk
from ui.interface.charts import Charts
from ui.interface.home import Home
# lib pandas
import numpy as np

# Iniciando aplicação
janela = Tk()

# janela principal
janela.geometry("500x500")
janela.title("Pyanalise")


# criando gerenciador de abas
style = ttk.Style()
style.configure("TNotebook", highlightbackground="#848a98")
nb = ttk.Notebook(janela, style="TNotebook")
nb.place(x=0, y=0, width=500, height=500,)

# criação de abas
tb1 = Frame(nb)
tb2 = Frame(nb)
tb3 = Frame(nb)

# adicionando aba
nb.add(tb1, text="Principal",)
nb.add(tb2, text="Gráficos")
nb.add(tb3, text="Histórioco")


# adicionando conteúdo nas abas
Home(tb1)
Charts(tb2)
# loop de execução
janela.mainloop()
