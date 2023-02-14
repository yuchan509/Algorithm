import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]

w = [[0] * c for _ in range(r)]
s = [[0] * c for _ in range(r)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

wq1, wq2, sq1, sq2 = deque(), deque(), deque(), deque()

def melt():

    while wq1:
        x, y = wq1.popleft()
        maps[x][y] = '.'

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < r and 0 <= ny < c and not w[nx][ny]:
                w[nx][ny] = 1
                if maps[nx][ny] != "X":
                    wq1.append([nx, ny])
                else:
                    wq2.append([nx, ny])

def swan():

    while sq1:
        x, y = sq1.popleft()

        if x == ex and y == ey:
            return 1

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < r and 0 <= ny < c and not s[nx][ny]:
                s[nx][ny] = 1
                if maps[nx][ny] != "X":
                    sq1.append([nx, ny])
                else:
                    sq2.append([nx, ny])
    return 0

for i in range(r):
    for j in range(c):
        if maps[i][j] == "L":
            if not sq1:
                sq1.append([i, j])
                s[i][j] = 1
            else:
                ex, ey = i, j

            maps[i][j] = '.'

        if maps[i][j] == '.':
            wq1.append([i, j])
            w[i][j] = 1

time = 0
while True:

    melt()
    if swan(): break

    wq1 = wq2
    sq1 = sq2

    wq2, sq2 = deque(), deque()

    time += 1

print(time)


'''
output : 2

8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
'''