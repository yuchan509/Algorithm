from collections import deque

def bfs(a, b):

    q = deque()
    q.append([a, 1])
  
    while q:
        x, cnt = q.popleft()
       
        if x == b: 
            return cnt

        for pos in [x * 2, int(str(x) + '1')]:
            if 0 <= pos < int(1e9) and pos not in v and pos <= b:   
                v.add(pos)
                q.append([pos, cnt + 1])
    return -1

v = set()
a, b = map(int, input().split())

print(bfs(a, b))


```
output : 5
2 162
```