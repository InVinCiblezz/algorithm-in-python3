import sys
while True:
	try:
		total = int(sys.stdin.readline().strip())
		line = list(sys.stdin.readline().strip().split())
		for i in range(total):
			line[i] = int(line[i])
		line.sort()
		for i in line:
			print(i)
		break
	except:
		break	