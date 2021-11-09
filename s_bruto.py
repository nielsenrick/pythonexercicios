print("---------- CALCULADORA SALÁRIO ----------")
v_hora = float(input("VALOR DA HORA: "))
qtd_hora = float(input("HORAS TRABALHADAS: "))
s_bruto = float(v_hora*qtd_hora)
fgts = s_bruto*0.11
i_sindical = s_bruto*0.03
if s_bruto <= 900:
	i_renda = 0
elif s_bruto > 900 and s_bruto < 1500:
	i_renda = 0.05*s_bruto
elif s_bruto > 1500 and s_bruto < 2500:
	i_renda = 0.10*s_bruto
else:
	i_renda = 0.20*s_bruto
s_liquido = s_bruto-i_renda-fgts-i_sindical
print("------------------------------------------")
print(f"SALÁRIO BRUTO:			", s_bruto)
print("IMPOSTO DE RENDA (IR):		-", i_renda)
print("FUNDO DE GARANTIA (FGTS):	-", fgts)
print("CONTRIBUIÇÃO SINDICAL: 		-", i_sindical)
print("SALÁRIO LÍQUIDO: 		", s_liquido)
input()