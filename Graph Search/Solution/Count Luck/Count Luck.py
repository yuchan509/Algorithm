from collections import deque

def bfs(arr, k):
    
    q = deque()
    visited = [[0] * m for _ in range(n)]
    
    # left(0), up(1), down(2), right(3)
    # Coner -> left(0) & right(3) : horizontal <-> up(1) & down(2) : vertical
    # :: horizontal <-> vertical 
    d = [(0, 0, -1), (1, -1, 0), (2, 1, 0), (3, 0, 1)]
    
    r, c = 0, 0
    for i in range(n):
        for j in range(m):
            # Start index
            if arr[i][j] == "M": 
                # -1 : non-direct
                q.append([i, j, -1])
                visited[i][j] = 1

            # End index
            if arr[i][j] == "*":
                r, c = i, j

    while q:
        x, y, direct = q.popleft()

        # when end point => return.
        if x == r and y == c:
            return "Impressed" if visited[x][y] - 1 == k else "Oops!"

        # (x, y, prev direct) -> Count movable index (0 <= cross <= 4)
        cross = 0
        for curdir, dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != "X" and not visited[nx][ny]:
                    cross +=  1
        
        # In range n x n (left -> up -> down -> right)
        for curdir, dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != "X" and not visited[nx][ny]:
                    
                    # prev direct + current direct != 3 -> Changed direction.
                    # cross count >= 2 -> crossroads!
                    if (direct + curdir) != 3  and cross > 1:
                        visited[nx][ny] = visited[x][y] + 1                            

                    else:
                        visited[nx][ny] =  visited[x][y]                 
                    
                    q.append([nx, ny, curdir])
  
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    k = int(input())
    print(bfs(arr, k))


# Run.
'''
output :Impressed
        Impressed
        Oops!
3
2 3
*.M
.X.
1
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
3
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4
'''
