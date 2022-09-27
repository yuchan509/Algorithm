def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n)]

flag = False
for idx in range(m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        flag = True
        print(idx + 1)
        break
    else:
        union(a, b)

if not flag:
    print(0)


# Run.
'''
output : 0
6 5
0 1
1 2
2 3
5 4
0 4
'''