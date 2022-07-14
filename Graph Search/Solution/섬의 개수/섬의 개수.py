import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
  
  q = deque()
  q.append([x, y])

  while q:
    x, y = q.popleft()
  
    for dx, dy in d:
      nx = x + dx
      ny = y + dy

      if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
        if arr[nx][ny] != 0:
          visited[nx][ny] = 1
          q.append([nx, ny])

  return 1

while True:

  w, h = map(int, input().split())
  
  if w == 0 and h == 0: break

  arr = [list(map(int, input().split())) for _ in range(h)]

  visited = [[0] * w for _ in range(h)]
  d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]

  ans = 0
  for i in range(h):
    for j in range(w):
      if arr[i][j] != 0 and not visited[i][j]:
        visited[i][j] = 1
        ans += bfs(i, j)

  print(ans)


```
output : 0 1 1 3 1 9
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
```