from tkinter import *
from tkinter import ttk


class CityTable:

    def __init__(self, master=None, dados_problemas=[]):

        frame = Frame(master, )

        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill=Y)

        principal = Listbox(frame, yscrollcommand=scroll.set)

        dados = ttk.Treeview(frame, columns=(
            "Id", "Cidades", "N˚ Problemas", "Resolvidos", "Pendentes"), show="headings", height=11)
        dados.column("Id", minwidth=0, width=100)
        dados.column("Cidades", minwidth=0, width=200)
        dados.column("N˚ Problemas", minwidth=0, width=100)
        dados.column("Resolvidos", minwidth=0, width=100)
        dados.column("Pendentes", minwidth=0, width=100)
        dados.heading("Id", text="ID ")
        dados.heading("Cidades", text="CIDADES ")
        dados.heading("N˚ Problemas", text="N˚ PROBLEMAS ")
        dados.heading("Resolvidos", text="RESOLVIDOS ")
        dados.heading("Pendentes", text="PENDENTES ")
        dados.pack(side=LEFT)

        for (id, ci, np, re, pe) in dados_problemas:
            dados.insert("", "end", values=(id, ci, np, re, pe))

        scroll.config(command=dados.yview)
        frame.pack()
