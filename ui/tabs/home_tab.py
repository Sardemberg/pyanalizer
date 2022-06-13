
from tkinter import *

from controllers.CityDAO import CityDAO
from controllers.CustomersDAO import CustomersDAO
from ui.charts.chart_bar import ChartBar


from ui.table.city_table import CityTable


class HomeTab:
    def __init__(self, master=None):
        # pegando os dados
        city_controller = CityDAO()
        customer_controller = CustomersDAO()
        dados_problemas = city_controller.get_city_problems()
        errosChartBar = customer_controller.get_city_errors()

        # criando label frame que vai engloba todo conteudo
        label_frame = LabelFrame(
            master, text="Visão Geral", borderwidth=1, relief="solid")
        label_frame.place(x=20, y=10, width=680, height=520)
        # criando figura onde vai fica a tabela
        self.firstContainer = Frame(label_frame)
        self.firstContainer.place(x=60, y=20)

        self.secondContainer = Frame(label_frame)
        self.secondContainer.place(x=60, y=250, width=550)

        # alocando conteúdo

        CityTable(self.firstContainer, dados_problemas)
        ChartBar(self.secondContainer, errosChartBar)
