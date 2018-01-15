a = {'1': 'a', '2': 'b', 'b': 'B', 'a': 'A'}
# 强制转换成列表,直接用列表方法sort排序
lista = list(a.items())

lista.sort()
print(lista)

# 先获取字典中的键，然后按键排序，排完之后再读取相应的值
list_keys = list(a.keys())
list_keys.sort()

# 两种读值方法，下面的似乎更高效
for key in list_keys:
    print(a[key], end=' ')

for key in list_keys:
    print(a.get(key))

