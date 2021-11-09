#Faça um Programa que leia três números e mostre o maior e o menor deles deles.
for i in range(1,4):
	num = int(input("{}º NÚMERO: ".format(i)))
	if i == 1:
		maior = num
		menor = num
	else:
		if num > maior:
			maior = num
		elif num < menor:
			menor = num
print("MAIOR: {}".format(maior))
print("MENOR: {}".format(menor))
input()