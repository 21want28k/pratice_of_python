a = [1, 2, 3, 4, 5, 3, 3, 5, 5]
b = [1, 2, 3, 4, 5, 3, 3, 5, 5]
c = [1, 2, 3, 4, 5, 3, 3, 5, 5]
# 在原列表上删除


def delete_odd_function(b):
    for i in b:
        if i % 2 == 1:
            b.remove(i)  # del b[b.index(i)]一样的效果
        print(b)


delete_odd_function(b)
'''
[2, 3, 4, 5, 3, 3, 5, 5]
[2, 4, 5, 3, 3, 5, 5]
[2, 4, 3, 3, 5, 5]
[2, 4, 3, 5, 5]
[2, 4, 3, 5]
'''


def delete_odd_function(a):
    for i in a:
        while a.count(i) != 0 and i % 2 == 1:
            del a[a.index(i)]
        print(a)


delete_odd_function(a)


def delete_odd_function(c):
    index = 0
    while index < len(c):
        if c[index] % 2 == 1:
            del c[index]  # c.pop(index) 一样的效果
        else:
            index += 1
        print(c)


delete_odd_function(c)
'''
[2, 3, 4, 5, 3, 3, 5, 5]
[2, 3, 4, 5, 3, 3, 5, 5]
[2, 4, 5, 3, 3, 5, 5]
[2, 4, 5, 3, 3, 5, 5]
[2, 4, 3, 3, 5, 5]
[2, 4, 3, 5, 5]
[2, 4, 5, 5]
[2, 4, 5]
[2, 4]
'''

# 用新列表代替原列表
d = [1, 2, 3, 4, 5, 3, 3, 5, 5]

new = []

for i in d:
    if i % 2 == 0:
        new += [i]  # new.append(i)也行
print(new)


