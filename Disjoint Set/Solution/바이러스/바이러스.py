import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
v = int(input())
parent = [i for i in range(n + 1)]

for _ in range(v):
    a, b = map(int, input().split())
    union(parent, a, b)

ans = -1
for i in range(1, n+1):
    if find(parent, i) == 1:
        ans += 1

print(ans)


# Run.
'''
output : 4
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''