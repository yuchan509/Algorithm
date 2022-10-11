import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

d = Counter(cards)
for num in nums:
    print(d[num], end = " ")

    
'''
output : 3 0 0 1 2 0 0 2
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''