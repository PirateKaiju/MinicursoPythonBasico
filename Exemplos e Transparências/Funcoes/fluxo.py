print "Isto sera a primeira linha a ser interpretada"

def dentro():
	print "Estou dentro da funcao agora"

print "Este aqui eh o escopo global do programa"
print "Eh bem legal aqui, nao acha?"

def nuncasera(): # Nao ha uma especificacao para "lugar" da funcao
	print "Esta frase nunca sera interpretada neste codigo, nao ha chamada de funcao"

#Apesar disto, muitos programadores preferem coloca-las no inicio
#Python somente interpretara uma chamada a uma funcao ja declarada anteriormente

dentro() # Chamada	
ultima() # Ira gerar um erro em tempo de execucao

def ultima ():
	print "No codigo, estou bem no fim"
