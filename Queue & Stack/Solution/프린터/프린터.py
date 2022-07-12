from collections import deque

def solution(priorities, location):
    
    ans = []
    q = deque([[p, idx] for idx, p in enumerate(priorities)])

    while len(q) > 1:
        p, i = q.popleft()
        
        if p < max(q)[0]:
            q.append([p, i])
        
        else:
            ans.append(i)
        
    ans.append(q[0][-1])

    return ans.index(location) + 1

    
```
output : 1
priorities = [2, 1, 3, 2]	
location = 2	
```