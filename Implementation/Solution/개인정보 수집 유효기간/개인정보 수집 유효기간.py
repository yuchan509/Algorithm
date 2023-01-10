def solution(today, terms, privacies):
    
    ans   = []
    kinds = {k : int(month) for k, month in map(lambda x : x.split(), terms)}
    
    today = today.replace('.', '')
    convert = lambda x : str(x).zfill(2)
    
    for index, info in enumerate(privacies):
        date, k = info.split()
        year, month, day = map(int, date.split('.'))
        
        # calculate day.
        day -= 1
        if not day: 
            day = 28
            month -= 1
        
        # calculate month, year.
        month += kinds[k]
        if not month % 12: 
            year += (month // 12) - 1
            month = 12
        else:
            year += month // 12
            month %= 12
        
        new = ''
        for v in [year, month, day]:
            new += convert(v)
        
        if new < today:
            ans.append(index + 1)
            
    return ans

'''
output : [1, 3]
today = "2022.05.19"	
terms = ["A 6", "B 12", "C 3"]	
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	
'''
