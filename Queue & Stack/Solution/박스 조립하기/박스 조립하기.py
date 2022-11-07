# B -> C, B -> O -> C, O -> O
# C -> B, B -> B -> C, B -> C -> C

from collections import deque

q = deque(list(input()))
stack = []

while q:
	x = q.popleft()

	if not stack:
		if x == "B":
			stack.append(x)
		else:
			break

	else:
		if stack[-1] == "B":
			if x == "C":
				stack.pop()
			else:
				stack.append(x)

if stack or q:
	print("X")
else:
	print("O")

    
'''
output : O
BBCCBC
'''