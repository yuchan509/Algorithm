import re

def solution(s, skip, index):
    ans = ''
    order = re.sub(f'[{skip}]', '', 'abcdefghijklmnopqrstuvwxyz')

    for sub in s:
        idx = order.index(sub) + index
        ans += order[idx % len(order)]

    return ans


# Run.
'''
output : "happy"
s = "aukks"	
skip = "wbqd"
index = 5
'''