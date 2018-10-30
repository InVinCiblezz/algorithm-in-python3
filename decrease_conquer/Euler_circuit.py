#!/usr/bin/env python3
import sys
# ================= 代码实现开始 =================

allOne = 0
vis = [[], []]
ans = ''


def towPow(x):
    return 1 << x


def dfs(u):
    global vis, ans
    for i in range(2):
        if not vis[i][u]:
            v = ((u << 1) | i) & allOne
            vis[i][u] = 1
            dfs(v)
            ans += str(i)


# 本函数求解大转盘上的数，你需要把大转盘上的数按顺时针顺序返回
# n：对应转盘大小，意义与题目描述一致，具体见题目描述。
# 返回值：将大转盘上的数按顺时针顺序放到一个string中并返回


def getAnswer(n):
    global allOne, ans, vis
    allOne = towPow(n - 1) - 1
    ans = ''
    for i in range(2):
        vis[i] = [0 for i in range(towPow(n - 1))]
    dfs(0)
    return ans

# ================= 代码实现结束 =================


sys.setrecursionlimit(2333333)
print(getAnswer(int(input())))
