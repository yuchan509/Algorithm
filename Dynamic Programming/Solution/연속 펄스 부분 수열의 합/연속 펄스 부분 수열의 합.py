def solution(sequence):

    n = len(sequence)
    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = -sequence[0]
    dp2[0] = sequence[0]

    for i in range(1, n):
        if i & 1:
            dp1[i] = max(sequence[i], dp1[i - 1] + sequence[i])
            dp2[i] = max(-sequence[i], dp2[i - 1] - sequence[i])
        else:
            dp1[i] = max(-sequence[i], dp1[i - 1] - sequence[i])
            dp2[i] = max(sequence[i], dp2[i - 1] + sequence[i])

    ans = max(max(dp1), max(dp2))
    return ans

# run.
'''
output : 10
sequence = [2, 3, -6, 1, 3, -1, 2, 4]
'''
