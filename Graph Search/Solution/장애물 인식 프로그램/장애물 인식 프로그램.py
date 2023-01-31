import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().strip())) for _ in range(n)]
v = [[0] * n for _ in range(n)]

def bfs(x, y):
    v[x][y] = 1
    q = deque([[x, y]])
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    cnt = 0
    while q:
        cnt += 1
        x, y = q.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] and not v[nx][ny]:
                    v[nx][ny] = 1
                    q.append([nx, ny])
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if maps[i][j] and not v[i][j]:
            ans.append(bfs(i, j))
ans.sort()

print(len(ans))
for size in ans:
    print(size)


# Run.
'''
output : 
3
7
8
9

7
1110111
0110101
0110101
0000100
0110000
0111110
0110000
'''