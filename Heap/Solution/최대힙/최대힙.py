import sys
import heapq

input = sys.stdin.readline 
n = int(input())

ans = []
arr = []
for _ in range(n):
    x = int(input())
    heapq.heappush(arr, -x)
    
    if x == 0 or len(arr) == 0:
        p = heapq.heappop(arr)
        print(-p)


```
output : 0 2 1 3 2 1 0 0 (vertical)
13
0
1
2
0
0
3
2
1
0
0
0
0
0
```