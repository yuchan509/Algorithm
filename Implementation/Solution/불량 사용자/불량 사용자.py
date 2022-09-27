import re
from itertools import permutations

def solution(user_id, banned_id):
    
    box = []
    for case in permutations(user_id, len(banned_id)):

        cnt = 0
        for c, b in zip(case, banned_id):
            chk = re.match(b.replace('*', '.'), c)
            if chk and chk.span()[-1] == len(c):
                cnt += 1

        if cnt == len(case):
            box.append(tuple(sorted(case)))

    ans = len(set(box))
    
    return ans


'''
output : 2
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
'''
