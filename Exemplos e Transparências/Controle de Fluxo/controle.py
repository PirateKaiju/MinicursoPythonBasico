print "RPG Batalha do Terminal - Versao 0.0.1 - Fase de Teste"

qtd_ataque = 10
qtd_hp = 100

print "Voce esta andando pela mansao da terrivel Cottonmouth. Um espadachim inimigo avista voce."
print "Ele vem em sua direcao."
if(qtd_ataque > 5): # Se ataque for maior que 5, executa o bloco de codigo no "interior" do if
	print("Voce desfere um golpe letal no inimigo!")
elif(qtd_hp > 20): # Senao, se hp maior que 20, executa o bloco de codigo no interior do "else if"
	print("O inimigo desfere um golpe em voce, porem voce so leva um corte.")
	qtd_hp -= 20
else: # Se tudo "falhar", ele ira para este bloco de codigo
	print("O inimgo desfere um golpe. Voce morreu!")	
	
		
	
