valores = range(5)
print valores # [0, 1, 2, 3, 4]

#range pode ser definida, em sua forma completa, da seguinte forma: range(inicio, fim, passo), onde:
#Inicio: De onde o intervalo de geracao devera partir. O intervalo sera fechado para este valor, ou seja, o mesmo sera incluido no conjunto
#Fim: Onde o intervalo devera terminar. O intervalo sera aberto para este valor, logo, o mesmo nao sera incluido no conjunto
#Passo: De quanto em quanto o valor ira progredir (aumentar ou decrementar)
#Em outras formas desta funcao, sao aceitos 2 parametros ou apenas 1

print "Exemplos"
print range (1, 10, 2) #De 1 a 9, "contando" de 2 em 2
print range (0, 5, 1) #Equivalente a range(5)
print range (15, 0, -5) #Decremental

#Forma de 2 parametros: inicio e fim
print range (1, 20)

#Forma de 1 parametro: apenas o fim (considera o inicio como 0)
print range(10)


