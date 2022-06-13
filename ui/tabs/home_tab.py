
from tkinter import *

from controllers.CityDAO import CityDAO
from ui.table.city_table import CityTable


class HomeTab:
    def __init__(self, master=None):
        # pegando os dados
        customer_controller = CityDAO()
        dados_problemas = customer_controller.get_city_problems()

        # criando figura onde vai fica a tabela
        self.firstContainer = Frame(master)
        self.firstContainer.place(x=20, y=80)

        # alocando conteúdo
        self.title = Label(master, text="Tabela de Visão Geral")
        self.title.place(x=18, y=25)
        CityTable(self.firstContainer, dados_problemas)
