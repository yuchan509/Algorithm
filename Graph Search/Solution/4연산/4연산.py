from collections import deque

def bfs(s, t):
    
    q = deque()
    q.append([s, ''])
    
    oper = ['*', '+', '/']
  
    while q:
        x, op = q.popleft()
       
        if x == t:
            return op
        
        for idx, pos in enumerate([x * x, 2 * x, 1]):
            if 0 < pos <= t and pos not in v:
                v.add(pos)
                q.append([pos, op + oper[idx]])
    return -1

s, t = map(int, input().split())
v = set({s})

if s == t:
    print(0)
else:
    print(bfs(s, t))


```
output : +*+
7 392
```