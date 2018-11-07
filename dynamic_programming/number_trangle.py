#!/usr/bin/env python3

# ================= 代码实现开始 =================
# 本函数计算答案（最大经过位置数字总和）
# n：描述数字三角形大小，意义同题目描述
# a：描述整个数字三角形，第 i 行的第 j 个数存放在 a[i][j]
# 中（你需要特别注意的是，所有下标均从 1 开始，也就是说下标为 0 的位置将存放无效信息）
# 返回值：最大经过位置数字总和


def getAnswer(n, a):
    dp = [[0 for j in range(i + 2)] for i in range(n + 1)]

    dp[1][0] = dp[1][2] = 0
    dp[1][1] = a[1][1]
    for i in range(2, n + 1):
        dp[i][0] = dp[i][i + 1] = 0
        for j in range(1, i + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + a[i][j]
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, dp[n][i])
    return ans

# ================= 代码实现结束 =================


n = int(input())
a = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    a[i] = list(map(int, input().split()))
    a[i].insert(0, 0)
print(getAnswer(n, a))
