so_bons = ["Princess Mononoke", "Fargo", "Predator", "Terminator 2"] # Nossa lista, alguns titulos bons aqui...

print so_bons # ["Princess Mononoke", "Fargo", "Predator", "Terminator 2"]

#ADICAO

so_bons.append("Batman Forever") # Operacao de adicao. Devera adicionar "Batman Forever" como ultimo item da lista

print so_bons # ["Princess Mononoke", "Fargo", "Predator", "Terminator 2", "Batman Forever"] 

so_bons.append("Batman Vs. Superman")
#DELECAO

so_bons.remove("Batman Forever") # Com remove(), podemos remover um objeto da lista diretamente pela sua referencia

print so_bons # ["Princess Mononoke", "Fargo", "Predator", "Terminator 2", "Batman Vs. Superman"]

del(so_bons[4]) # Ja utilizando a Keyword del(), eh necessario passarmos o objeto completo, ou seja, o item da lista com seu indice para remover

print so_bons

#ORDENACAO

so_bons.sort() # Ordena a lista (nesse caso, por ordem alfabetica)

print so_bons

lista_num = [5, 2, 3, 7, 11]

print lista_num

lista_num.sort() # Ordena a lista de numeros

print "Ordenada: ", lista_num

#REVERSAO

print so_bons

so_bons.reverse() # Coloca a lista "ao contrario"

print so_bons

