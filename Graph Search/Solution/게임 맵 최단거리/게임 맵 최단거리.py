from collections import deque

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([0, 0])
    
    visited = [[0] * m for _ in range(n)]
    
    while q:
        x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[-1][-1] + 1
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
    return -1


# Run.(1 : 가능, 0 : 불가능)
maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

solution(maps)