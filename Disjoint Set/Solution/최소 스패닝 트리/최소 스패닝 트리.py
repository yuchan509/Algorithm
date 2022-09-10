import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
            
ans = 0
p = [i for i in range(n + 1)]
edge = []

for _ in range(m):
    a, b, w = map(int, input().split())
    edge.append((w, a, b))

edge.sort(key = lambda x : x[0])

for w, a, b in edge:
    if find(p, a) != find(p, b):
        union(p, a, b)
        ans += w
    
print(ans)


# Run.
'''
output : 3
3 3
1 2 1
2 3 2
1 3 3
'''