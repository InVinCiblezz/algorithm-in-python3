#!/usr/bin/env python3
from heapq import heappush, heappop
# ============== 代码实现开始 =============

#  n: 初始点数
#  k: 哈夫曼树的叉树
#  w: w[i] 表示第i个点的点权
# 返回值：最终编码的长度


def solve(n, k, w):
    Q = []
    sum = 0
    for i in range(n):
        heappush(Q, w[i])

    r = 0 if (n - 1) % (k - 1) == 0 else k - n % (k - 1)
    n += r
    for _ in range(r):
        heappush(Q, 0)

    while n > 1:
        newEle = 0
        for _ in range(k):
            newEle += heappop(Q)
        sum += newEle
        heappush(Q, newEle)
        n -= k - 1

    return sum

# ============= 代码实现结束 ===============


if __name__ == '__main__':
    n, k = map(int, input().split(' '))
    w = []
    for i in range(n):
        w.append(int(input()))
    print(solve(n, k, w))
