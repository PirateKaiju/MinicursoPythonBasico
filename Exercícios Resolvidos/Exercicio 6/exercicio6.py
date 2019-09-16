valor_da_gasolina = float(raw_input("Digite o preco da gasolina: "))
valor_do_alcool = float(raw_input("Digite o preco do alcool: "))

if(valor_do_alcool > (0.7 * valor_da_gasolina)):
	print("A gasolina esta mais em conta.")
else:
	print("O alcool esta mais em conta")	
