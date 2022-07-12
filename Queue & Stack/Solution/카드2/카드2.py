from collections import deque

n = int(input())
q = deque([i for i in range(1, n + 1)])

while len(q) > 1:
    q.popleft()
    second = q.popleft()
    q.append(second)
    
print(q[0])

    
```
output : 4
6
```