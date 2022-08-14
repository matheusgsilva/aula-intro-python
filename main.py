# Aluno: Matheus Graciano da Silva - BSI - Ciência de Dados

option = input("Digite:\n1 - Para conversão de Pés para Metros.\n2 - Para Conversão de Metros para Pés.\n")
value = input("Digite o valor que deseja converter:\n")

if value:
  if option == "1":
    print((int(value) * 0.3048), "metros")
  elif option == "2":
    print((int(value) * 3.281), "pés")
  else:
    print("Opção Inválida")
else:
  print("Nenhum valor foi informado.")