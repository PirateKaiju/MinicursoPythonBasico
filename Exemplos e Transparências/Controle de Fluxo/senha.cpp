#include <iostream>
#include <string>

using namespace std;

int main(){
	
	cout<<"Senha: ";
	string senha = "";
	cin>>senha;
	
	if(senha == "senha1234"){
		cout<<"Bem-Vindo!"<<endl;
	}else{
		cout<<"Senha incorreta. Este sistema ira se autodestruir."<<endl;
		}
	return 0;	
	}
	
	
	
