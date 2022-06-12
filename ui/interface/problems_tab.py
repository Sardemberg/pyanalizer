from tkinter import*
from tkinter import ttk

from controllers.CustomersDAO import CustomersDAO

class ProblemsTab:
    
    def __init__(self, master=None, dados_customers=[]):
        
        frame = Frame(master)

        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill=Y)
        
        problemas = Listbox(frame, yscrollcommand=scroll.set)
        print(dados_customers)
        
        dados=ttk.Treeview(frame, columns=("Nome", "Ip", "Cidades", "Descrição do Problema"), show="headings")
        dados.column("Nome", minwidth=0, width=200)
        dados.column("Ip", minwidth=0, width=130)
        dados.column("Cidades", minwidth=0, width=130)
        dados.column("Descrição do Problema", minwidth=0, width=200)
        dados.heading("Nome", text="NOME ")
        dados.heading("Ip", text="IP")
        dados.heading("Cidades", text="CIDADES ")
        dados.heading("Descrição do Problema", text="DESCRIÇÃO DO PROBELMA")
        dados.pack(side=LEFT)
        
        for (nome, ip, cidade, descricao) in dados_customers:
            dados.insert("", "end", values=(nome, ip, cidade, descricao)) 
    
        scroll.config(command=dados.yview)
        frame.place(x=10, y=50)
