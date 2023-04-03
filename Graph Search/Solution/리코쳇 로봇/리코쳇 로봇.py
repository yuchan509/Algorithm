from collections import deque

def solution(board):
    visited = set()
    n, m = len(board), len(board[0])
    d = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                q.append([i, j, 0])
                visited.add((i, j))

            elif board[i][j] == "G":
                goal = (i, j)

    while q:
        x, y, cnt = q.popleft()

        if (x, y) == goal:
            return cnt

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "D":
                nx += dx
                ny += dy

            nx -= dx
            ny -= dy

            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append([nx, ny, cnt + 1])

    return -1


```
output : 7
board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
```