minhas_frutas = ['caqui','manga','morango']
frutas_amigos = minhas_frutas[:]

minhas_frutas.append('laranja')
frutas_amigos.append('melao')

print('Minhas Frutas:')
for minha_fruta in minhas_frutas:
  print(minha_fruta)

print('\nFrutas dos meus Amigos')	
for fruta_amigos in frutas_amigos:
  print(fruta_amigos)
