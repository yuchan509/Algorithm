import heapq

n = int(input())

heap = []
for _ in range(n):
  heapq.heappush(heap, int(input()))

ans = 0

while len(heap) > 1:
  c1 = heapq.heappop(heap)
  c2 = heapq.heappop(heap)
  comb = c1 + c2 
  heapq.heappush(heap, comb)
  ans += comb

print(ans)

```
output : 100
3
10
20
40
```