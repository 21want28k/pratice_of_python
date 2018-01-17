seq = [1, 5, 6, 4, 6, 4, 6, 6, 6, 4, 4]

seq.sort()
print(seq)
lower = 0
upper = len(seq)-1

number = int(input('输入你要查找的数'))

while True:
    if lower == upper:
        if seq[upper] != number:
            print('未找到')
        else:
            print(upper)
            count2 = 0

            for i in range(upper + 1, len(seq)):
                if seq[i] == seq[upper]:
                    count2 += 1
                else:
                    break
            print('后面一共有%d个相同的数:' % count2, i)
        break
    else:
        middle = (lower + upper)//2
        if number > seq[middle]:
            lower = middle+1
        else:
            upper = middle





