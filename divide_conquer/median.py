#!/usr/bin/env python3
from heapq import heappop, heappush
''' ================ 代码实现开始 ============== '''
bigHeap = []
smallHeap = []


# 向当前数列末尾插入一个数a
def add(a):
    if len(bigHeap) == 0 or -bigHeap[0] >= a:
        heappush(bigHeap, -a)
        if len(bigHeap) - len(smallHeap) > 1:
            heappush(smallHeap, -heappop(bigHeap))
    else:
        heappush(smallHeap, a)
        if len(smallHeap) - len(bigHeap) > 1:
            heappush(bigHeap, -heappop(smallHeap))


# 返回值：当前序列中位数的值
def getMedian():
    if len(bigHeap) > len(smallHeap):
        return -bigHeap[0]
    else:
        return smallHeap[0]


''' ================ 代码实现结束 ============== '''

if __name__ == '__main__':
    n = int(input())
    a = input().split(' ')
    for i in range(2 * n - 1):
        x = int(a[i])
        add(x)
        if i % 2 == 0:
            print(getMedian())
