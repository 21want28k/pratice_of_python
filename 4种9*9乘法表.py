s = 0

for i in range(1,10):
    for j in range(1,i+1):
        s = i*j
        print('%d*%d=%2d' % (i, j, s), end=' ')
    print('')
print('\n')


for i in range(1,10):
    for j in range(i,10):
        s = i*j
        print('%d*%d=%2d' % (i, j, s), end=' ')
    print('')
print('\n')


for i in range(1,10):
    print((9-i)*'       ',end='')
    for j in  range(1,i+1):
        s = i*j
        print('%d*%d=%2d' % (i, j, s), end=' ')
    print('')
print('\n')


for i in range(1,10):
    print(((i-1)*'       '),end='')
    for j in range(i,10):
        s = i*j
        print('%d*%d=%2d' % (i, j, s), end=' ')
    print('')
