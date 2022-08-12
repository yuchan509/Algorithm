import sys

def solution(routes):
    
    ans, cam = 0, -sys.maxsize
    routes.sort(key = lambda x : x[-1])
    
    for start, end in routes:
        if cam < start:
            ans += 1
            cam = end

    return ans


# Run.
'''
output : 2
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	
'''