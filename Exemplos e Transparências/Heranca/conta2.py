class Conta(): # Classe Conta: operacoes bancarias genericas...
	def __init__(self, nome, dinheiro):
		self.nome = nome
		self.dinheiro = dinheiro
	def deposito(self, valor):
		self.dinheiro += valor
	def saque(self, valor):
		self.dinheiro -= valor

class ContaCorrente(Conta): # ContaCorrente "herda" de Conta. Heranca possui esta sintaxe.
	def __init__(self, nome, dinheiro, nome_conjunto):
		Conta.__init__(self, nome, dinheiro) # "Super" interessante, nao eh?
		# A linha acima invoca o construtor de "Conta", sobre este objeto (vide self)
		self.nome_conjunto = nome_conjunto
	def responsaveis(self):
		print self.nome_conjunto, " - ", self.nome
	def saque(self, valor):
		print "Saque de Conta Corrente"
		print "Aviso: eh necessario aprovacao de ambos os correntistas" #Este eh diferente
		self.dinheiro -= valor				
			
#Neste exemplo, "Conta" eh a classe pai e "ContaCorrente" eh a classe filha

c1 = ContaCorrente("Milionario", 1000, "Ze Rico")

c1.responsaveis() # Metodo de ContaCorrente

print c1.dinheiro # Este atributo eh da classe Conta
c1.deposito(333) # Este metodo tambem eh da classe Conta
print c1.dinheiro 

c1.saque(100)
print c1.dinheiro # E ai, o que sera que vai acontecer? Spoiler: Isto funciona, e eh bem util...

