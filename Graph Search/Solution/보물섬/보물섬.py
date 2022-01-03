import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    
    visited = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = 1

    while q:
        x, y, dist = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] != "W":
                    visited[nx][ny] = 1
                    q.append([nx, ny, dist + 1])

    return dist

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != "W":
            ans = max(bfs(i, j), ans)
            
print(ans)

'''
output : 8
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''