from tkinter import *

from ui.chart.chart_bar import ChartBar


class Application:
    def __init__(self, master=None):
        self.chart_bar = ChartBar()
        self.show = False
        self.fontePadrao = ("Arial", "10")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["pady"] = 30
        self.secondContainer["padx"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 20
        self.thirdContainer["pady"] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 20
        self.fourthContainer.pack()

        self.fifthContainer = Frame(master)
        self.fifthContainer["pady"] = 20
        self.fifthContainer.pack()

        self.sixthContainer = Frame(master)
        self.sixthContainer["pady"] = 20
        self.sixthContainer.pack()

        self.titleState = Label(self.firstContainer, text="Sistema desativado")
        self.titleState["font"] = ("Arial", "10", "bold")
        self.titleState.pack(side="left")

        self.containerState = Frame(
            self.firstContainer, bg='red', height=10, width=10, )
        self.containerState.pack(side="right")

        self.buttonStart = Button(self.secondContainer,
                                  text="Iniciar análise", font=self.fontePadrao, pady=10, command=self.updateState)
        self.buttonStart.pack()

        self.showProblems = Button(self.thirdContainer,
                                   text="Problemas encontrados", font=self.fontePadrao, pady=10, height=1, width=20, command=self.showData)
        self.showProblems.pack()

        self.showCharts = Button(self.fifthContainer,
                                 text="Análise de área", font=self.fontePadrao, pady=10, height=1, width=20, command=self.showChart)
        self.showCharts.pack()

        self.listCharts = Label(self.sixthContainer,
                                text="", font=self.fontePadrao,)
        self.listCharts.pack()

    # ativa o programa
    def updateState(self):
        if self.titleState["text"] == "Sistema desativado":
            self.titleState["text"] = "Sistema Ativado"
            self.containerState['bg'] = "#45f542"
        else:
            self.titleState["text"] = "Sistema desativado"
            self.containerState['bg'] = '#f54242'
    # chamar a tabela

    def showData(self):

        self.chart_bar.showChart(self.fourthContainer, )

    # chama o gráfico

    def showChart(self):

        print("")
