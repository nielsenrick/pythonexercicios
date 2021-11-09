import os
print("~~~~~~~ FILA DE BANCO ~~~~~~~")
ultimo = int(input("TAMANHO DA FILA: "))
fila = list(range(1,ultimo+1))
while True:
	print("FILA ATUAL: {}".format(fila))
	print("INFORME O ÍTEM CORRESPONDENTE À AÇÃO QUE DESEJA REALIZAR:")
	print("[ A ] - ADICIONAR PESSOA A FILA")
	print("[ E ] - EXCLUIR PESSOA DA FILA")
	print("[ S ] - SAIR DO PROGRAMA")
	operacao = input("OPÇÃO: ")
	if len(fila) > 0:
		if operacao.upper() == "A":
			fila.append(fila[-1]+1)
		elif operacao.upper() == "E":
			del fila[0]
		elif operacao.upper() == "S":
			break
		else:
			print("VOCÊ DIGITOU UM COMANDO INVÁLIDO!")
	os.system('cls' if os.name == 'nt' else 'clear')
input()
