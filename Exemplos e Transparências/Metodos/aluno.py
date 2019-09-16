class Aluno ():
	def __init__(self, nome): # Isto eh um metodo
		self.nome = nome
		self.escola = "Escola Python"
		
	def estuda(self): # Isto eh outro metodo. Observe a sintaxe, similar a funcoes
		print self.nome, " esta estudando no momento"	



aluno1 = Aluno("Beatrix Kiddo") 
aluno1.estuda() # Chamada de metodo, novamente, olhe a sintaxe
