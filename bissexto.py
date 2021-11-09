#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe
#se este ano é ou não bissexto.

num = int(input("NÚMERO: "))
res = str()
if num%4 == 0:
	res = "BISSEXTO"
elif num%100 == 0:
	res = "NÃO É BISSEXTO"
elif num%400 == 0:
	res = "BISSEXTO"
else:
	res = "NÃO É BISSEXTO"
print(res)
input()