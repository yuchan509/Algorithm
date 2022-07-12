from collections import deque
from itertools import permutations

def solution(k, dungeons):

    ans = 0
    n = len(dungeons)
    for case in permutations(range(n), n):

        q = deque(case)
        cnt, current = 0, k

        while q:
            idx = q.popleft()
            need, waste = dungeons[idx]

            if need <= current:
                current -= waste
                cnt += 1

            else: continue

        ans = max(ans, cnt)

    return ans

    
```
output : 3
k = 80
dungeons = [[80,20],[50,40],[30,10]]	
```