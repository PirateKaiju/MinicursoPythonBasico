nome = raw_input("Nome: ")
helper = True
if("a" in nome):
	print("A de Astronomy")
	helper = False
	
if("e" in nome):
	print("E de Enter Sandman")
	helper = False

if("i" in nome):
	print("I Disappear")
	helper = False	
	
if("o" in nome):
	print("O de One")
	helper = False	
	
if("u" in nome):
	print("U de Unforgiven")
	helper = False	

if(helper):
	print "Certamente prefere Megadeth"
