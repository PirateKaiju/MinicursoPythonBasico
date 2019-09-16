valor = 10

def cinco():
	valor = 5

cinco()	
print valor	 # 10

def vinte():
	global valor
	valor = 20

vinte()	
print valor	 # 20
# Trabalhar diretamente com globais eh uma pratica ruim de programacao

lista_val = [16, 26, 36, 46]
def muda (lista):
	lista.append(56)
print lista_val
muda(lista_val)
print lista_val # Contem o valor 56
