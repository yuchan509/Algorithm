import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
        
n, m = map(int, input().split())
p = [i for i in range(n + 1)]

for _ in range(m):
    flag, a, b = map(int, input().split())
    
    if flag == 1:
        if find(p, a) == find(p, b):
            print('YES')
        else: 
            print('NO')
    
    else:
        union(p, a, b)


# Run.
'''
output : 
NO
NO
YES

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''