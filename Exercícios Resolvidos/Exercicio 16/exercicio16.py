def calculadora(valor1, valor2):
	print "Soma: " + str((valor1 + valor2))
	print "Subtracao: " + str((valor1 - valor2))
	if(valor2 != 0):
		print "Divisao: " + str(valor1 / valor2)
	else:
		print "Erro, divisao por 0"	
	print "Multiplicacao: " + str(valor1 * valor2)
	

calculadora(10, 5)

calculadora(20, 0)

calculadora(12, 7)
