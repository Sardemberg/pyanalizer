# lib tkinter
from tkinter import *
from tkinter import ttk
from processing.processes import Processes
from controllers.CustomersDAO import CustomersDAO
from time import sleep

# lib pandas
import numpy as np

#import tabs
from ui.tabs.problems_tab import ProblemsTab
from ui.tabs.home_tab import HomeTab


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
nb.add(tb2, text="Problemas")


# adicionando conteúdo nas abas
HomeTab(tb1)
ProblemsTab(tb2)


# loop de execução

Processes().enqueue_ips()
count_time = 0
count_customers = CustomersDAO().get_count_customers()
count_customers = count_customers[0] / 10

if(isinstance((count_customers), int)):
    sleep(count_customers * 5)
else:
    seconds = int(count_customers) + 5
    sleep(seconds)

janela.mainloop()
