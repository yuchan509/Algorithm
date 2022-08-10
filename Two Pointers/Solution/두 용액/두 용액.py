import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

v = sys.maxsize
ans = [0, n - 1]
start, end = 0, n - 1

while start < end:
  s = arr[start] + arr[end]
  
  if abs(s) < v:
    v = abs(s)
    ans[0] = arr[start]
    ans[-1]= arr[end]

  if s < 0: start += 1
  elif s > 0: end -= 1
  else: break

for i in ans:
    print(i, end = ' ')


# Run.
'''
output : -99 98
5
-2 4 -99 -1 98
'''