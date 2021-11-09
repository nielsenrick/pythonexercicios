
num1 = [1,2,3,4,5,6]
num2 = [2,4,5,8,10,12]
num3 = []
for i in range(0,6):
	if num1[i] != num2[i]:
		num3.append(num1[i])
	if num2[i] != num1[i]:
		num3.append(num2[i])
print(num1)
print(num2)
print(num3)
input()
