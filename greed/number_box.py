#!/usr/bin/env python3

# ================= 代码实现开始 =================

Mod = 1000003
table = [[] for i in range(Mod)]


def Hash(x):
    return x % Mod

# 执行操作时会调用这个函数
# op：对应该次操作的 op（具体请见题目描述）
# x：对应该次操作的 x（具体请见题目描述）
# 返回值：如果输出为"Succeeded"，则这个函数返回 1，否则返回 0


def check(op, x):
    h = Hash(x)
    ptr = -1
    for it in range(len(table[h])):
        if table[h][it] == x:
            ptr = it
            break
    if op == 1:
        if ptr == -1:
            table[h].append(x)
            return 1
        return 0
    else:  # op = 2
        if ptr > -1:
            table[h][ptr] = table[h][-1]
            table[h].pop()
            return 1
        return 0

# ================= 代码实现结束 =================


Q = int(input())
for _ in range(Q):
    op, x = map(int, input().split())
    print("Succeeded" if check(op, x) else "Failed")
