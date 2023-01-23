import sys

string = input()

length = len(string)
a = string.count('a')

ans = sys.maxsize
for i in range(length):
    if a + i > length:
        window = string[i:length] + string[:(a + i) % length]
    else:
        window = string[i:a + i]

    b = window.count('b')
    ans = min(ans, b)

print(ans)


# Run.
'''
output : 3
abababababababa
'''