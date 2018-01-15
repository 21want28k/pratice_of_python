# 用enumerate 按索引进行迭代
strings = ['a11a ', 'b11b', 'a  a', 'a  a', '  ', ' ']

print(list(enumerate(strings)))

for index, string in enumerate(strings):
    # 第一步删除空格
    while string.isspace():
        del strings[index]
        print(strings)
        # 因为del会删去 原列表，所以删去之后index 索引就会超出范围，利用if句做约束
        if index == len(strings):
            break
    # 同样，由于先删去的空格 所以会造成索引超出范围，再次做约束。
    if ('11' in string or ' ' in string) and index < len(strings):
        strings[index] = strings[index].replace('11', '')
        strings[index] = strings[index].replace(' ', '')
        print(strings)


  # 对strings中的每一个元素进行判断删除，修改。
strings = ['a11a', 'b11b', 'a  a', 'a  a', '  ', ' ']

index1 = 0

while index1 < len(strings):
    if strings[index1].isspace():
        del strings[index1]
    elif ' ' in strings[index1]:
        strings[index1] = strings[index1].replace(' ', '')
    else:
        index1 += 1


  # 和第一种方法不同，我先做修改，但是空格会被修改成''，最后还要进行全部删除，才能达到目的
strings = ['a11a ', 'b11b', 'a  a', 'a  a', '  ', ' ']

for index, string in enumerate(strings):
    if '11' in string:
        strings[index] = strings[index].replace('11', '')
    if ' ' in string:
        strings[index] = strings[index].replace(' ', '')

while '' in strings:
    strings.remove('')