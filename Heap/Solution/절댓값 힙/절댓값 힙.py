import sys
import heapq

n = int(input())

pq = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(pq, (abs(x), x))
    else:
        if pq:
            print(heapq.heappop(pq)[-1])
        else:
            print(0)

    
'''
output :
-1
1
0
-1
-1
1
1
-2
2

18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
'''