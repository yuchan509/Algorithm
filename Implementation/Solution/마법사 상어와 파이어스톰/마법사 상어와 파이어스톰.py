import sys
import copy
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** n)]
L = list(map(int, input().split()))

# 나눈 격자만큼 시계 방향으로 90도 회전 함수.
def rotate(L):

    global arr
    ans = copy.deepcopy(arr)
    size = 2 ** L
    for i in range(0, 2 ** n, size):
        for j in range(0, 2 ** n, size):
            for x in range(size):
                for y in range(size):
                    arr[i + y][j - x + size - 1] = ans[i + x][j + y]

# 가장 큰 덩어리 얼음 칸 개수 계산 함수.
d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
visited = [[0] * (2 ** n) for _ in range(2 ** n)]

def bfs(x, y):

    cnt = 1
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                if arr[nx][ny] != 0 and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    return cnt

for l in L:

    rotate(l)
    chk = []
    for x in range(2 ** n):
        for y in range(2 ** n):

            cnt = 0
            for dx, dy in d:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and arr[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                chk.append([x, y])

    for x, y in chk:
        if arr[x][y] > 0:
            arr[x][y] -= 1

ans1 = sum(sum(arr, []))
ans2 = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if arr[i][j] != 0 and not visited[i][j]:
            ans2 = max(ans2, bfs(i, j))

print(ans1)
print(ans2)

'''
output : 284 64
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1
'''