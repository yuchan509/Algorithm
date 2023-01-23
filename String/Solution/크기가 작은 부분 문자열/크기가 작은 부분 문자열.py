def solution(t, p):

    ans = 0
    for i in range(len(t) - len(p) + 1):
        substr = t[i:i + len(p)]

        if substr <= p:
            ans += 1

    return ans

# Run.
'''
output : 8
t = "500220839878"
p = "7"
'''