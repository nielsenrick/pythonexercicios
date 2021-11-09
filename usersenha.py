#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
#ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
user = 'a'
senha = 'a'
while user == senha:
	user = str(input("USUÁRIO: "))
	senha = str(input("SENHA: "))
	if user == senha:
		print("SENHA INVÁLIDA! DIGITE NOVAMENTE:")
		print()
	else:
		print("OK! SENHA VÁLIDA. OBRIGADO!")
input()