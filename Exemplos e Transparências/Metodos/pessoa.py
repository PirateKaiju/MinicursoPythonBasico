class Pessoa():
	def __init__(self, nome, idade): # Observe que eh o primeiro parametro
		self.nome = nome # self representa a declaracao de nome para a instancia em questao no momento
 		self.idade = idade 
	def apresenta (self):
		print "Eu sou", self.nome # Acesso ao atributo nome da instancia que chamar este metodo

p1 = Pessoa("Von Neumann", 33)

p1.apresenta()# Nao especificamos o self ao chamar o metodo (ja sabiamos disso...)		
