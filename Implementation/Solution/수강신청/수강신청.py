import sys

k, l = map(int, input().split())
d = {}

for idx, _ in enumerate(range(l)):
    v = sys.stdin.readline().strip()
    d[v] = idx

ans = sorted(d.items(), key = lambda x : x[-1])[:k]
for a, b in ans:
    print(a)

```
output : 
20103324
20133221
20140101

3 8
20103324
20133221
20133221
20093778
20140101
01234567
20093778
20103325
```