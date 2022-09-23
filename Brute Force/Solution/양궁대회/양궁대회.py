from itertools import combinations_with_replacement

def solution(n, info):

    MAX = 0
    ans = []

    for case in combinations_with_replacement(range(11), n):

        info2 = [0] * 11
        for idx in case:
            info2[idx] += 1

        apeach, ryan = 0, 0
        for score, res in enumerate(zip(info, info2)):
            a, r = res
            if a == 0 and r == 0:
                continue

            if a >= r:
                apeach += 10 - score
            else:
                ryan += 10 - score

        diff = ryan - apeach
        if diff <= 0:
            continue
        else:
            if MAX <= diff:
                MAX = diff
                ans.append((MAX, info2))

    ans.sort(key = lambda x : (x[0], x[-1][::-1]), reverse = True)


    if not ans:
        return [-1]
    else:
        return ans[0][-1]

    
'''
output : [0,2,2,0,1,0,0,0,0,0,0]
k = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
'''