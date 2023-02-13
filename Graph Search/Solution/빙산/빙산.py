import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split()))for _ in range(n)]

def check(q):
    result = deque()
    while q:
        x, y = q.popleft()

        cnt = 0
        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny]:
                cnt += 1
        result.append([x, y, cnt])

    return result


def floodfill(x: int, y: int) -> int:
    v[x][y] = 1
    q = deque([[x, y]])

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
                if maps[nx][ny]:
                    v[nx][ny] = 1
                    q.append([nx, ny])
    return 1


time = 0
while True:

    time += 1
    island = 0
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    iceberg = deque([(i, j) for i in range(n) for j in range(m) if maps[i][j]])
    if not iceberg:
        time = 0
        break

    info = check(iceberg)
    for x, y, cnt in info:
        value = maps[x][y] - cnt
        maps[x][y] = value if value > 0 else 0

    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] and not v[i][j]:
                island += floodfill(i, j)

    if island > 1:
        break

print(time)


'''
output : 2

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''