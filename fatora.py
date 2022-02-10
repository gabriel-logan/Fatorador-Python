def fatorar():
	x = int(input("Digite x: "))
	A = []
	for y in range(2,x):
		while x%y==0:
			x /= y
			A.append(y)
	if sum(A)==0:
		A.append(x)
	print(A)
fatorar()