import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
h, w = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(w)]

monkey = [[0, 1], [1, 0], [0, -1], [-1, 0]]
horse = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

v = [[[0] * (k + 1) for _ in range(h)] for _ in range(w)]

def bfs():

    v[0][0][0] = 1
    q = deque([[0, 0, 0]])

    while q:
        x, y, m = q.popleft()

        if x == w -1 and y == h - 1:
            return v[x][y][m] - 1

        for dx, dy in monkey:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < w and 0 <= ny < h and not v[nx][ny][m]:
                if not maps[nx][ny]:

                    v[nx][ny][m] = v[x][y][m] + 1
                    q.append([nx, ny, m])

        if m < k:
            for dx, dy in horse:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < w and 0 <= ny < h and not v[nx][ny][m + 1]:
                    if not maps[nx][ny]:

                        v[nx][ny][m + 1] = v[x][y][m] + 1
                        q.append([nx, ny, m + 1])
    return -1

print(bfs())


'''
output : 4

1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
'''