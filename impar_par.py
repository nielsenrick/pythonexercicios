num_par = []
num_impar = []
for i in range(10):
	num = int(input("NÚMERO: "))
	if num%2 == 0:
		num_par.append(num)
	else:
		num_impar.append(num)
print("QUANTIDADE DE PARES: ", len(num_par))
print("PARES: ", num_par)
print("QUANTIDADE DE ÍMPARES: ", len(num_impar))
print("ÍMPARES: ", num_impar)
input()
