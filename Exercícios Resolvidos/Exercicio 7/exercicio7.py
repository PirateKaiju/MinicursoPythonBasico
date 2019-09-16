temperatura = float(raw_input("Entre com a temperatura: "))
if(temperatura < 0):
	print "Sub-Zero!"
elif(temperatura >= 0 and temperatura < 15):	
	print "Trolla-Solteiros"
elif(temperatura >= 15 and temperatura <= 35):
	print "Sorvete Tropical"
else:
	print "Ta pegando fogo bicho!"		
	
