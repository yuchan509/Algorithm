from collections import deque

n, k = map(int, input().split())
q = deque(i for i in range(1, n + 1))

ans = []
idx = 1
while q:
    x = q.popleft()
    
    if idx % k != 0: 
        q.append(x)
        
    else:
        ans.append(str(x))
    idx += 1
    
print('<' + ', '.join(ans) + '>')

    
```
output : <3, 6, 2, 7, 5, 1, 4>
7 3
```