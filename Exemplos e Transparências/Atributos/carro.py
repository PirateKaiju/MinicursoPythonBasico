class Carro():
	
	# Este __init__ sera chamado ao criarmos o objeto. Detalhes a frente.
	def __init__(self, marca, modelo, motor, proprietario):
		self.marca = marca
		self.modelo = modelo
		self.motor = motor
		self.proprietario = proprietario

# Criando o objeto a partir da classe "Carro"
fuscao = Carro("Volkswagen", "80 - Off-Road", "V8", "Popretariu")

print fuscao.marca # Acesso ao atributo "marca". Imprime "Volkswagen"
print fuscao.modelo
print fuscao.motor
print fuscao.proprietario		
		
		
	
	
