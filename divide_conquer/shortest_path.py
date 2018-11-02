#!/usr/bin/env python3
import queue
# ================= 代码实现开始 =================
N = 100005
graph = [[]for i in range(N)]
pq = queue.PriorityQueue()
flag = [False for i in range(N)]
mind = [0 for i in range(N)]
# 这个函数用于计算答案（最短路）
# n：节点数目
# m：双向边数目
# U,V,W：分别存放各边的两端点、边权
# s,t：分别表示起点、重点
# 返回值：答案（即从 s 到 t 的最短路径长度）


def shortestPath(n, m, U, V, W, s, t):
    global graph, pq, flag, mind
    while pq.qsize() > 0:
        pq.get()
    for i in range(1, n + 1):
        graph[i].clear()
        mind[i] = 0x7ff7f7f
        flag[i] = False

    for i in range(m):
        graph[U[i]].append((V[i], W[i]))
        graph[V[i]].append((U[i], W[i]))

    mind[s] = 0
    pq.put((0, s))

    # Dijkstra
    while pq.qsize() > 0:
        u = pq.get()[1]
        if not flag[u]:
            flag[u] = True
            for it in graph[u]:
                v, w = it
                if w + mind[u] >= mind[v]:
                    continue
                mind[v] = mind[u] + w
                pq.put((mind[v], v))
    return mind[t]
# ================= 代码实现结束 =================


n, m, s, t = map(int, input().split())
U, V, W = [], [], []
for i in range(m):
    u, v, w = map(int, input().split())
    U.append(u)
    V.append(v)
    W.append(w)

print(shortestPath(n, m, U, V, W, s, t))
