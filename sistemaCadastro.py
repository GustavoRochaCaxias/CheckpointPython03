
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

def evento ():
 while True:
  print("\n__AGENDA DE EVENTOS__\n")
  print(" 1. - Adicionar evento")
  print(" 2. - Listar contato")
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
