from itertools import product

def solution(queries): 
    
    ans = []
    for q in queries:
        n, p = q
        
        init = 'Rr'
        
        if n == 1:
            ans.append(init)
            
        else:
            for i in range(n - 2, -1, -1):
                
                if i > 0:
                    generation = [''.join(sorted(i)) for i in product(init, repeat = 2)]
                    idx, p = divmod(p, (4 ** i))
                    init = generation[idx]
            
            res = [''.join(sorted(i)) for i in product(init, repeat = 2)][p - 1]
            ans.append(res)

    return ans

    
'''
output : ["RR"]
queries = [[3, 5]]	
'''