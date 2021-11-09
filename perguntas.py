#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa
#no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
respostas = []
cont = 1
respostas.append(str(input("Telefonou para a vítima? (S/N)")))
respostas.append(str(input("Esteve no local do crime? (S/N)")))
respostas.append(str(input("Mora perto da vítima? (S/N)")))
respostas.append(str(input("Devia para a vítima? (S/N)")))
respostas.append(str(input("Já trabalhou com a vítima? (S/N)")))
for i in range(0,4):
	if respostas[i] == 'S':
		cont = cont + 1
if cont == 2:
	print("SUSPEITA")
elif cont == 3 or cont == 4:
	print("CÚMPLICE")
elif cont == 5:
	print("ASSASINO")
else:
	print("INOCENTE")
input()