
print "Este aqui eh o escopo global"

def testador_primo(possivel_primo):
	m_possivel_primo = int((possivel_primo)/2) # Uma otimizacao: Testa apenas metade do conjunto
	for cont in range(2,m_possivel_primo,1): # Inicia em 2
		if(possivel_primo % cont == 0): # Se o resto da divisao eh 0, significa que o numero dividiu, logo, nao eh primo
			return False
	return True

def buscaprimo(valor):
	print """Esta funcao testa se valores são primos
(divisivel somente por 1 e ele mesmo)."""
	if(limite < 2):# Solucao elegante
		return
	res = testador_primo(int(valor))
	if(res):
		print "EH PRIMO"
	else:
		print "NAO EH PRIMO"

#Multiplas chamadas
buscaprimo(7)
buscaprimo(2)
buscaprimo(6)	
buscaprimo(15557)		
				
