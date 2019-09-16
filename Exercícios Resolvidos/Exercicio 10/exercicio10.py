
n = int(raw_input("Entre com o valor: "))

for i in range(n - 1, 0, -1):
	n *= i
print n	

n = int(raw_input("Entre com o valor: "))

aux = 1
while(n > 0):
	aux *= n
	n -= 1
print aux

n = int(raw_input("Entre com o valor: "))

for i in range(1,n):
	n *= i
print n	
