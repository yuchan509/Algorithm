from collections import Counter

def solution(weights):

    ans = 0
    count = Counter(weights)

    meter = [2, 3, 4]
    ratio = {a / b for a in meter for b in meter if a != b}

    for w in count:
        pairs = set(map(lambda x: x * w, ratio)) & set(count)
        p_sum = sum(map(lambda p : count[p] ,pairs))

        ans += count[w] * ((count[w] - 1) + p_sum) / 2

    return ans

'''
output : 4
weights = [100,180,360,100,270]
'''
