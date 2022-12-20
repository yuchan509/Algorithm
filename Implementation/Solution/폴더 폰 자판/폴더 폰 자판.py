import sys
sys.stdin.readline

n = int(input())
s = list(map(int, input()))

phone = ['1.,?!', '2ABC', '3DEF',
        '4GHI', '5JKL', '6MNO',
        '7PQRS', '8TUV', '9WXYZ']

ans = ''
cnt = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        cnt += 1
    
    else:
        p = phone[s[i] - 1]
        ans += p[cnt % len(p)]
        cnt = 0
    
p = phone[s[-1] - 1]
ans += p[cnt % len(p)]

print(ans)


'''
output : .
2
11
'''
