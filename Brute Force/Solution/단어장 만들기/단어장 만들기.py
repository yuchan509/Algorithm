import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]
words.sort(key = lambda x : (len(x), x))

print(words[k - 1])


'''
output : aa
7 3
aaaa
aaa
aa
a
b
bb
bbb
'''