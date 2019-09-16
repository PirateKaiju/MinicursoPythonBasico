
def isJohn (nomes):
	for registro in nomes:
		if(registro['Nome'] == 'John'):
			print(registro)
			
def add_j(nomes):
	novo_nome = raw_input("Nome: ")
	novo_sob = raw_input("Sobrenome: ")
	novo_prof = raw_input("Profissao: ")
	novo = {'Nome' : novo_nome, 'Sobrenome' : novo_sob, 'Profissao' : novo_prof}
	nomes.append(novo)
	
	
def remove_j(nomes, remover):	
	del(nomes[remover])		
		
		

vet_johns = [{'Nome' : 'John',  'Sobrenome' : 'Hammond', 'Profissao' : 'Empreendedor'}, 
{'Nome' : 'John',  'Sobrenome' : 'Rambo', 'Profissao' : 'Militar'}, 
{'Nome' : 'John',  'Sobrenome' : 'Wick', 'Profissao' : 'Veterinario'},  
{'Nome' : 'John',  'Sobrenome' : 'McClane', 'Profissao' : 'Detetive'},  
{'Nome' : 'John',  'Sobrenome' : 'Snow', 'Profissao' : 'Patinador'}
]


isJohn(vet_johns)
add_j(vet_johns)
print vet_johns
remove_j(vet_johns, 3)
print vet_johns
