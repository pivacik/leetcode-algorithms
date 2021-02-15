import sys


def calculate_plan(a, b, c, d):
    if d > b:
        return a + c * (d - b)
    else:
        return a


string = ''
for line in sys.stdin:
    string += line

lst = list(string.split())


a, b, c, d = lst
print(a, b, c, d)
print(calculate_plan(a, b, c, d))
