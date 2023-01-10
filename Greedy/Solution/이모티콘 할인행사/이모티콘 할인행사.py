from itertools import product

def solution(users, emoticons):
    
    ans = []
    for case in product(range(10, 41, 10), repeat = len(emoticons)):

        plus, amount = 0, 0
        for user in users:
            ur, up = user
            
            cumsum = 0
            for rate, price in zip(case, emoticons):
                if rate >= ur:
                    cumsum += price * (1 - rate / 100) 
                
                if cumsum >= up: 
                    plus += 1
                    break
            else:
                amount += cumsum
        ans.append([plus, amount])

    ans.sort(key = lambda x: (-x[0], -x[1]))    

    return ans[0]


# Run.
'''
output : [4, 13860]
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
'''