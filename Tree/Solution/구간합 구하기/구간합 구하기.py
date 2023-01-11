import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = maps[start]
        return tree[node]

    mid = (start + end) // 2
    left = node * 2
    right = (node * 2) + 1
    tree[node] = init(left, start, mid) + init(right, mid + 1, end)

    return tree[node]

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l = subSum(node * 2, start, mid, left, right)
    r = subSum((node * 2) + 1, mid + 1, end, left, right)
    cumsum = l + r

    return cumsum

def update(node, start, end, index, diff):
    if index < start or index > end: return

    tree[node] += diff
    mid = (start + end) // 2

    if start != end:
        update(node * 2, start, mid, index, diff)
        update((node * 2) + 1, mid + 1, end, index, diff)


n, m, k = map(int, input().split())
maps = [int(input()) for _ in range(n)]
tree = [0] * (n * 4)

init(1, 0, n - 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - maps[b - 1]
        maps[b - 1] = c
        update(1, 0, n - 1, b - 1, diff)
    else:
        print(subSum(1, 0, n - 1, b - 1, c - 1))


# Run.
'''
output
17
12

5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
'''