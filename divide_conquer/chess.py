#!/usr/bin/env python3

# ================= 代码实现开始 =================
N = 505 * 2
M = N * N


class E:
    def __init__(self):
        self.next = 0
        self.to = 0


e = [E() for i in range(M)]
cnt, ihead, mc = 0, [0 for i in range(N)], [0 for i in range(N)]
vis = [False for i in range(N)]


def add(x, y):
    global cnt, e, ihead
    cnt += 1
    e[cnt].next = ihead[x]
    e[cnt].to = y
    ihead[x] = cnt


def dfs(x):
    global mc, vis
    i = ihead[x]
    while i != 0:
        y = e[i].to
        if not vis[y]:
            vis[y] = True
            if mc[y] == 0 or dfs(mc[y]):
                mc[x] = y
                mc[y] = x
                return True
        i = e[i].next
    return False

# 求解棋盘上最多能放多少个“车”
# n：棋盘的大小为n×n的
# board：所给棋盘，对于某个位置上的数：若值为1表示可以放“车”；若值为0表示不能放“车”
# 返回值：能放“车”的最大个数


def getAnswer(n, board):
    global cnt, mc, ihead, vis

    # init
    cnt = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i - 1][j - 1] == 1:
                add(i, j + n)

    ans = 0
    for i in range(1, n + 1):
        if mc[i] == 0:
            vis = [0 for i in range(1, n * 2 + 1)]
            if dfs(i):
                ans += 1

    return ans
# ================= 代码实现结束 =================


n = int(input())
_e = []
for i in range(n):
    t = list(map(int, input().split()))
    _e.append(t)
print(getAnswer(n, _e))
