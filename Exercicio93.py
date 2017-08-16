personagem = {'Nome':'pikachu','Habilidade':'choque do trovao'}

print('Before' +str(personagem))

personagem['Pontuaçao'] = 100
personagem['Cor'] = 'amarelo'

print('\nAfter' +str(personagem))

#Nesse caso eu adicionei 2 chaves ao dicionário imprimi o que estava antes e depois adicionei mais 2 chaves no dicionário, quando eu adiciono novas chaves no
#dicionário eu nao perco as chaves que eu já havia criado, ele simplesmente armazena as outras chaves que eu criei sem perder os valores armazenados anteriormente