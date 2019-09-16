x = 0 #Inicializamos uma variavel que sera nossa contadora
while(x < 5):#Inicio do loop While, com nosso criterio de parada sendo "execute ENQUANTO x < 5"
	print x
	x+=1 #Incrementamos nossa contadora #NAO PODEMOS ESQUECER DISSO! 

#Um exemplo mais pratico
#Somatorio
#Funcao: 2X + 4
somatorio = 0
limite_inf = 0
limite_sup = 5

while(limite_inf <= limite_sup):
	somatorio += 2*limite_inf + 4
	limite_inf += 1
print somatorio	
#Resultado deve ser 54


			
