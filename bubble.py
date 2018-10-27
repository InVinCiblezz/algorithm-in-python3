#!/usr/bin/env python3

# ================= 代码实现开始 =================
# 这是进行排序的函数
# n：题目描述中的 n
# A：各同学的算法训练营成绩
# DS：各同学的数据结构训练营成绩
# 返回值：将要输出的数字依次加入到返回值的数组中


def getAnswer(n, A, DS, id, sum):
    ans = []
    cnt = 0

    for i in range(n):
        for j in range(n - 1, 0, -1):
            if j == i:
                break
            if sum[j] > sum[j - 1] or sum[j] == sum[j - 1] and A[j] > A[j - 1]:
                id[j], id[j - 1] = id[j - 1], id[j]
                sum[j], sum[j - 1] = sum[j - 1], sum[j]
                A[j], A[j - 1] = A[j - 1], A[j]
                DS[j], DS[j - 1] = DS[j - 1], DS[j]
                cnt += 1

    for i in range(n):
        ans.append(id[i])
        ans.append(sum[i])
        ans.append(A[i])
        ans.append(DS[i])

    ans.append(cnt)
    return ans

# ================= 代码实现结束 =================


n = int(input())
A = []
DS = []
sum, id = [], []

for i in range(n):
    a, ds = map(int, input().split())
    A.append(a)
    DS.append(ds)
    id.append(i + 1)
    sum.append(a + ds)

ans = getAnswer(n, A, DS, id, sum)
cnt = 0
for i in range(n):
    print(' '.join(map(str, ans[cnt:cnt + 4])))
    cnt += 4
print(ans[cnt])
