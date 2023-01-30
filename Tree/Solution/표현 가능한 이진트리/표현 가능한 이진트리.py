def search(bit: str) -> None:

    global check
    if len(bit) == 1 or not check: return

    node = len(bit) // 2
    l, r = bit[:node], bit[node + 1:]
    left = l[len(l) // 2]
    right = r[len(r) // 2]

    if bit[node] == '0' and '1' in [left, right]:
        check = False
        return

    search(l)
    search(r)


def solution(numbers):
    ans = []
    for num in numbers:

        bit = bin(num)[2:]

        global check
        check = True
        for n in range(51):
            seq = (2 ** n - 1)

            if len(bit) <= seq:
                bit = '0' * (seq - len(bit)) + bit
                search(bit)
                ans.append(1 if check else 0)
                break

    return ans

# Run.
'''
output : [1, 1, 0]
numbers = [7, 42, 5]
'''