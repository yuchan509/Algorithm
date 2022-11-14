import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(q):
	result = set()
	
	while q:
		x, y = q.popleft()
		v[x][y] = 1
	
		for dx, dy in d:
			nx = x + dx
			ny = y + dy
			
			if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
				if arr[nx][ny] == 1:
					result.add((nx, ny))
				
				else:
					v[nx][ny] = 1
					q.append((nx, ny))
	
	return result

def check(x, y):
	q = deque()
	q.append([x, y])
	
	while q:
		x, y = q.popleft()
		chk[x][y] = 1
	
		for dx, dy in d:
			nx = x + dx
			ny = y + dy
			
			if 0 <= nx < n and 0 <= ny < m and not chk[nx][ny]:
				if arr[nx][ny] == 1:
					chk[nx][ny] = 1
					q.append([nx, ny])
	return 1
	
time = 0 
island = 0
while island < 2:
	
	island = 0
	queue = deque()
	for i in range(n):
		for j in range(m):
			if not v[i][j] and arr[i][j] == 0:
				queue.append([i, j])
	
	result = bfs(queue)
	for x, y in result:
		arr[x][y] = 0
		
	chk = [[0] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
				if not chk[i][j] and arr[i][j] == 1:
					island += check(i, j)

	time += 1
	
	if not island:
		print(-1)
		exit(0)
		
print(time)


'''
output : 2
6 5
1 1 1 1 1
1 1 1 1 1
1 1 0 1 1
1 1 0 1 1
1 1 1 1 1
1 1 0 1 1
'''