n, m = map(int, input().split())
x, y, direct = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 1
arr[x][y] = 2
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while True:

    flag = False
    for _ in range(4): 

        direct = (direct + 3) % 4 
        dx, dy = d[direct]
        nx = x + dx
        ny = y + dy

        if not arr[nx][ny]:
            arr[nx][ny] = 2
            ans += 1
            x, y = nx, ny
            flag = True
            break

    if not flag:
        if arr[x - dx][y - dy] == 1:
            break
        else:
            x -= dx
            y -= dy
            
print(ans)


```
output : 57
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
```