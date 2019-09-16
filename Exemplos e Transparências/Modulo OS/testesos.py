import os

def detalhesRede():
	if(os.name == "posix"): #os.name, retorna detalhes quanto ao S.O. usado
		os.system("ifconfig")#os.system, executa um comando
	else:
		os.system("ipconfig")	

detalhesRede()#Voce consegue definir qual a funcionalidade deste programa?
