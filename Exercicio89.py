coberturas_disponíveis = ['mussarela','bacon','calabreza','cebola']

coberturas_pedidas = ['bacon','brocolis','tomate']

for cobertura in coberturas_pedidas:
	if cobertura in coberturas_disponíveis:
		print('Adicionando ' +cobertura)
	else:
		print('Não temos ' +cobertura+ ' no momento')

print('\n')