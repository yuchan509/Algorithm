import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs():
	
	res = []
	q = deque()
	for i in range(n):
		for j in range(n):
			if arr[i][j] != 0:
				q.append([i, j])

	while q:
		x, y = q.popleft()

		cnt = 0
		for dx, dy in d:
			nx = x + dx
			ny = y + dy
			
			if 0 <= nx < n and 0 <= ny < n:
				if arr[nx][ny] == 0:
					cnt += 1
					
		res.append([x, y, max(0, arr[x][y] - cnt)])
		
	for r, c, v in res:
		arr[r][c] = v
		
	return 1

ans = 0
while max(map(max, arr)) != 0:
	ans += bfs()
	
print(ans)


'''
output : 3
3
0 0 1
2 2 0
2 2 0
'''