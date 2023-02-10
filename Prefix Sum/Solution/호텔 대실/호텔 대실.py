def convert(time: str) -> int:
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def solution(book_time):
    imos = [0] * (60 * 24 + 10)
    for time in book_time:
        s, e = map(lambda x: convert(x), time)
        imos[s] += 1
        imos[e + 10] -= 1

    for i in range(1, len(imos)):
        imos[i] += imos[i - 1]

    ans = max(imos)

    return ans

# run.
'''
output : 3
book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	
'''
