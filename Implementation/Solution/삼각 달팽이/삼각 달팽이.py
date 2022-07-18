def solution(n):
  arr = [[0] * i for i in range(1, n + 1)]

  dx = [1, 0, -1]
  dy = [0, 1, -1]

  x = y = direct = 0

  for v in range(1, len(sum(arr, [])) + 1):

    arr[x][y] = v
    x += dx[direct]
    y += dy[direct]

    if not 0 <= x < n or not 0 <= y < len(arr[x]) or arr[x][y] != 0:
      
      x -= dx[direct]
      y -= dy[direct]
      direct = (direct + 1) % 3

      x += dx[direct]
      y += dy[direct]
    
  ans = sum(arr, [])
  return ans

```
output : [1,2,9,3,10,8,4,5,6,7]
n = 4
```