'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''


class Solution:

    def judge_order(self, push ,pull):
        help_list = []
        for i in push:
            help_list.append(i)
            while  len(help_list) > 0 and help_list[-1] == pull[0]:
                help_list.pop()
                pull.pop(0)

        if len(help_list) == 0:
            print('是弹出序列')
        else:
            print('不是弹出序列')


s = Solution()
push = [1, 2, 3, 4, 5]
pull = [4, 5, 3, 2, 1]
print(s.judge_order(push, pull))
'''
找一个辅助栈，按入栈顺序压入辅助栈，直到压到和第一个出栈相等的元素。
实际上就是在辅助栈上，模拟入栈出栈的这个过程
'''