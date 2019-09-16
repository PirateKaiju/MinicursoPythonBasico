dados_pessoa = {"Nome" : "Hannibal", "Sobrenome" :  "Lecter", "Profissao" : "Psicologo", "Detalhes" : "Curte uns rango diferenciado..."} 
#Exemplo de dicionario. Note a estrutura organizada em chaves
print dados_pessoa["Nome"]#Imprime o valor cuja chave eh "Nome"
print dados_pessoa

mapeamento_id = {0 : "Alice", 1 : "Bob", 2 : "Carl"}#Mapeamento de ids, uma possivel aplicacao para dicionarios

#Algumas funcionalidades especificas de dicionarios

print mapeamento_id.keys()#Somente as chaves
print mapeamento_id.values()#Somente os valores

mapeamento_id2 = {2 : "Charlinho", 42 : "Irineu"}

mapeamento_id.update(mapeamento_id2) # Update atualiza/complementa valores entre dois dicionarios

print mapeamento_id

mapeamento_id.clear()#Remove todos os pares presentes

