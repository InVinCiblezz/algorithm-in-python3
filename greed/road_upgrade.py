#!/usr/bin/env python3

# ================= 代码实现开始 =================
N = 500005


class UnionSet:
    parent = [0 for i in range(N)]

    # init
    def init(self, n):
        for i in range(1, n + 1):
            self.parent[i] = i

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        setX = self.find(x)
        setY = self.find(y)
        if setX == setY:
            return False
        else:
            self.parent[setX] = setY
        return True


us = UnionSet()
# 给定一个n个点m条边的无向图，第i条边边权为i，求所有需要升级的边
# n：如题意
# m：如题意
# U：大小为m的数组，表示m条边的其中一个端点
# V：大小为m的数组，表示m条边的另一个端点
# 返回值：所有需要升级的边，从小到大排列；第一小问的答案自然即为返回值的size，所以你不必考虑如何返回size


def getAnswer(n, m, U, V):
    global us
    ans = []
    us.init(n)
    for i in range(m - 1, -1, -1):
        if us.merge(U[i], V[i]):
            ans.append(i + 1)
    ans.reverse()
    return ans

# ================= 代码实现结束 =================


n, m = map(int, input().split())
U, V = [], []

for i in range(m):
    u, v = map(int, input().split())
    U.append(u)
    V.append(v)

ans = getAnswer(n, m, U, V)
print(len(ans))
print(*ans, sep='\n')
