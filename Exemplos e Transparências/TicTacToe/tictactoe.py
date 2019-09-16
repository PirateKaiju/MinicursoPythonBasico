tabuleiro = []  # Inicializa como uma lista vazia "[]"
for cont in range (3): # Desejamos construir um tabuleiro "padrao" para o jogo da velha 
	tabuleiro.append([0,0,0]) # A cada iteracao, adiciona uma lista preenchida por "0"
print tabuleiro
#Com apenas 3 linhas de codigo, fomos capazes de criar o tabuleiro!

def vitoria(tabuleiro_a_analisar):
	for cont in range(3):
		if sum(tabuleiro_a_analisar[cont]) == 3 or sum(tabuleiro_a_analisar[cont]) == -3:
			return True # Alguem venceu horizontalmente
	somavertical = 0		
	for contx in range(3):
		for conty in range (3):
			somavertical += tabuleiro_a_analisar[conty][contx]
		if(somavertical == 3 or somavertical == -3):
			return True # Alguem venceu verticalmente
		somavertical = 0
	#Diagonais
	somadiagonal = 0	
	for cont in range(3):
		somadiagonal += tabuleiro_a_analisar[cont][cont]
	if(somadiagonal == 3 or somadiagonal == -3):
		return True	
	somadiagonal = 0	
	for cont in range(3):
		somadiagonal += tabuleiro_a_analisar[cont][2 - cont]
	if(somadiagonal == 3 or somadiagonal == -3):
		return True	
	return False					

def imprimetabuleiro(tabuleiro_a_imprimir):
	for linha in range (3):
		print tabuleiro[linha]
			
turno = 0
while (not(vitoria(tabuleiro)) and turno < 9):
	imprimetabuleiro(tabuleiro)
	if(turno%2 == 0):
		x = int(raw_input("Jogador 1, escolha a coordenada x: "))
		y = int(raw_input("Jogador 1, escolha a coordenada y: "))
		
		if(tabuleiro[x][y] == 0):
			tabuleiro[x][y] = 1
			turno += 1
		else:
			turno += 1
	else:
		x = int(raw_input("Jogador 2, escolha a coordenada x: "))
		y = int(raw_input("Jogador 2, escolha a coordenada y: "))
		
		if(tabuleiro[x][y] == 0):
			tabuleiro[x][y] = -1
			turno += 1
		else:
			turno += 1
imprimetabuleiro(tabuleiro)			
print "Fim de jogo"					
	

