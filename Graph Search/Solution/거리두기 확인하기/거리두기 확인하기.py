from collections import deque

def bfs(place):
  
  d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
  people = []
  for i in range(5):
    for j in range(5):
      if place[i][j] == "P":
        people.append([i, j])

  for p in people:

    q = deque()
    q.append(p)
    visited = [[0] * 5 for _ in range(5)]
    visited[p[0]][p[-1]] = 1

    while q:
      x, y = q.popleft()
      
      for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
          if place[nx][ny] != "X":
            if place[nx][ny] == "P" and visited[x][y] <= 2:
              return 0

            else:
              visited[nx][ny] = visited[x][y] + 1
              q.append([nx, ny])
  return 1

def solution(places):
    ans = []
    for place in places:
      ans.append(bfs(place))
    return ans


```
output : [1, 0, 1, 1, 1]
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
```