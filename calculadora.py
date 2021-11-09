#Escreva um programa que leia dois números e que pergunte qual
#operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

n1= float(input("DIGITE O PRIMEIRO NÚMERO: "))
n2= float(input("DIGITE O SEGUNDO NÚMERO: "))
resultado= float(0)
print("QUAL OPERAÇÃO MATEMÁTICA DESEJA EFETUAR?")
print("A) ADIÇÃO")
print("B) SUBTRAÇÃO")
print("C) MULTIPLICAÇÃO")
print("D) DIVISÃO")
operação= str(input("QUAL OPERAÇÃO MATEMÁTICA DESEJA EFETUAR? "))
if operação == "A" or operação == "a":
	resultado= n1+n2
elif operação == "B" or operação == "b":
	resultado= n1-n2
elif operação == "C" or operação == "c":
	resultado= n1*n2
elif operação == "D" or operação == "d":
	resultado= n1/n2
else:
	input("Comando Invalido!")
print("RESULTADO: ", resultado)
input()