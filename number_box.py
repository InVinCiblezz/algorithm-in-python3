#!/usr/bin/env python3
n = int(input())
box = set([])
length = 0

for _ in range(n):
	try:
		tmp = input().split(' ')
		op = int(tmp[0])
		number = int(tmp[1])
		if op is 1:
			box.add(number)
			c_length = len(box)

			if c_length is length:
				raise NameError()
			else:
				length += 1

		else:
			box.remove(number)
			length -= 1

		print('Succeeded')
	except:
		print('Failed')