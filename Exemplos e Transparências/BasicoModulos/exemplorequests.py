import requests

r = requests.get("https://sistemas.riopomba.ifsudestemg.edu.br/dacc/index.php/professores")

print r # Se estiver tudo certo, retorna o codigo 200

print r.content
