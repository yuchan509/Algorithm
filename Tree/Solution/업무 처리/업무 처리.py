import sys
from collections import deque
input = sys.stdin.readline

h, k, r = map(int, input().split())
tree = [None] * (2 ** (h + 1))
ans = 0


class Worker:
    def __init__(self, depth):
        self.leaf = deque()
        self.left = deque()
        self.right = deque()
        self.depth = depth


def init(n: int, depth: int) -> None:
    if depth > h: return

    tree[n] = Worker(depth)
    init(n * 2, depth + 1)
    init(n * 2 + 1, depth + 1)


def LeafToRoot(n: int, w: int) -> None:
    global ans

    if n == 1:
        ans += w
        return

    i = n // 2
    if not n % 2:
        tree[i].left.append(w)
    else:
        tree[i].right.append(w)


def Process(n: int, r: int, depth: int) -> None:
    if depth > h: return

    worker = tree[n]

    if depth == h and worker.leaf:
        w = worker.leaf.popleft()
        LeafToRoot(n, w)

    if depth < h:
        if worker.left and r % 2:
            w = worker.left.popleft()
            LeafToRoot(n, w)

        elif worker.right and not r % 2:
            w = worker.right.popleft()
            LeafToRoot(n, w)

    Process(n * 2, r, depth + 1)
    Process(n * 2 + 1, r, depth + 1)


init(1, 0)
for n in range(2 ** h, 2 ** (h + 1)):
    work = map(int, input().split())
    for w in work:
        tree[n].leaf.append(w)

for day in range(1, r + 1):
    Process(1, day, 0)

print(ans)


# Run.
'''
output : 5

1 3 2
9 3 7
5 11 2
'''