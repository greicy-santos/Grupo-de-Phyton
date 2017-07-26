frutas = ['maçã','banana','kiwi','manga','morango','abacate','caqui']

print('Frutas que eu como mas não gosto tanto: ' +str(frutas[1:4])+'\n')

#Nesse caso são impressos somente 3 elementos pois ele não considera o elemento segundo elemento do colchete no caso o 4, ou seja,
#ele começa da posição 1 que é banana e vai até a posição 3 que é manga. Se eu quisesse imprimir o quarto elemento tbm eu teria 
#que declarar de 1:5