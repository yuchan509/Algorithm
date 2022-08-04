string = input()
n = [sum(list(map(int, s.split("+")))) for s in string.split("-")]
print(n[0] - sum(n[1:]))


# Run.
'''
output : -35
55-50+40	
'''