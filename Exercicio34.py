frutas = ['morango','maçã','manga','laranja','caqui']

for fruta in frutas:
	print('A salada de fruta tem ' +str(fruta.title()) +'!')

print('Mas minha fruta favorita é ' +str(fruta.title()))

#O primeiro print possui todos os elementos da lista, pois fazem parte da identação do laço, o segundo print imprime somente o ultimo item da lista, pois o phyton 
#entende que o segundo print não faz parte do laço, pois está fora da identação e como o ultimo elemento armazenado na variável fruta é o ultimo elemento da lista
#ele imprime da variável