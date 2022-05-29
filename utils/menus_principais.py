def menu():
    print("Selecione a opção que deseja realizar")
    print("0 - Sair da aplicação")
    print("1 - Iniciar anánlise")
    print("2 - Problemas por região")
    print("3 - Problemas por prioridade")
    print("4 - Clientes na espera de uma resposta a cerca da solução probelam ")
    print("5 - Problemas mais recorrentes")
    print("6 - Listas de problemas geral")

def menu_conserto(customer_controller):
    print("Selecione o usuário que deseja atualizar o status:")
    for customer in customer_controller.get_consumers_errors():
        print("--------------------")
        print(f"id: {customer[0]}, Nome: {customer[1]}, cidade: {customer[2]}")
        print("--------------------")

