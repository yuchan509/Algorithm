from collections import deque

def solution(maps):

    ans = []

    n, m = len(maps), len(maps[0])
    v = [[0] * m for _ in range(n)]

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def bfs(x, y):

        v[x][y] = 1
        q = deque([[x, y]])

        res = 0
        while q:
            x, y = q.popleft()
            res += int(maps[x][y])

            for dx, dy in d:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and not v[nx][ny]:
                        v[nx][ny] = 1
                        q.append([nx, ny])
        return res

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not v[i][j]:
                ans.append(bfs(i, j))

    ans.sort()

    return ans if ans else [-1]


# Run.
'''
output : [1, 1, 27]
maps = ["X591X","X1X5X","X231X", "1XXX1"]	
'''