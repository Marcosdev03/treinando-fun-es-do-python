soma = 0 
lista = []

for c in range(1, 6):
    num = int(input(f'Digite o número {c}: '))
    lista.append(num)
    soma += num

maior = max(lista)
menor = min(lista)

print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')
print(f'A soma dos {len(lista)} números é {soma}.')