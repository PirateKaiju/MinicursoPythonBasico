def exterminador(municao):
	while(municao > 0):
		print "Disparando..."
		municao -= 1
	return "Eu vou voltar..." 
	
""" Keyword return, indica que algo sera "retornado" para o fluxo que
originou a chamada desta funcao"""

fala_personagem = exterminador(10)

print "Fala: ", fala_personagem

