num = int(input('Digite um número: '))

print('='*15)
print(f'TABUADA DO {num} ') 
print('='*15)   
  
for c in range(1, 11):
    print(f'{c} x {num} =',(c *  num))
