ladoA = str(input("LADO A: "))
ladoB = str(input("LADO B: "))
ladoC = str(input("LADO C: "))
if ladoA < ladoB+ladoC and ladoB < ladoA+ladoC and ladoC < ladoA+ladoB:
	print("É UM TRIANGULO!")
	if ladoA == ladoB == ladoC:
		print("EQUILÁTERO")
	elif ladoA == ladoB or ladoA==ladoC or ladoC==ladoB:
		print("ISÓSCELES")
	elif ladoA != ladoB != ladoC:
		print("ESCALENO")
else:
	print("NÃO É UM TRIANGULO!")
input()