import heapq
def solution(jobs):

  heap = []
  for p, t in jobs:
    heapq.heappush(heap, (t, p))

  heap.sort()
  ans, now = 0, 0

  while heap:
    for idx in range(len(heap)):

      time, point = heap[idx]

      if point <= now:
        now += time
        ans += now - point
        heap.pop(idx)
        break

      if idx == len(heap) - 1:
        now += 1

  return ans // len(jobs)


```
output : 9
jobs = [[0, 3], [1, 9], [2, 6]]	
```