lista = []
for c in range(1, 6):
   num =  int(input(f'Digite o número {c}: '))
   lista.append(num)
   
maior = max(lista)
menor = min(lista)

print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')
