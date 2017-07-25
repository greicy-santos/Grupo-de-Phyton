carros = ['fox','celta','gol','honda civic']

vendedor = 'marcos'

cliente = 'greicy'

print('Vendedor: Seja bem vinda senhora ' + cliente.title() + "! Meu nome é " +vendedor.title() + ".")
print('\nCliente:  Oi ' + vendedor.title() + ", gostaria de saber quantos carros tem na concessionária?")
print('\nVendedor: Então senhora ' + cliente.title() + " nós temos " + str(len(carros)) + " carros na concessionária!")
print('\nCliente: Quais são os carros?')
print('\nVendedor: Os carros são: ' +str(carros[0].title()) + ", " +str(carros[1].title()) + ", " +str(carros[2].title()) + " e " +str(carros[3].title()))
print('\nCliente: Eu gostei do ' +str(carros[3].title()) +"! Qual o preço?")
print('\nVendedor: Esse está R$ 40.000,00 reais.')
print('\nCliente: Nossa como está barato!\n')
