class Aluno():
	quantidade_alunos = 0 #Variavel estatica, inicializada com 0
	def __init__(self, nome):
		self.nome = nome # Um atributo "comum"
		Aluno.quantidade_alunos += 1 #Observe que o acesso eh diferenciado

aluno1 = Aluno("Ada")
print "De aluno1: ", aluno1.quantidade_alunos #Altera para todos os membros da classe
aluno2 = Aluno("Alan")		
print "De aluno2: ", aluno2.quantidade_alunos

print "De aluno1: ", aluno1.quantidade_alunos
