import itertools
import sys
g = list(map(int,input().split()))
DICE_COUNT = g[0]
FACE_COUNT = g[1]
TOP_DICE_COUNT = g[2]
TOP_DICE_SUM = g[3]
factorial = [1] * (DICE_COUNT + 1)

def init_factorial():
    for i in range(1, DICE_COUNT + 1):
        factorial[i] = factorial[i - 1] * i

def get_combination_count(combination):
    freqs = [0] * FACE_COUNT
    for i in combination:
        freqs[i - 1] += 1
    n, d = factorial[DICE_COUNT], 1
    for i in freqs:
        d *= factorial[i]
    return int(n/d)
init_factorial()
ways = 0
for i in itertools.combinations_with_replacement(range(1, FACE_COUNT + 1), DICE_COUNT):
    if sum(i[DICE_COUNT - TOP_DICE_COUNT::]) == TOP_DICE_SUM:
        ways += get_combination_count(i)
print(ways)

