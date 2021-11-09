n1= float(input("DIGITE UM NÚMERO: "))
n2= float(input("DIGITE OUTRO NÚMERO: "))
n3= float(input("DIGITE MAIS UM NÚMERO: "))
n4= float(input("DIGITE OUTRO NÚMERO: "))
media= (n1+n2+n3+n4)/4
moda= "{}"
mediana= ""
if n1==n2 or n1==n3 or n1==n4:
	moda=n1
if n2==n3 or n2==n4:
	moda=n2
if n3==n4:
	moda=n3
print("media: ", media)
print("moda: ", moda)
input()
