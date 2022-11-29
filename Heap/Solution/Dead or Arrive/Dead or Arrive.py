import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
cars = defaultdict(list)

for i in range(n):
	v, w = map(int, input().split())
	heapq.heappush(cars[v], (-w, i + 1))

ans = 0
for v in cars:
	cars[v].sort(key = lambda x : (x[0], -x[1]))
	ans += heapq.heappop(cars[v])[-1]
	
print(ans)


    
'''
output : 8
5
1 50
5 10
3 20
3 15
3 25
'''