#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
temperatura_mensal = []
meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
acima_media = []
t = temperatura_mensal
for i in range(12):
	temperatura_mensal.append(float(input(f"TEMPERATURA DO MÊS {meses[i]} (EM C°): ")))
media_anual = (t[0]+t[1]+t[2]+t[3]+t[4]+t[5]+t[6]+t[7]+t[8]+t[9]+t[10])/12
print(f"MEDIA ANUAL: {media_anual}\n")
print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:\n")
for i in range(12):
	if t[i] > media_anual:
		print(f"{meses[i]}: {t[i]}")
input()