from collections import deque

n, k = map(int, input().split())
num = input()

d = 0
stack = deque()
for i in num:

    while stack and stack[-1] < i:
        if d == k:
            break
        else:
            d += 1
            stack.pop()
    stack.append(i)

ans = ''.join(list(stack)[: n - k])
print(ans)


'''
out : 94
4 2
1924
'''