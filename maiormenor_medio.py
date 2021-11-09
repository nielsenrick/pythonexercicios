lista = []
for i in range(0,3):
	lista.append(int(input("{}º NÚMERO: ".format(i+1))))
	if i == 0:
		maior = lista[i]
		menor = lista[i]
	else:
		if lista[i] > maior:
			maior = lista[i]
		elif lista[i] < menor:
			menor = lista[i]
for i in range(0,3):
	if lista[i] != maior and lista[i] != menor:
		medio = lista[i]
print("MAIOR: ", maior)
print("MÉDIO: ", medio)
print("MENOR: ", menor)
input()