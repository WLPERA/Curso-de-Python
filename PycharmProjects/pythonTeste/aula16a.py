num = [2,5,9,12]
print (num)
print(num[2])
num[2]=3
print(num[2])
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(f'Essa lista tem {len(num)} elementos')
num.insert(2,0)
print(num)
num.pop()
print(num)
num.remove(0)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
