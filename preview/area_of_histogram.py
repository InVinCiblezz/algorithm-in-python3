#maximal rect in a histogram
import sys
total = int(sys.stdin.readline().strip())
line = list(sys.stdin.readline().strip().split())
for f in range(total):
	line[f] = int(line[f])
arr = 0
for i, value in enumerate(line):
	sum = value
	if i > 0:#left side
		for c in range(i):
			if line[i - c - 1] < value:
				break
			else:
				sum += value
	if i < total:#right side
		for v in range(total - i -1):
			if line[i + v + 1] < value:
				break
			else:
				sum += value
	if arr < sum:
		arr = sum
print(arr)