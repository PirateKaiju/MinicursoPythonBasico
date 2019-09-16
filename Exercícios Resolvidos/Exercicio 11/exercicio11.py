lista_charme = ["casa", "bonito", "lanterna" ]
lista_funk = ["casa", "lanterna", "elegante"]

for charme in lista_charme:
	if(not(charme in lista_funk)):
		print "Diferenca: " +  charme

for funk in lista_funk:
	if(not(funk in lista_charme)):
		print "Diferenca: " +  funk		
