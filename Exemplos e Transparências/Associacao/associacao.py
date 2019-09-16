# Exemplos que consideram o tipo String
frase = "Words have no power to impress the mind without the exquisite horror of their reality." # Frase de Poe

if ("reality" in frase): # Operador in, ira checar se a palavra reality esta contida na string que eh o valor de "frase"
	print "Esta frase contem a palavra reality."
if ("green" in frase):
	print "Esta frase contem a palavra green"
if ("ghost" not in frase): # Operador not in, checa se ghost nao estara em "frase"
	print "Esta frase nao contem a palavra ghost"		

# Exemplo com apenas um caractere
palavra = "poe"

if("p" in palavra):
	print "Esta contida a letra p"	

