def calculator(p: list, m: list) -> int:
    fatigue = sum([v1 * v2 for v1, v2 in zip(p, m)])
    return fatigue


def solution(picks, minerals):
    t = 5
    m = minerals[:sum(picks) * t]
    v = {"diamond": [1, 1, 1],
         "iron": [5, 1, 1],
         "stone": [25, 5, 1]}

    fatigues = []
    for i in range(0, len(m), t):
        count = {p: 0 for p in v}

        for mineral in minerals[i:i + t]:
            count[mineral] += 1

        info = list(count.values())
        fatigues.append((calculator(v['stone'], info), info))

    fatigues.sort(key=lambda x: -x[0])

    p = sum([[v] * p for v, p in zip(v, picks)], [])

    ans = 0
    for idx, (fatigue, mineral) in enumerate(fatigues):
        ans += calculator(v[p[idx]], mineral)

    return ans


# Run.
'''
output : 12
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]	
'''