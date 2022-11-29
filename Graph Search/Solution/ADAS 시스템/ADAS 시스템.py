import sys
from queue import PriorityQueue

input = sys.stdin.readline
w, h = map(int, input().split())
arr = [list(input()) for _ in range(w)]

def bfs():
    q = PriorityQueue()
    v = [[0] * h for _ in range(w)]
    pq = {"E": 1, "P": 2, "0": 3}
    d = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    ans = 0

    for i in range(w):
        for j in range(h):
            if arr[i][j] == "S":
                q.put(["S", i, j])
                v[i][j] = 1

    while not q.empty():
        chk, x, y = q.get()

        if chk == 1:
            break

        elif chk == "S":
            for dx, dy in d[:4]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < w and 0 <= ny < h and not v[nx][ny]:
                    v[nx][ny] = 1
                    q.put([pq[arr[nx][ny]], nx, ny])

        else:
            temp = 0
            for flag, ds in enumerate(d):
                nx = x + ds[0]
                ny = y + ds[-1]

                if 0 <= nx < w and 0 <= ny < h:
                    if flag < 4 and not v[nx][ny]:
                        v[nx][ny] = 1
                        q.put([pq[arr[nx][ny]], nx, ny])

                    if arr[nx][ny] == "P":
                        temp += 1

            if arr[x][y] == "P":
                ans += (temp - 3)
            else:
                ans += temp

    return max(0, ans)


print(bfs())

'''
output : 10
4 4
P000
PPPP
000S
0EP0
'''