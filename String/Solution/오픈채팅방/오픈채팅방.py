def solution(record):
    
    ans = []
    update = {r.split()[1] : r.split()[-1] for r in record 
             if r.split()[0] in ["Enter", "Change"]}     

    for r in record:
        r = r.split()
        if r[0] == "Enter":
            ans.append(f"{update[r[1]]}님이 들어왔습니다.")

        if r[0] == "Leave":
            ans.append(f"{update[r[1]]}님이 나갔습니다.")
            
    return ans

# Run.
'''
output : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
'''