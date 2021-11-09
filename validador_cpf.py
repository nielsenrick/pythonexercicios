import os
while True:
	print("--------------- VALIDADOR DE CPF ---------------")
	cpf = str(input("INFORME O SEU CPF (APENAS OS NÚMEROS): "))
	verificacao = 0
	for j in range(0,2):
		if len(cpf) == 11:
			c = 10+j
			soma = 0
			for i in range(0,9+j):
				soma += int(cpf[i])*c
				c = c-1
			resto_onze = soma%11
			if resto_onze < 2:
				if int(cpf[9+j]) == 0:
					verificacao += 1
			else:
				if int(cpf[9+j]) == (11-resto_onze):
					verificacao += 1
	if verificacao == 2:
		print("O CPF É VÁLIDO!")
		break
	else:
		print("\nDIGITE SEU CPF SEM PONTOS E HÍFEN! APENAS OS NÚMEROS.")
		input("O CPF É INVÁLIDO! APERTE ENTER PARA DIGITAR OUTRO CPF.")
		os.system('cls' if os.name == 'nt' else 'clear')
input()