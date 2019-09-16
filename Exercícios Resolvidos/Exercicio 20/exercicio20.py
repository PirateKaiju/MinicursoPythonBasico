class Animal(object):
	def __init__(self, nome, idade, eh_amigavel):
		self.nome = nome
		self.idade = idade
		self.eh_amigavel = eh_amigavel
	def fugir(self):
		print "Estou correndo para longe"
	def atacar(self):
		print "Insira o som de um ataque aqui..."		

class Mamifero(Animal):
	def cair_pelo(self):
		print "Meu pelo esta caindo"

class Ave(Animal):
	def voar(self):
		if(self.nome != "pinguim" and self.nome != "galinha"):
			print "Volare, oh, oh..."		

m1 = Mamifero("cachorro", 5, True)
a1 = Ave("beija-flor", 1, True)
m1.fugir()
a1.voar()
