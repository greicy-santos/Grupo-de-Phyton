frutas = ['laranja', 'maçã', 'caqui']

print("Before")
print(frutas)
frutas.insert(0, 'uva')
print("=============================")
print("After")
print(frutas)
print("=============================")
print("Excluindo um item da lista")
print("=============================")
del frutas[2]
print("Lista Atualizada")
print(frutas)