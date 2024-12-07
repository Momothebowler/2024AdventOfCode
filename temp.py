arr = [11, 6, 16, 20]
ops1 = []
ops2 = []


def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))


for i in range(3 ** (len(arr) - 1)):
    binary = ternary(i)
    if len(binary) < len(arr) - 1:
        for j in range(abs(len(binary) - len(arr) + 1)):
            binary = "0" + binary
    ops1.append(list(binary))
print(ops1)
for j in ops1:

    for k in j:
        ops2.append(k)
