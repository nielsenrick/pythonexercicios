import os
print("~~~~~~~ FILA DE BANCO ~~~~~~~")
ultimo = int(input("TAMANHO DA FILA: "))
pilha = list(range(1,ultimo+1))
while True:
	print("PILHA ATUAL: {}".format(pilha))
	print("INFORME O ÍTEM CORRESPONDENTE À AÇÃO QUE DESEJA REALIZAR:")
	print("[ A ] - ADICIONAR ÍTEM A PILHA")
	print("[ E ] - EXCLUIR ÍTEM DA PILHA")
	print("[ S ] - SAIR DO PROGRAMA")
	operacao = input("OPÇÃO: ")
	if len(pilha) > 0:
		if operacao.upper() == "A":
			pilha.append(len(pilha)+1)
		elif operacao.upper() == "E":
			excluir = pilha.pop(-1)
		elif operacao.upper() == "S":
			break
		else:
			print("VOCÊ DIGITOU UM COMANDO INVÁLIDO!")
	os.system('cls' if os.name == 'nt' else 'clear')
input()
