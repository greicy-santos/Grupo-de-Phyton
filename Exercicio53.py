contas_janeiro = ['água','luz','telefone']
contas_fevereiro = contas_janeiro[:]

contas_janeiro.append('internet')
contas_fevereiro.append('cartão de credito')

contas_fevereiro = contas_janeiro

print("Contas do mês de Janeiro:" +str(contas_janeiro))
print("Contas do mês de Fevereiro:" +str(contas_fevereiro))

#Nesse caso as listas ficam iguais, porque quando eu atribuo uma lista a outra o python entende que foi feita uma conexão entre elas, entao tudo o que eu alterar
#em uma será alterado na outra também

