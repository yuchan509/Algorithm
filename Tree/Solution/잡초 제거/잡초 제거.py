import sys
input = sys.stdin.readline

# init 함수 >> 구간 트리(Segment Tree) 생성.
def init(node, start, end):
    if start == end:  # >> leaf node
        tree[node] = yard[start]
        return tree[node]

    '''
    specific node = left + right 

    left subtree   >> [start, mid]
    right substree >> (mid, end]
    '''

    mid = (start + end) // 2
    left = node * 2
    right = (node * 2) + 1
    tree[node] = init(left, start, mid) + init(right, mid + 1, end)

    return tree[node]


def subSum(node, start, end, left, right):
    '''
    need range >> [left, right]
    '''
    # 범위 밖 존재.
    if left > end or right < start:
        return 0

    # 범위 내 모두 포함.
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

n, q = map(int, input().split())
yard = list(map(int, input().split()))
tree = [0] * (n * 4)

init(1, 0, n - 1)
for _ in range(q):
    q, index, b = map(int, input().split())
    index -= 1

    if q == 1:
        print(subSum(1, 0, n - 1, index, b - 1))
    elif q == 2:
        update(1, 0, n - 1, index, b)
    else:
        update(1, 0, n - 1, index, -b)


# Run.
'''
output : 
5
12

3 3
1 2 3
1 2 3
2 2 7
1 2 3
'''