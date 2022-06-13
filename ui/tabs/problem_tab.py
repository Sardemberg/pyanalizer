from tkinter import Frame, Label
from controllers.CustomersDAO import CustomersDAO
from ui.table.customers_table import CustomersTable


class ProblemTab:

    def __init__(self, master=None):
        # pegando os dados
        customer_controller = CustomersDAO()
        dados_customers = customer_controller.get_consumers_errors()

        # criando figura onde vai fica a tabela
        self.firstContainer = Frame(master)
        self.firstContainer.place(x=20, y=80)

        # alocando conteúdo
        CustomersTable(self.firstContainer, dados_customers)
        self.title = Label(master, text="Tabela de Visão Geral")
        self.title.place(x=18, y=25)
