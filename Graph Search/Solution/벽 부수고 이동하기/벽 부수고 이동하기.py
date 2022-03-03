from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs():

    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1
    
    while q:
        x, y, w = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not arr[nx][ny] and not visited[nx][ny][w]:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])

                if not w and arr[nx][ny]:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])

    return -1

print(bfs())


# Run.
'''
output : 15
6 4
0100
1110
1000    
0000
0111
0000
'''
