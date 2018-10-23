#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
N = 100005

class node:
    def __init__(self):
        self.val = self.l = self.r = 0

t = [node() for i in range(N)]

root, cnt = 0, 0

def insert(v, x):
    if x == 0:
        global cnt
        x = node()
        x.val = v
        return x
        
    if (x.val > v):
        x.l = insert(v, x.l)
    else:
        x.r = insert(v, x.r)
    return x

def dlr(x, ans):
    if x != 0:
        ans.append(x.val)
        dlr(x.l, ans)
        dlr(x.r, ans)
def lrd(x, ans):
    if x != 0:
        lrd(x.l, ans)
        lrd(x.r, ans)
        ans.append(x.val)
# 给定一个1到n的排列，依次插入到二叉树中，返回前序遍历和后序遍历
# n：如题意
# sequence：给定的排列，大小为n
# 返回值：将要输出的元素依次加入到返回值中
def getAnswer(n, sequence):
    global root, cnt

    root = cnt = 0 #init
    for i in range(n):
        root = insert(sequence[i], root)

    ans = []

    dlr(root, ans)
    lrd(root, ans)

    return ans

    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n = int(input())
sequence = list(map(int, input().split(' ')))
ans = getAnswer(n, sequence)
print(' '.join(map(str, ans[0:n])))
print(' '.join(map(str, ans[n:n+n])))