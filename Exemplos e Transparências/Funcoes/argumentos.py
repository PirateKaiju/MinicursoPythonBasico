
def cumprimentar_requerido (nome, idade): # Argumentos requeridos
	print nome, " meu grande amigo!"

def cumprimentar_padrao(nome = "Joao Amorim", idade = 60): # Argumentos padrao
	#Estes valores serao padrao em qualquer chamada
	print nome, " meu grande amigo!"

def cumprimentar_tamvar(*nome): # Argumentos de tamanho de variavel
	#Nome sera uma tupla, tao grande quanto se queira
	print nome, " meu(s) grande(s) amigo(s)!"	

def cumprimentar_keyword (nome, idade): # Argumentos palavra chave
	#Sintaticamente, a funcao eh declarada da mesma forma que com args. requeridos
	print nome, " meu grande amigo!"
	
	
cumprimentar_requerido("Irineu", 36) # Chamada
cumprimentar_padrao("Schwarzenegger", 22) # Chamada 
cumprimentar_padrao() # Utiliza dos valores definidos por padrao
cumprimentar_tamvar("Fulano", "Beltrano") # Chamada com mais de um valor associado ao parametro
cumprimentar_keyword(idade = 40, nome = "Mikkelsen") # Por palavras chave, os argumentos podem estar em qualquer ordem

