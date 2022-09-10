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

t = int(input())

for _ in range(t):
    
    n, m = map(int, input().split())
    ans = 0
    p = [i for i in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        if find(p, a) != find(p, b):
            union(p, a, b)
            ans += 1
    
    print(ans)

# Run.
'''
output : 
2
4

2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5
'''