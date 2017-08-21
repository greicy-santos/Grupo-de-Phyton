#99:Crie um script com um dicionário que tenha o username de uma pessoa, o primeiro nome, e o ultimo a cada par de chaves, 
#em seguida faça um loop for para mostrar as chaves e os seus valores, use .items() explique
usuario = {
     'username':'greicy.santos',
     'first_name':'greicy',
     'last_name':'santos'
     }

for chave,valor in usuario.items():
	print(chave.title() +': ' +valor)

#Para fazer um laço no caso de dicionário temos que declarar uma variável para acessar a chave e para acessar o valor temos que declarar outra
#e para acessar os valores eu tenho que colocar o nome do dicionario .items() que é um método que retorna cada elemento do dicionário em pares
#que é a chave + valor

