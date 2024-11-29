soma = 0 
mult = []
for c in range(1, 51):
    if c % 3 == 0:
        mult.append(c)
        soma += c
print(f'A soma dos multiplos de 3 é {soma}.')