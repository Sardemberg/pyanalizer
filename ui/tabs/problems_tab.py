# lib tkinter
from tkinter import *
from turtle import delay
from controllers.CustomersDAO import CustomersDAO
from controllers.HistoryDAO import HistoryDAO
from time import sleep

# importando gráficos
from ui.charts.chart_pie import ChartPie
from ui.table.customers_table import CustomersTable


class ProblemsTab:

    def __init__(self, master=None):
        # pegando dados

        # Chart Bar
       
        self. history_controller = HistoryDAO()
        customer_controller = CustomersDAO()
        table_customers = customer_controller.get_consumers_errors()

        errosChartPie = customer_controller.get_problems_errors()

        # criando label frame que vai engloba todo conteudo
        self.label_frame = LabelFrame(
            master, text="Problemas", borderwidth=1, relief="solid")
        self.label_frame.place(x=20, y=10, width=680, height=520)

        # criando figura onde vai fica os gráficos
        self.firstContainer = Frame(self.label_frame)
        self.firstContainer.place(x=20, y=20,)

        self.secondContainer = Frame(self.label_frame)
        self.secondContainer.place(x=20, y=230,)
        # alocando conteúdo

        ChartPie(self.firstContainer, errosChartPie)

        CustomersTable(self.secondContainer, table_customers,)

        self.buttom_history = Button(
            master, text="Gerar Histórico", command = self.getDocument)

        self.buttom_history.place(x=480, y=120)

        self.label_history =Label(master, text= "")
        self.label_history.place(x=430, y= 175)


    def getDocument(self):
            self.history_controller.build_file()
            self.label_history['text'] = "Documento gerado com sucesso"

