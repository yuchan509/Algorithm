import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
v = [[0] * m for _ in range(n)]

def cal(ans, x, y):
	
	if arr[x][y] == 0:
		ans += 1
	else:
		ans -= 2
	return ans

def bfs(x, y):
	q = deque()
	q.append([x, y])
	v[x][y] = 1
	
	ans = cal(0, x, y)
	
	while q:
		x, y = q.popleft()
		
		for dx, dy in d:
			nx = x + dx
			ny = y + dy
			
			if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
				if arr[nx][ny] != 1: 
					v[nx][ny] = 1
					q.append([nx, ny])
					ans = cal(ans, nx, ny)	
	return ans

answer = []
for i in range(n):
	for j in range(m):
		if arr[i][j] != 1 and not v[i][j]:
			answer.append(bfs(i, j))
			
if answer:
	print(max(answer)) if max(answer) >= 0 else print(0)
else:
	print(0)


'''
output : 4
6 5
1 2 0 1 1
0 2 1 2 0
0 0 0 2 0
1 1 1 1 1
0 0 1 1 1
0 0 1 1 1
'''