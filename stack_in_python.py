# /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#H = []
#H.append('1 a')
#H.append('1 b')
#H.append('1 c')
#H.append('2')
#H.append('3 1')
n = int(sys.stdin.readline().strip())
S = []

for i in range(n):
	text = list(sys.stdin.readline().strip().split())

	if text[0] is '1':
		S.append(text[1])
	elif text[0] is '2':
		print(S.pop())
	else:
		print(S[int(text[1]) - 1])

