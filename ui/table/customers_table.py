from tkinter import*
from tkinter import ttk


class CustomersTable:

    def __init__(self, master=None, table_customers=[],):

        frame = Frame(master, )
        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill=Y)

        problemas = Listbox(frame, yscrollcommand=scroll.set)

        dados = ttk.Treeview(frame, columns=(
            "Nome", "Ip", "Cidades", "Descrição do Problema"), show="headings",  height=11)
        dados.column("Nome", minwidth=0, width=130)
        dados.column("Ip", minwidth=0, width=130)
        dados.column("Cidades", minwidth=0, width=150)
        dados.column("Descrição do Problema", minwidth=0, width=210)
        dados.heading("Nome", text="NOME ")
        dados.heading("Ip", text="IP")
        dados.heading("Cidades", text="CIDADES ")
        dados.heading("Descrição do Problema", text="DESCRIÇÃO DO PROBELMA")
        dados.pack()

        # populando a tabela
        for (nome, ip, cidade, descricao) in table_customers:
            dados.insert("", "end", values=(nome, ip, cidade, descricao))

        scroll.config(command=dados.yview)
        frame.pack()

        itemSelecionado = dados.selection()
        valores = dados.item(itemSelecionado, "values")
