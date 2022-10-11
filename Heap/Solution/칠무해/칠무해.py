import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, float(input()))

for _ in range(7):
    x = heapq.heappop(heap)
    print(f'{x:.3f}')
    
'''
output : 
20.000
30.000
30.000
50.000
60.000
70.000
70.000

8
20.000
70.000
50.000
30.000
70.000
30.000
60.000
70.000
'''