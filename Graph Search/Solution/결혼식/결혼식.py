from collections import deque, defaultdict

n = int(input())
m = int(input())

d = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

def bfs():

    v = set([1])
    q = deque()
    q.append([1, 0])

    while q:
        x, cnt = q.popleft()

        for next_node in d[x]:
            if next_node not in v and cnt < 2:
                v.add(next_node)
                q.append([next_node, cnt + 1])

    return len(v) - 1

print(bfs())

```
output : 3
6
5
1 2
1 3
3 4
2 3
4 5
```