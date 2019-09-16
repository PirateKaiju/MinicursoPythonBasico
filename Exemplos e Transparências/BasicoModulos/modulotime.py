import time # Importamos o modulo time (padrao na maioria das instalacoes)
#Vamos utiliza-lo para mensurar o tempo de execucao 
atual = time.time() # Tempo atual

x = 0

'''Fazemos algum processamento aqui,
por exemplo, somar todo mundo de 0 a 999'''

for i in range(1000):
	x += i

print x

print time.time() - atual # Diferenca que representa o tempo decorrido


