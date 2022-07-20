from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

point = []
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            if arr[i][j] == '.':
                point.append([i, j])
                
                
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[0] * m for _ in range(n)]
    
q = deque()
q.append(point[0])
visited[point[0][0]][point[0][-1]] = 1

while q:
    x, y = q.popleft()
    
    if x == point[-1][0] and y == point[-1][-1]:
        break
    
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if arr[nx][ny] != '+':
                visited[nx][ny] = visited[x][y] + 1
                visited
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            arr[i][j] = "@"
    
p = deque()
p.append([x, y])
cnt = visited[x][y]
arr[x][y] = "."
   
while p:
    x, y = p.popleft()
    if x == point[0][0] and y == point[0][-1]:
        break
    
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
            if cnt - 1 == visited[nx][ny]:
                p.append([nx, ny])
                arr[nx][ny] = "."
                cnt -= 1

for i in arr:
    print(''.join(i))


```
output :
+++++++++++
+@+.....+@+
+@+.+++.+@+
+...+@+...+
+.+++@+@+.+
+.+@@@+++.+
+.+++@+@+.+
+.@@@@@@+..
+.+++++++++
+.@@@@@@+@+
+.+++++++++
+..........
+++++++++++

13 11
+++++++++++
+.+.....+.+
+.+.+++.+.+
+...+.+...+
+.+++.+.+.+
+.+...+++.+
+.+++.+.+.+
+.......+..
+.+++++++++
+.......+.+
+.+++++++++
+..........
+++++++++++
```