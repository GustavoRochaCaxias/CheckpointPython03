
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

sistema_cadastro = {} 
eventos_reservados = {}

def adicionar_evento(sistema_cadastro,nome,tel,email,end):
    novo_evento = {}
    novo_evento["telefone"] = tel
    novo_evento["email"] = email
    novo_evento["endereço"] = end
    
    sistema_cadastro[nome]= evento
    print(f"Evento {nome} adicionado com sucesso!!!")

def lista_evento():
    print("Eventos disponíveis em nosso sistema:")
    for evento in sistema_cadastro:
        print(evento)

def reservar_vaga(eventos_reservados,nome,tel,email,end):
    novo_evento = {}
    novo_evento["telefone"] = tel
    novo_evento["email"] = email
    novo_evento["endereço"] = end
    sistema_cadastro[nome]= evento
    print(f"Evento {nome} reservado com sucesso!!!")
def evento ():
 while True:
  print("\n__AGENDA DE EVENTOS__\n")
  print(" 1. - Adicionar evento")
  print(" 2. - Listar eventos")
  print(" 3. - Reservar vaga")
  print(" 4. - Cancelar vaga")
  print(" 5. - Vizualizar Detalhes do Evento")
  print(" 6. - Salvar Dados  ")
  print(" 7. - Carregar dados")
  print(" 8. - Sair\n")   
  user_op = input("Escolha uma opção:")

  if user_op == "1":
    user_name = input("Nome do Evento: ")
    if  user_name not in sistema_cadastro:
     user_tel = input("Telefone para contato")
     user_email = input("Email para contato: ")
     user_end = input("Endereço Evento")
     adicionar_evento(sistema_cadastro,user_name,user_tel,user_email,user_end)
    else:
     print(f"Esse evento já esta no nosso sistema:{user_name}")

  elif user_op == "2":   
   lista_evento()

  elif user_op == "3":
    user_name = input("Nome do Evento: ")
    if  user_name not in eventos_reservados :
     user_tel = input("Telefone para contato")
     user_email = input("Email para contato: ")
     user_end = input("Endereço Evento")
     reservar_vaga(eventos_reservados,user_name,user_tel,user_email,user_end)
    else:
     print(f"Esse evento já esta no nosso sistema:{user_name}")
    

  if user_op == "8" :
    print("Obrigado pela escolha, até mais !!")
    break

if __name__ == "__main__":
    evento()
