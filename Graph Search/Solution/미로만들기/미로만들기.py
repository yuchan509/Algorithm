import sys
import heapq

n = int(input())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs():

    q = []
    v = [[-1] * n for _ in range(n)]
    heapq.heappush(q, [0, 0, 0])
    v[0][0] = 0

    while q:
        cnt, x, y = heapq.heappop(q)

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == -1:

                if maps[nx][ny] == 0:
                    v[nx][ny] = cnt + 1
                    heapq.heappush(q, [cnt + 1, nx, ny])
                else:
                    v[nx][ny] = cnt
                    heapq.heappush(q, [cnt, nx, ny])
    return v[-1][-1]

print(bfs())



```
output : 2
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
```