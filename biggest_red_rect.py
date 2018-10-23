import sys

def maximalRectangle(H,n):
#init
	M = []
	maxRect = 0
	k = 0
	length = 0
	H.append(-1)
	while k <= n:
		if (not M) or (H[M[-1]] <= H[k]):
			M.append(k)
			k = k + 1
		else:
			t = M.pop()
			if not M:
				length = k
			else:
				length = k - M[-1] - 1
			maxRect = max(maxRect, H[t] * length)
	return(maxRect)

H = []
total = list(sys.stdin.readline().strip().split())
n = int(total[0])
m = int(total[1])
if m is 0 or n is 0:
	print(0)
	exit()

#H.append('....')
#H.append('X.X.')
#H.append('X..X')
#H.append('.XX.')
#H.append('..X.')
temp = []
res = 0
for i in range(n):
	line = sys.stdin.readline().strip()
	mList = [0] * m
	for j in range(m):
		if line[j] is '.':
			if i > 0:
				mList[j] = temp[j] + 1
			else:
				mList[j] = 1
		else:
			mList[j] = 0
	temp = mList
	res = max(res, maximalRectangle(temp, m))
print(res)