import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
  p, d = map(int, input().split())
  heapq.heappush(heap, (d, p))

ans = []
while heap:
  d, p = heapq.heappop(heap)
  heapq.heappush(ans, p)

  if d < len(ans):
    heapq.heappop(ans)

print(sum(ans))

```
output : 185
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10
```