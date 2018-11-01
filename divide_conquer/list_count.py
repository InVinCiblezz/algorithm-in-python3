#!/usr/bin/env python3

# ================= 代码实现开始 =================
N = 300005
n, d, max_value, min_value = 0, 0, [0 for i in range(N)], [0 for i in range(N)]
a = []
# 求出有多少个_a数组中的连续子序列（长度大于1），满足该子序列的最大值最小值之差不大于_d
# _n：_a数组的长度
# _d：所给d
# _a：数组_a，长度为_n
# 返回值：满足条件的连续子序列的个数


def solve(left, right):
    if left == right:
        return 0
    mid = (left + right) >> 1
    ans = solve(left, mid) + solve(mid + 1, right)
    for i in range(mid + 1, right + 1):
        min_value[i] = a[i] if i == mid + 1 else min(min_value[i - 1], a[i])
        max_value[i] = a[i] if i == mid + 1 else max(max_value[i - 1], a[i])

    mn, mx, pos = 0, 0, right
    i = mid
    while i >= left and pos > mid:
        mn = a[i] if i == mid else min(mn, a[i])
        mx = a[i] if i == mid else max(mx, a[i])
        while pos > mid and max(mx, max_value[pos]) - min(mn, min_value[pos]) > d:
            pos -= 1
        ans += pos - mid
        i -= 1
    return ans


def getAnswer(_n, _d, _a):
    global n, d, a
    n = _n
    d = _d
    a = _a
    return solve(0, n - 1)

# ================= 代码实现结束 =================


n, d = map(int, input().split())
a = list(map(int, input().split()))
print(getAnswer(n, d, a))
