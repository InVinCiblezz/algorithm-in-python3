#!/usr/bin/env python3

# ================= 代码实现开始 =================
import queue
pq = queue.PriorityQueue()
# 这是求解整个问题的函数
# w：题目描述中的 w（所有）
# n：题目描述中的 n
# 返回值：答案


def getAnswer(n, w):
    for i in range(n):
        pq.put(w[i])
    sum = 0
    while pq.qsize() > 1:
        newEle = 0
        for k in range(2):
            newEle += pq.get()
        sum += newEle
        pq.put(newEle)
    return sum

# ================= 代码实现结束 =================


n = int(input())
w = []
for i in range(n):
    x = int(input())
    w.append(x)
print(getAnswer(n, w))
