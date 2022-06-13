
from tkinter import *

from controllers.CityDAO import CityDAO
from ui.table.city_table import CityTable


class HomeTab:
    def __init__(self, master=None):
        customer_controller = CityDAO()
        dados_problemas = customer_controller.get_city_problems()
        self.firstContainer = Frame(master)
        self.firstContainer.place(x=20, y=80)

        CityTable(self.firstContainer, dados_problemas)
