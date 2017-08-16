idade = 66

if idade < 4:
  preco = 0
elif idade < 18:
	preco = 5
elif idade < 65:
	preco = 10
else:
	preco = 5

print('Seu custo de admissão são R$' +str(preco) + ',00 reais')

#Nesse caso se a idade for menor que 4 o preço será 0, se a idade for menor que 18 ou maior que 65 anos será 5 reais, se for menor que 65 e maior que 18 será
#10 reais.