n = int(input())
cipher = input()

ans = ""
for i in range(0, n, 2):
    ans += chr(ord("a") + ((ord(cipher[i]) + int(cipher[i + 1]) ** 2) - ord("a")) % 26)

print(ans)


# Run.
'''
output : bflu
8
a1b2c3e4
'''