class Veiculo(object):
	def __init__(self, nome, fabricante, ano, rodas, tipo):
		self.nome = nome
		self.fabricante = fabricante
		self.ano = ano
		self.rodas = rodas
		self.tipo = tipo
	def reabastecer(self):
		print "Em reabastecimento"
	
	def isPequenoPorteTerrestre(self):
		if(self.tipo == "terrestre" and self.rodas <= 4):
			print "Sou um veiculo de pequeno porte" 
	def antigo(self):
		if(self.ano < 1990):
			print "Sou antigo"
v1 = Veiculo("Enzo", "Ferrari", 2010, 4, "terrestre")
v2 = Veiculo("AC-130", "Lockheed Martin", 2000, 32, "aereo")
v3 = Veiculo("DB5", "Aston Martin", 1963, 4, "terrestre" )			
					
v1.isPequenoPorteTerrestre()
v2.reabastecer()
v3.antigo()
