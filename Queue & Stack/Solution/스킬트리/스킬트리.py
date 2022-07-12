from collections import deque

def solution(skill, skill_trees):
    
    ans = len(skill_trees)
    s = list(skill)

    for case in skill_trees:
        
        q = deque(list(case))
        skill_q = deque(s)
        cur_skill = skill_q.popleft()
        
        while len(q):

            x = q.popleft()
            if x not in s:
                continue

            else:
                if cur_skill == x:
                    if len(skill_q) > 0:
                        cur_skill = skill_q.popleft()
                else: 
                    ans -= 1
                    break
    return ans


```
output : 2
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
```