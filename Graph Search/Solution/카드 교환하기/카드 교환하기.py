import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10 ** 6) # 재귀 깊이 늘리기(재귀를 이용한 dfs 활용시 깊이 늘려주기, default : 1000으로 설정.)
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 양방향 그래프 만들기.
graph = defaultdict(list)
for i in range(1, n + 1):
	graph[i]

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)


# queue를 활용한 bfs.
def bfs(start: int) -> int:
	q = deque()
	q.append(start)
	v.add(start)

	while q:
		x = q.popleft()
		a.append(x)
		b.append(cards[x - 1])

		for node in graph[x]:
			if node not in v:
				v.add(node)
				q.append(node)
	a.sort()
	b.sort()
	res = sum([abs(v1 - v2) for v1, v2 in zip(a, b)])

	return res


# 문제 채점상 >> python으로 재귀 활용시 runtime 발생.
def dfs(x: int) -> int:
	v.add(x)
	a.append(x)
	b.append(cards[x - 1])

	for node in graph[x]:
		if node not in v:
			dfs(node)
	a.sort()
	b.sort()
	res = sum([abs(v1 - v2) for v1, v2 in zip(a, b)])

	return res


# Stack을 활용한 dfs >> python에서 pop() 활영시 deque가 list보다 성능이 일반적으로 뛰어나므로 대신하여 활용.
def dfsStack(start: int) -> int:
	stack = deque()
	stack.append(start)

	while stack:
		x = stack.pop()

		if x not in v:
			v.add(x)
			a.append(x)
			b.append(cards[x - 1])
			stack.extend(graph[x])
	a.sort()
	b.sort()
	res = sum([abs(v1 - v2) for v1, v2 in zip(a, b)])

	return res

ans = 0
v = set()
for node in graph:
	if node not in v:
		a, b = [], []
		ans += bfs(node)

print(ans)

'''
output : 8
6 7
3 4 4 1 5 6
1 3
1 6
3 6
3 5
1 5
5 6
1 2
'''
