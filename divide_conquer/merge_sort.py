#!/usr/bin/env python3
data = [2, 5, 8, 1, 23, 21, 14, 22, 9, 7]


def merge(lo, hi):
    res = []
    while lo and hi:
        if lo[0] < hi[0]:
            res.append(lo.pop(0))
        else:
            res.append(hi.pop(0))
    res = res + lo + hi
    return res


def mergeSort(data):
    length = len(data)
    if length < 2:
        return data
    mid = int(length >> 1)
    lo = mergeSort(data[:mid])  # low
    hi = mergeSort(data[mid:])  # high
    return merge(lo, hi)


print(mergeSort(data))
