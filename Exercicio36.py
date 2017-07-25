lista_compras = ['arroz','feijão','açúcar','alface','tomate']

for lista in lista_compras:
	print('Item da lista: ' +str(lista.title()))
	print('Não posso esquecer de comprar ' + str(lista)+'\n')
	
	print('Compra efetuada com sucesso!')
#print('Compra efetuada com sucesso!')

#Esse erro ocorre, pois foi feito uma identação desnecessária na terceira mensagem, para consertar eu teria que colocar o print fora da identação do laço, 
#assim como eu coloquei na linha comentada.