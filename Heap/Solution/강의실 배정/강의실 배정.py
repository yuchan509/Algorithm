import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
  start, end = map(int, input().split())
  heapq.heappush(heap, (start, end))

end = []
while heap:
  s, e = heapq.heappop(heap)
  heapq.heappush(end, e)

  if end and end[0] <= s:
    heapq.heappop(end)

print(len(end))

```
output : 2
3
1 3
2 4
3 5
```