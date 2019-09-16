class Personagem():
	def __init__(self, nome, classe, hp): # Construtor
		self.nome = nome
		self.classe = classe
		self.hp = int(hp)
	def acao (self, narracao):
		print self.nome, " realizou: ", narracao	

p1 = Personagem("Bill", "Espadachim", 100) # O construtor eh chamado neste momento!
p2 = Personagem("Beholder", "Monstro", 200)

p1.acao("Retira espada da bainha")
