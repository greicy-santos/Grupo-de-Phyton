85:Faça como o 84 porem adicione elifs depois do if , o código vai parar na primeira condição caso ela passe, explique por que isso acontece .

pizza = ['mussarela','calabreza','bacon']

if 'mussarela' in pizza:
	print('Mussarela adicionada')
elif  'cebola' in pizza:
	print('\nCebola Adicionada')
elif 'calabreza' in pizza:
	print('Calabreza Adicionada')

#Ele só entra entra em uma única condiçao, pois se encontrar uma condiçao válida ele nem testa as demais condiçoes