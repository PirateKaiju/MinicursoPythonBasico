lista_magias = ["Abacadabra", "Babacadabra", "Hocus Pocus","Tome Cevadis", "Apalavris Sensintidus"]

def super_magia(magias):
	for magia in magias:
		print "Atacando com: ", magia

super_magia(lista_magias)

print "\n\n\n"

# Um exemplo mais pratico
def busca_binaria(lista_valores, inicio, fim, valor):
	meio = int((inicio + fim)/2)
	print meio
	if(valor == lista_valores[meio]):
		print "Encontrado", lista_valores[meio]
		return
	elif(meio == fim or meio == inicio):
		print "Fim de execucao, Valor Inexistente no conjunto"
		return	
	elif(valor < lista_valores[meio]):
		busca_binaria(lista_valores, inicio, meio-1, valor)
		return
	elif(valor > lista_valores[meio]):
		busca_binaria(lista_valores, meio+1, fim, valor)
		return
	else:
		print "Valor Inexistente no conjunto"
		return

lista_a_testar = [1,2,3,5,8,13,21]

busca_binaria(lista_a_testar, 0, len(lista_a_testar), 13)			
				
