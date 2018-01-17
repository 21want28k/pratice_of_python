seq = [1, 5, 6, 4, 6, 4, 6, 6, 6, 4, 4]

seq.sort()
print(seq)

def search(seq, number, start=0, end=len(seq)-1):
    if start == end and number != seq[end]:
        return '未找到'
    elif start == end:
        return end
    else:
        middle = (start+end)//2
        if number > seq[middle]:
            return search(seq, number, middle+1, end)
        else:
            return search(seq, number, start, middle)


print(search(seq,4))