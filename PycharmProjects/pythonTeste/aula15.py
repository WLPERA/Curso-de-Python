n = s = 0
while True:
    n = int(input('Digite um número :'))
    if n == 999:
        break
    s += n
#print('A Soma vale {}'.format(s))
print(f'A Soma vale {s}')
