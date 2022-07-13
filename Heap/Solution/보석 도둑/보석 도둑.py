import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())

bag = []
heap = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(heap, (m, v))

for _ in range(k):
    m = int(input())
    heapq.heappush(bag, m)

ans = 0
temp = []
while bag:
    c = heapq.heappop(bag)

    while heap:
        m, v = heapq.heappop(heap)
        if m <= c:
            heapq.heappush(temp, (-v))
        
        else:
            heapq.heappush(heap, (m, v))
            break
    
    if temp:
        ans -= heapq.heappop(temp)


print(ans)

```
output : 164
3 2
1 65
5 23
2 99
10
2
```