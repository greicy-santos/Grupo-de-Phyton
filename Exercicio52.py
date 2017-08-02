contas_janeiro = ['água','luz','telefone']
contas_fevereiro = contas_janeiro[:]

contas_janeiro.append('internet')
contas_fevereiro.append('cartão de credito')

print("Contas do mês de Janeiro:" +str(contas_janeiro))
print("Contas do mês de Fevereiro:" +str(contas_fevereiro))

#As listas exibem valores diferentes, porque quando eu fiz a cópia da lista ela não havia adicionado o elemento novo, quando eu inseri a lista nova já havia
#sido copiada, fazendo com que tudo que eu adicionasse de diferente nas listas não refletisse na outra, pois o vinculo que elas tinham só ocorreu na hora da
#cópia de uma lista para outra.

