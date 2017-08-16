idade = 66

if idade < 4:
  preco = 0
elif idade < 18:
	preco = 5
elif idade < 65:
	preco = 10
elif idade >=65:
	preco = 5

print('Seu custo de admissão são R$' +str(preco) + ',00 reais')