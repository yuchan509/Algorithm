n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

ans = 0
for i, j in enumerate(t):
    ans = max(i + j + 2, ans)

print(ans)

'''
out : 7
4
2 3 4 3	
'''