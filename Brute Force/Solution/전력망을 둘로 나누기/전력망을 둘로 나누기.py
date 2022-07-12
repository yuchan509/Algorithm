from collections import deque, defaultdict

def solution(n, wires):

  ans = n
  for case in wires:
    start, end = case

    d = defaultdict(list)
    for a, b in wires:
        d[a].append(b)
        d[b].append(a)

    d[start].remove(end)
    d[end].remove(start)

    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1

    while q:
      x = q.popleft()

      for i in d[x]:
        if not visited[i]:
          visited[i] = 1
          q.append(i)

    ans = min(ans, abs(n - 2 * visited.count(1)))

  return ans

    
```
output : 3
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
```