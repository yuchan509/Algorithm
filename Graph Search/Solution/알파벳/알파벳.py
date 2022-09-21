import sys

r, c = map(int, input().split())
arr = [sys.stdin.readline().strip() for _ in range(r)]

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs():

    ans = 1
    q = set()
    q.add((0, 0, arr[0][0]))

    while q and len(q) != 26:
        x, y, s = q.pop()
        ans = max(ans, len(s))

        for i in d:
            nx = x + i[0]
            ny = y + i[-1]

            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in s:
                q.add((nx, ny, s + arr[nx][ny]))
    return ans

print(bfs())




'''
output : 6
3 6
HFDFFB
AJHGDH
DGAGEH
'''