from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

w = deque()
q = deque()

time = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == "*":
            w.append([i, j])
            time[i][j] = 1
            
        if arr[i][j] == "S":
            q.append([i, j, 1])
            
def bfs_water():
    while w:
        x, y = w.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not time[nx][ny]:
                if arr[nx][ny] != "D" and arr[nx][ny] != "X":
                    time[nx][ny] = time[x][y] + 1
                    w.append([nx, ny])

bfs_water()

visited = [[0] * m for _ in range(n)]

def bfs():
    
    while q:
        x, y, cnt = q.popleft()
        if arr[x][y] == "D":
             return cnt - 1

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] != "X":
                    if not time[nx][ny] or time[nx][ny] > cnt + 1:
                        visited[nx][ny] = 1
                        q.append([nx, ny, cnt + 1]) 
    return "KAKTUS"

print(bfs())


# Run.
'''
output : 3
3 3
D.*
...
.S.
'''

'''
output : KAKTUS
3 3
D.*
...
..S
'''