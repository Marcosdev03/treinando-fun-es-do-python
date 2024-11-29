import statistics
soma = 0
lista = []
for c in range(1, 7):
    num = int(input(f'Digite o número {c}: '))
    lista.append(num)
    soma += num
    
media = soma / len(lista)

print(soma)
print(media)

