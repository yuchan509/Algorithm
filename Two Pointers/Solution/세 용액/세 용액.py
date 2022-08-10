import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

v = sys.maxsize
ans = [0] * 3

for idx in range(n - 2):
    start, end = idx + 1, n - 1
    
    while start < end:
        s = arr[start] + arr[end] + arr[idx]
        if abs(s) < v:
            v = abs(s)
            ans[0] = arr[idx]
            ans[1] = arr[start]
            ans[-1]= arr[end]

        if s < 0: start += 1
        elif s > 0: end -= 1
        else: break

for i in ans:
    print(i, end = ' ')


# Run.
'''
output : -97 -2 98
5
-2 6 -97 -6 98
'''