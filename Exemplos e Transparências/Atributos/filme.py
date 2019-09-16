class Pessoa():
	def __init__(self, nome):
		self.nome = nome

class Filme():
	
	def __init__(self):
		self.protagonista = Pessoa("Leonardo Dicaprio") # Chamando a outra classe
		self.protagonista2 = Pessoa("Tom Hanks")

filme_top = filme()

print filme_top.protagonista.nome # Observe como fazemos o acesso aqui
	 
		
