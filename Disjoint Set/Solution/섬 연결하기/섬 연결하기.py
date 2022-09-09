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

def solution(n, costs):

    ans = 0
    parent = [i for i in range(n)]

    costs.sort(key = lambda x : x[-1])

    for e in costs:
        a, b, w = e

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            ans += w
    return ans


# Run.
'''
output : 4
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
'''