import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    tree = {i : 0 for i in range(1, n + 1)}
    for _ in range(n - 1):
        parent, child = map(int, input().split())
        tree[child] = parent

    a, b = map(int, input().split())
    ap = [a]
    
    while tree[a]:
        ap.append(tree[a])
        a = tree[a]

    while True:
        if b in ap:
            print(b)
            break
        b = tree[b]


# Run.
'''
output : 
4
3

2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5
'''