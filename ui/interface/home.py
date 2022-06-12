from tkinter import *

from controllers.CityDAO import CityDAO
from ui.interface.table_main import TableMain


class Home:
    def __init__(self, master=None):
        customer_controller = CityDAO()
        dados_problemas = customer_controller.get_city_problems()
        
        TableMain(master, dados_problemas)