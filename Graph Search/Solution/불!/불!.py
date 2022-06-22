import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

f, q = deque(), deque()

time = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if arr[i][j] == "F":
            f.append([i, j])
            time[i][j] = 1
            
        if arr[i][j] == "J":
            q.append([i, j, 1])
            

def bfs_fire():
    while f:
        x, y = f.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c and not time[nx][ny]:
                if arr[nx][ny] != "#":
                    time[nx][ny] = time[x][y] + 1
                    f.append([nx, ny])

bfs_fire()

visited = [[0] * c for _ in range(r)]

def bfs():
    
    while q:
        x, y, cnt = q.popleft()
        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
             return cnt

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] != "#":
                    if not time[nx][ny] or time[nx][ny] > cnt + 1:
                        visited[nx][ny] = 1
                        q.append([nx, ny, cnt + 1]) 
    return "IMPOSSIBLE"

print(bfs())


# Run.
'''
output : 3
4 4
####
#JF#
#..#
#..#
'''