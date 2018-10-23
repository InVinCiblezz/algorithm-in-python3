#maximal rect in a histogram
import sys
class Stack:
    def __init__(self):
        self.items = []
        self.length = -1

    def isEmpty(self):
        return -1 is self.length

    def push(self, item):
    	self.length += 1
    	self.items.append(item)

    def pop(self):
        if -1 is self.length:
        	return False
        item = self.items[self.length]
        del self.items[self.length]
        self.length -= 1
        return item

    def top(self):
    	return self.items[self.length]

    def size(self):
        return self.length + 1

n = int(sys.stdin.readline().strip())
H = list(sys.stdin.readline().strip().split())
for i in range(n):
	H[i] = int(H[i])
H.append(-1)#place a guard

#init
M = Stack()
maxRect = 0
k = 0
length = 0

while k <= n:
	if M.isEmpty() or (H[M.top()] <= H[k]):
		M.push(k)
		k = k + 1
	else:
		t = M.pop()
		if M.isEmpty():
			length = k
		else:
			length = k - M.top() - 1
		maxRect = max(maxRect, H[t] * length)
print(maxRect)
