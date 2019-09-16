class Pessoa(): # Classe
	def __init__(self, nome, idade, hobby): # Chamada do metodo
		# Abaixo, teremos a definicao dos atributos
		self.nome = nome # Atributo nome
		self.idade = int(idade) # Atributo idade
		self.hobby = hobby # Atributo hobby
		#Talvez esteja curioso com o porque deste "self", nao?
		
		#Todos atributos, representando alguma caracteristica de pessoa
	
	def apresenta(self): # Nao se preocupe com isto ainda
		print "Sou ", self.nome, ", tenho ", self.idade	

tom = Pessoa("Tom Cruise", 45, "Escalar")

tom.apresenta()
