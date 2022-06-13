
from tkinter import *

from controllers.CityDAO import CityDAO
from controllers.CustomersDAO import CustomersDAO
from ui.table.city_table import CityTable
from ui.table.customers_table import CustomersTable


class HomeTab:
    def __init__(self, master=None):
        # pegando os dados
        city_controller = CityDAO()
        dados_problemas = city_controller.get_city_problems()
        customer_controller = CustomersDAO()
        dados_customers = customer_controller.get_consumers_errors()

        # criando label frame que vai engloba todo conteudo
        label_frame = LabelFrame(
            master, text="Visão Geral", borderwidth=1, relief="solid")
        label_frame.place(x=20, y=10, width=680, height=520)
        # criando figura onde vai fica a tabela
        self.firstContainer = Frame(label_frame)
        self.firstContainer.place(x=60, y=20)

        self.secondContainer = Frame(label_frame)
        self.secondContainer.place(x=60, y=250)

        # criando bordas para alocar conteúdo
        self.cardFirst = Frame(master, borderwidth=1, relief="raised")
        self.cardFirst.place(x=20, y=27,  width=420, height=150,)

        # alocando conteúdo

        CityTable(self.firstContainer, dados_problemas)

        CustomersTable(self.secondContainer, dados_customers,
                       )
