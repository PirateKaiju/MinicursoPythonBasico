def magia_avancada(palavra_magica): # "palavra_magica" aqui eh um PARAMETRO da funcao
	print "Hocus " + palavra_magica # variavel esta "disponivel pelo nome do parametro" agora

palavra = "Abacadabra" # Criamos a palavra em outro escopo, nesse caso, Global

magia_avancada(palavra)	#passamos como ARGUMENTO "palavra" a funcao magia avancada

