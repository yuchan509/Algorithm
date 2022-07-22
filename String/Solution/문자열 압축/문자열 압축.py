def solution(s):
    
    res = len(s)
    for size in range(1, len(s) // 2 + 1) :

            compressed = [s[i : i + size] for i in range(0, len(s), size)]

            ans = ""
            idx, num = 0, 1
            while idx != len(compressed) - 1:

                if compressed[idx] == compressed[idx + 1]:
                    idx += 1
                    num += 1

                else:
                    ans += str(num) +  compressed[idx] if num != 1 else '' + compressed[idx]
                    idx += 1
                    num = 1

            ans += str(num) +  compressed[idx] if num != 1 else '' + compressed[idx]
            res = min(res, len(ans))
        
    return res


# Run.
'''
output : 14
s = "abcabcabcabcdededededede"	
'''