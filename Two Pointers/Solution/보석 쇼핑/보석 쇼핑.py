from collections import defaultdict

def solution(gems):

    ans = [1, len(gems)]
    n = len(set(gems))
    left, right = 0, 0

    contain = defaultdict(int)
    contain[gems[right]] += 1

    while left <= right < len(gems):
        if len(contain) < n:
            right += 1

            if right >= len(gems):
                break
            contain[gems[right]] += 1

        else:
            if right - left < ans[-1] - ans[0]:
                ans = [left + 1, right + 1]

            contain[gems[left]] -= 1
            if not contain[gems[left]]:
                contain.pop(gems[left])
            left += 1

    return ans


# Run.
'''
output : [3, 7]
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
'''