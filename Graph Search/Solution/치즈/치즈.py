import sys
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs():

    q = deque([(0, 0)])
    v = [[0] * m for _ in range(n)]
    v[0][0] = 1

    cnt = 0
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
                v[nx][ny] = 1
                if maps[nx][ny] == 1:
                    cnt += 1
                    maps[nx][ny] = 0
                else:
                    q.append([nx, ny])
    return cnt

ans, chk = 0, n * m
while True:
    run = bfs()
    if run != 0:
        ans += 1
        chk = min(chk, run)
    else:
        print(ans, chk, sep = '\n')
        break


'''
output : 3, 5 (row)
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''

