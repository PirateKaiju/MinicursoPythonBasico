lista_poderes = ["Hadouken", "Kamehameha", "Serious_Punch", "Astucia", "Dinheiro", "Force_Lightning", "Orar_para_Existencia_X" ]

lista_poderes[5] = "Mind_Trick"

print lista_poderes

lista_so_vogal = []
for item in lista_poderes:
	if(item[0] in "aeiouAEIOU"):
		lista_so_vogal.append(item)

print lista_so_vogal

i = 0
while(i < len(lista_poderes)):
	if(i >= 3):
		lista_poderes[i] = "Sem Poder"
	i+=1
print lista_poderes
