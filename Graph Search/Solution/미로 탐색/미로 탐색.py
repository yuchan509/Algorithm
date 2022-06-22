import sys
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = [[0] * m for i in range(n)]

def bfs():
    
    q = deque()
    q.append([0, 0, 1])
    
    while q:
        
        x, y, cnt = q.popleft()
        visited[x][y] = 1
        
        if x == n - 1 and y == m - 1:
            break
            
        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny, cnt + 1])
    return cnt

print(bfs())

# Run.
'''
output : 15
4 6
101111
101010
101011
111011
'''
