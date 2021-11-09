#5. Escrever um programa que leia três valores, e identifique o maior valor dentre eles.
pessoaA = []
pessoaB = []
pessoaC = []
pessoaA.append(str(input("1º NOME: ")))
pessoaA.append(int(input("1º IDADE: ")))
pessoaB.append(str(input("2º NOME: ")))
pessoaB.append(int(input("2º IDADE: ")))
pessoaC.append(str(input("3º NOME: ")))
pessoaC.append(int(input("3º IDADE: ")))

if pessoaA[1] >= pessoaB[1] and pessoaA[1] >= pessoaC[1]:
	maior = pessoaA[1]
elif pessoaB[1] >= pessoaA[1] and pessoaB[1] >= pessoaC[1]:
	maior = pessoaB[1]
elif pessoaC[1] >= pessoaA[1] and pessoaC[1] >= pessoaB[1]:
	maior = pessoaC[1]

if maior == pessoaA[1]:
	nomeMaior = pessoaA[0]
elif maior == pessoaB[1]:
	nomeMaior = pessoaC[0]
elif maior == pessoaC[1]:
	nomeMaior = pessoaC[0]

input("A PESSOA MAIS VELHA É {}, E TEM {} ANOS DE IDADE.".format(nomeMaior, maior))