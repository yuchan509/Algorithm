import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(x, y):
    q = deque([[x, y]])
    v = [[-1] * (w + 2) for _ in range(h + 2)]
    v[x][y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and v[nx][ny] == -1:
                if maps[nx][ny] == '#':
                    v[nx][ny] = v[x][y] + 1
                    q.append([nx, ny])

                elif maps[nx][ny] in '$.':
                    v[nx][ny] = v[x][y]
                    q.appendleft([nx, ny])
    return v


for _ in range(t):
    h, w = map(int, input().split())

    maps = [['.'] * (w + 2) for x in range(h + 2)]
    for i in range(h):
        maps[i + 1][1:-1] = list(input().strip())

    prisoner = [(i, j) for j in range(w + 2)
                for i in range(h + 2) if maps[i][j] == '$']

    x1, y1 = prisoner[0]
    x2, y2 = prisoner[1]

    map1 = bfs(0, 0)
    map2 = bfs(x1, y1)
    map3 = bfs(x2, y2)

    ans = sys.maxsize
    for i in range(h + 2):
        for j in range(w + 2):
            if maps[i][j] in '$*': continue

            if -1 not in [map1[i][j], map2[i][j], map3[i][j]]:

                cumsum = map1[i][j] + map2[i][j] + map3[i][j]
                if maps[i][j] == '#':
                    cumsum -= 2

                ans = min(ans, cumsum)
    print(ans)


# Run.
'''
output : 4 0 9

3
5 9
****#****
*..#.#..*
****.****
*$#.#.#$*
*********
5 11
*#*********
*$*...*...*
*$*.*.*.*.*
*...*...*.*
*********.*
9 9
*#**#**#*
*#**#**#*
*#**#**#*
*#**.**#*
*#*#.#*#*
*$##*##$*
*#*****#*
*.#.#.#.*
*********
'''