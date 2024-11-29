soma = 0
lista = []
pares = []
for c in range(1, 7):
    num = int(input(f'Digite o número {c}: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
        soma += num
print(f'A soma dos números {pares} foi {soma}.')

    
