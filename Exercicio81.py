idade = 12

if idade < 4:
  preco = 0
elif idade < 18:
	preco = 5
else:
	preco = 10

print('Seu custo de admissão são R$' +str(preco) + ',00 reais')

#Nesse caso foi armazenado o valor na variável de acordo com a condiçao, caso fosse menor que 4 armazenaria 0 na variavel preco, se fosse menor que 18 armazenaria 
#5 na variavel preco se nao fosse nenhuma das condiçoes atribuiria 10 na variavel preco. O valor impresso na tela é 5 pois o valor da variavel idade é igual a 
#12 fazendo com que entrasse no segundo if.