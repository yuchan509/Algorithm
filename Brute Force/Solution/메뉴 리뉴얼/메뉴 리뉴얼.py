from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    
    ans = []
    for c in course :
        menu = defaultdict(int)
        
        for order in orders:
            for case in combinations(order, c):
                substr = ''.join(sorted(case))
                menu[substr] += 1
        
        result = [k for k in menu if menu[k] == max(menu.values()) and menu[k] > 1]
        ans.extend(result)
        
    ans.sort()
    return ans


'''
output : ["AC", "ACDE", "BCFG", "CDE"]
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
'''