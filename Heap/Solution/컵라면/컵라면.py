import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
  deadline, num = map(int, input().split())
  heapq.heappush(heap, (deadline, num))

ans = []
while heap:
  d, n = heapq.heappop(heap)
  heapq.heappush(ans, n)
  if d < len(ans):
    heapq.heappop(ans)

print(sum(ans))

    
```
output : 15
7
1 6
1 7
3 2
3 1
2 4
2 5
6 1
```