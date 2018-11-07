#!/usr/bin/env python3

# ================= 代码实现开始 =================
N = 5005
d = [[0 for j in range(N)] for i in range(N)]
f = [[0 for j in range(N)] for i in range(N)]
# n个物品，每个物品有体积价值，求若扔掉一个物品后装进给定容量的背包的最大价值
# n：如题
# w：长度为n+1的数组，w[i]表示第i个物品的价值（下标从1开始，下标0是一个数字-1，下面同理）
# v：长度为n+1的数组，v[i]表示第i个物品的体积
# q：如题
# qV：长度为q+1的数组，qV[i]表示第i次询问所给出的背包体积
# qx：长度为q+1的数组，qx[i]表示第i次询问所给出的物品编号
# 返回值：返回一个长度为q的数组，依次代表相应询问的答案


def getAnswer(n, w, v, q, qV, qx):
    for i in range(1, n + 1):
        for V in range(v[i]):
            d[i][V] = d[i - 1][V]
        for V in range(v[i], 5001):
            d[i][V] = max(d[i - 1][V], d[i - 1][V - v[i]] + w[i])

    for i in range(n, 0, -1):
        for V in range(v[i]):
            f[i][V] = f[i + 1][V]
        for V in range(v[i], 5001):
            f[i][V] = max(f[i + 1][V], f[i + 1][V - v[i]] + w[i])

    ans = []
    for k in range(1, q + 1):
        x, V = qx[k], qV[k]
        mx = 0
        for i in range(V + 1):
            mx = max(mx, d[x - 1][i] + f[x + 1][V - i])
        ans.append(mx)
    return ans


# ================= 代码实现结束 =================


v, w, qv, qx = [], [], [], []
v.append(-1)
w.append(-1)
qv.append(-1)
qx.append(-1)
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    v.append(a)
    w.append(b)
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    qv.append(a)
    qx.append(b)
ans = getAnswer(n, w, v, q, qv, qx)
for i in ans:
    print(i)
