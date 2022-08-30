from collections import deque

def solution(queue1, queue2):
    
    ans = 0
    q1, q2 = deque(queue1), deque(queue2)
    a, b = sum(q1), sum(q2)
    mid = (a + b) / 2
    
    if (a + b) % 2 != 0: 
        return -1
    
    while q1 and q2:
        
        if a > mid:
            a -= q1.popleft()
            
        elif a < mid:
            a +=  q2[0]
            q1.append(q2.popleft())
            
        else:
            return ans
        
        ans += 1

    return -1
    
```
output : 2
queue1 = [3, 2, 7, 2]	
queue2 = [4, 6, 5, 1]	
```