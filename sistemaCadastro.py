
""""
o sistema de cadastro vai ter as funções

criar_evento
lista_evento
reservar_vaga
cancelar_vaga
visualizar_detalhes_evento
salvar_dados
carregar_dados

a estrutura da sistema será um dicionario de dicionarios para cada função.


"""

import json

sistema_cadastro = {}

def adicionar_evento(sistema_cadastro, nome, tel, email, end):
    novo_evento = {}
    novo_evento["telefone"] = tel
    novo_evento["email"] = email
    novo_evento["endereço"] = end

    sistema_cadastro[nome] = novo_evento
    print(f"Evento {nome} adicionado com sucesso!!!")

def lista_evento():
    print("Eventos disponíveis em nosso sistema:")
    for evento in sistema_cadastro:
        print(evento)    

def reservar_vaga(nome_evento, nome_cliente):
    if nome_evento in sistema_cadastro:
        if "participantes" not in sistema_cadastro[nome_evento]:
            sistema_cadastro[nome_evento]["participantes"] = []
        participantes = sistema_cadastro[nome_evento]["participantes"]

        if nome_cliente not in participantes:
            participantes.append(nome_cliente)
            print(f"{nome_cliente} reservou uma vaga para o evento '{nome_evento}'.")
        else:
            print(f"{nome_cliente} já está registrado no evento '{nome_evento}'.")
    else:
        print(f"Evento '{nome_evento}' não encontrado.")

def cancelar_vaga(nome_evento, nome_cliente):
    if nome_evento in sistema_cadastro:
        if "participantes" in sistema_cadastro[nome_evento]:
            participantes = sistema_cadastro[nome_evento]["participantes"]

            if nome_cliente in participantes:
                participantes.remove(nome_cliente)
                print(f"{nome_cliente} cancelou a reserva para o evento '{nome_evento}'.")
            else:
                print(f"{nome_cliente} não está registrado no evento '{nome_evento}'.")
        else:
            print(f"Nenhum participante registrado para o evento '{nome_evento}'.")
    else:
        print(f"Evento '{nome_evento}' não encontrado.")

def visualizar_detalhes_evento(nome_evento):
    if nome_evento in sistema_cadastro:
        evento = sistema_cadastro[nome_evento]
        print(f"Detalhes do evento '{nome_evento}':")
        print(f"Telefone de contato: {evento['telefone']}")
        print(f"Email de contato: {evento['email']}")
        print(f"Endereço do evento: {evento['endereço']}")
        if "participantes" in evento:
            print(f"Participantes registrados: {', '.join(evento['participantes'])}")
        else:
            print("Nenhum participante registrado para este evento.")
    else:
        print(f"Evento '{nome_evento}' não encontrado.")

def salvar_dados():
    with open('eventos.json', 'w') as arquivo:
        json.dump(sistema_cadastro, arquivo)
    print("Dados salvos com sucesso!")

def carregar_dados():
    try:
        with open('eventos.json', 'r') as arquivo:
            global sistema_cadastro
            sistema_cadastro = json.load(arquivo)
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Nenhum dado foi carregado.")

def evento():
    while True:
        print("\n__AGENDA DE EVENTOS__\n")
        print(" 1. - Adicionar evento")
        print(" 2. - Listar eventos")
        print(" 3. - Reservar vaga")
        print(" 4. - Cancelar vaga")
        print(" 5. - Visualizar Detalhes do Evento")
        print(" 6. - Salvar Dados")
        print(" 7. - Carregar dados")
        print(" 8. - Sair\n")
        user_op = input("Escolha uma opção:")

        if user_op == "1":
            user_name = input("Nome do Evento: ")
            if user_name not in sistema_cadastro:
                user_tel = input("Telefone para contato: ")
                user_email = input("Email para contato: ")
                user_end = input("Endereço Evento: ")
                adicionar_evento(sistema_cadastro, user_name, user_tel, user_email, user_end)
            else:
                print(f"Esse evento já está no nosso sistema: {user_name}")

        elif user_op == "2":
            lista_evento()

        elif user_op == "3":
            nome_evento = input("Nome do Evento: ")
            nome_cliente = input("Nome do Cliente: ")
            reservar_vaga(nome_evento, nome_cliente)

        elif user_op == "4":
            nome_evento = input("Nome do Evento: ")
            nome_cliente = input("Nome do Cliente: ")
            cancelar_vaga(nome_evento, nome_cliente)

        elif user_op == "5":
            nome_evento = input("Nome do Evento: ")
            visualizar_detalhes_evento(nome_evento)

        elif user_op == "6":
            salvar_dados()

        elif user_op == "7":
            carregar_dados()

        if user_op == "8":
            print("Obrigado pela escolha, até mais !!")
            break

if __name__ == "__main__":
    evento()