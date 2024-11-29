lista = []
pares = []
impares = []
soma = 0

for c in range(1, 11):
     try:
         num = int(input(f'Digite o número {c}:'))
         soma += num
         if num % 2 == 0:
             pares.append(num)
         else:
             impares.append(num)
     except ValueError:
        print('Digito inválido, Digite um número inteiro')
print('='*40)        
print(f'A soma de todos os números é {soma}.')
print(f'A quantidade de números pares é {len(pares)}')
print(f'A quantidade de números impares é {len(impares)}')
print('='*40)