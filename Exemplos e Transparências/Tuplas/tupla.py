tupla_vazia = () # Inicializa uma tupla vazia.

tupla_numerica = (1, 2) # Tupla numerica de 2 elementos

tupla_numerica = (1, 2, 3, 4) # Tupla numerica com 4 elementos

print tupla_numerica

print len(tupla_numerica) # Lembra-se de len()? Aqui, nos dara o tamanho da tupla

tupla_aeds = ("AEDs 1", "AEDs 2", "AEDs 3") # Tupla de strings

print tupla_aeds[0] # Acessando e imprimindo um elemento da tupla

#Tuplas tambem podem ser definidas sem os "()". Na realidade, python
#ira avaliar qualquer elemento separado por "," e sem outro delimitador
#como uma Tupla.

tupla_sem_parenteses = 1,2,3

print type(tupla_sem_parenteses) # type() nos permite obter o tipo associado a uma variavel, da forma como python o "enxerga"

#Tuplas sao bastante usadas em python para a troca de valores. 
#Esta operacao, alem de "economica", eh bastante simples de se compreender 

a = 0
b = 1

print a, b

a, b = b, a # Troca por tupla ou "Tuple Swapping"

print a, b

