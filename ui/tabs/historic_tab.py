from tkinter import Frame, Label

from controllers.HistoryDAO import HistoryDAO
from ui.table.customers_table import CustomersTable


class HistoricTab:

    def __init__(self, master=None):
        # pegando os dados
        customer_controller = HistoryDAO()
        dados_customers = customer_controller.get_consumers_errors()

        # criando figura onde vai fica a tabela
        self.firstContainer = Frame(master)
        self.firstContainer.place(x=20, y=80)

        #cirando bordas para alocar conteúdo
        self.cardFirst = Frame(master, borderwidth=1, relief="raised")
        self.cardFirst.place(x=20, y=27,  width=420, height=150,)

        # alocando conteúdo
        self.title = Label(master, text="Tabela de Visão Geral")
        self.title.place(x=18, y=25)
