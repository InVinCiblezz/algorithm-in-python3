#!/usr/bin/env python3

# ================= 代码实现开始 =================

# 将给定数组a升序排序
# n：数组大小
# a：所给数组，大小为n
# 返回值：排序后的数组


def getAnswer(n, a):
    a.sort()
    return a

# ================= 代码实现结束 =================


n = int(input())
a = list(map(int, input().split()))
a = getAnswer(n, a)
print(' '.join(map(str, a)))
