# 点分十进制IP地址 转换成二进制输出

ten_input = input('输入需要转换的IP地址：\n')
lista = ten_input.split('.')

index = 0
for i in lista:
    lista[index] = bin(int(i)).replace('0b', '')
    index += 1
    print(lista)

print('.'.join(lista))
