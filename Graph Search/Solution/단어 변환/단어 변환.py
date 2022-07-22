from collections import deque

def solution(begin, target, words):
    
    if target not in words: return 0;
    
    q = deque()
    q.append([begin, 0])
    visited = [0] * len(words)
    
    while q:
        prev, cnt = q.popleft()
        
        if prev == target:
            return cnt
        
        for idx, word in enumerate(words):
            check = 0
            for a, b in zip(prev, word):
                if a != b: 
                    check += 1
            if check == 1:
                visited[idx] = 1
                q.append([word, cnt + 1])


```
output : 4
begin = "hit"	
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
```