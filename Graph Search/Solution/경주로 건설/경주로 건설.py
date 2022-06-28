from collections import deque

def solution(board):
    
    n = len(board)
    d = {0 : (0, -1), 1 : (-1, 0), 2: (1, 0), 3 :(0, 1)}

    visited = [[[float("inf")] * 4 for _ in range(n)] for _ in range(n)]
    visited[0][0] = [0, 0, 0, 0]

    q = deque()
    q.append([0, 0, -1])

    while q:
        x, y, direct = q.popleft()

        for curdir, dx in d.items():
            nx, ny = x + dx[0], y + dx[-1]

            if 0 <= nx < n and 0 <= ny < n:

                if direct != -1 and (direct + curdir) != 3 and direct != curdir:
                    cost = 600
                else:
                    cost = 100

                if board[nx][ny] != 1 and visited[nx][ny][curdir] > visited[x][y][direct] + cost:                    
                    visited[nx][ny][curdir] = visited[x][y][direct] + cost
                    q.append([nx, ny, curdir])

    return min(visited[-1][-1])


# Run.
board = [[0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1],
        [0,0,1,0,0,0,1,0],
        [0,1,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,0]]
        
solution(board)