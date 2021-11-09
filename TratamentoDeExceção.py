while True: #repete a pergunta ao usuário insistentemente.
	try:
		x = int(input("DIGITE UM NÚMERO INTEIRO: "))
		print("OK!")
		break #finaliza o programa.
	except ValueError: #se o usuário digitar algo que não seja um número inteiro, será impressa a mensagem abaixo.
		print("VOCÊ NÃO DIGITOU UM NÚMERO VÁLIDO! TENTE NOVAMENTE.\n")
input()