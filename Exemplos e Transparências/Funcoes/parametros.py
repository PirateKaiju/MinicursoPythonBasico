palavra_magica = "Alakazam" # Escopo Global

def magia ():
	palavra_magica = "Abacadabra" # Mesmo nome, porem escopo diferente
	print palavra_magica

print "\nDo escopo da Funcao"	
magia()	

#Resultados diferentes, escopos diferentes

print "\nDo Global:"
print palavra_magica


def outra_magia():
	print palavra_magica 

# Eh aqui que a magica acontece!
print "\nE aqui, o Python fazendo esforco: "	
outra_magia()

palavra_magica = "Abracapocus"

outra_magia()

#Lembre-se: Python faz o "melhor esforco" para tudo dar certo!

