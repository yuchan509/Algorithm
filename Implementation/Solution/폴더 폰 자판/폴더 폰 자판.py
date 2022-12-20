import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input()))

phone = ['1.,?!', '2ABC', '3DEF',
        '4GHI', '5JKL', '6MNO',
        '7PQRS', '8TUV', '9WXYZ']

ans = ''
cnt = 0
for i in range(n):	
    if i != (n - 1) and s[i] == s[i + 1]:
        cnt += 1
    
    else:
        p = phone[s[i] - 1]
        ans += p[cnt % len(p)]
        cnt = 0

print(ans)

'''
output : .
2
11
'''
