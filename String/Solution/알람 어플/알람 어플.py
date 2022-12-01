s = input()
k = int(input())

substring = set()
for i in range(len(s)):
    substr = ""

    for j in range(i, i + k):
        if (j >= len(s)):
            break
        substr += s[j]
        substring.add(substr)

ans = sorted(substring)[k - 1]
print(ans)

# Run.
'''
output : b
aba
4
'''