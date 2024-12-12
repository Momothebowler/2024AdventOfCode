import math

s = 4048
n_digits = math.floor(math.log10(s)) + 1
print(s // 10 ** (n_digits // 2))
print(s - s // 10 ** (n_digits // 2) * 10 ** (n_digits // 2))
