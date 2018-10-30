#!/usr/bin/env python3

# ================= 代码实现开始 =================

# 将所给数组分成连续的m份，使得数字之和最大的那一份的数字之和最小
# n：数组大小
# m：题中的m
# a：所给数组，大小为n
# 返回值：最优方案中，数字之和最大的那一份的数字之和


def check(d, n, m, a):
    sum = 0
    cnt = 1
    for i in range(n):
        if a[i] > d:
            return False
        sum += a[i]
        if sum > d:
            if cnt == m:
                return False
            cnt += 1
            sum = a[i]

    return True


def getAnswer(n, m, a):
    left = 1
    right = sum(a)

    while left <= right:
        mid = (left + right) >> 1
        if check(mid, n, m, a):
            right = mid - 1
        else:
            left = mid + 1
    return right + 1
# ================= 代码实现结束 =================


n, m = map(int, input().split())
a = list(map(int, input().split()))
print(getAnswer(n, m, a))
