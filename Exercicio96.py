nave = {'posicao_y':0,'posicao_x':50,'velocidade':'baixa'}
print('Posição X = ' +str(nave['posicao_x']))

if nave['velocidade'] == 'baixa':
	add = 20
elif nave['velocidade'] == 'media':
	add = 10
else:
	add = 5

nave['posicao_x'] = nave['posicao_x'] + add

print('Nova Posição X = ' +str(nave['posicao_x']))

#Nessa caso foi atribuido um valor para a chave posicao_x, depois foi feito uma condiçao baseada na chave de velocidade e acrescentado um valor a uma variavel
#depois foi somado o valor da nova variavel na posicao_x, modificando assim, o valor original dessa chave