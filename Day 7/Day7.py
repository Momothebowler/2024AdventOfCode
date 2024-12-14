import copy

test_value = []
factors = []
lines = []
good = []
for line in open("day7.txt", "r"):
    test = line.strip("\n").split(": ")
    lines.append(test)
data = []
for test_v in lines:
    test_value.append(test_v[0])
    factors.append(test_v[1].split(" "))


def add(num1, num2):
    return int(num1) + int(num2)


def mult(num1, num2):
    return int(num1) * int(num2)


def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))


def cat(num1, num2):
    return int(f"{num1}{num2}")


def solve(nums, ops):
    if len(nums) == 2:
        return nums[0] == nums[1]

    total, a, b, *rest = nums
    for op in ops:
        if solve([total, op(a, b)] + rest, ops):
            return total
    return 0


# data = [list(map(int, line.replace(":", "").split())) for line in open("day7.txt")]
# print(
#    *[sum(solve(nums, ops) for nums in data) for ops in [[add, mult], [add, mult, cat]]]
# )


def old2():
    for f in range(len(factors)):
        print("hi")
        print(good)
        f2 = copy.deepcopy(factors[f])
        sum2 = 0
        ops1 = []
        ops2 = []
        for i in range(len(factors[f]) + 1):
            ops1.append(list(bin(i).replace("0b", "")))
        for j in ops1:
            for k in j:
                ops2.append(k)

        for i in range(3 ** (len(factors[f]) - 1)):
            binary = ternary(i)
            if len(binary) < len(factors[f]) - 1:
                for j in range(abs(len(binary) - len(factors[f]) + 1)):
                    binary = "0" + binary
            ops1.append(list(binary))
        for j in ops1:
            for k in j:
                ops2.append(k)

        while len(ops2) > 0 and sum2 != test_value[f]:
            if len(f2) == 1:
                sum2 = 0
                f2 = copy.deepcopy(factors[f])
            op = int(ops2.pop(0))

            if op == 1:
                num1 = f2.pop(0)
                num2 = f2.pop(0)
                f2.insert(0, add(num1, num2))
            elif op == 0:
                num1 = f2.pop(0)
                num2 = f2.pop(0)
                f2.insert(0, mult(num1, num2))
            elif op == 2:
                num1 = f2.pop(0)
                num2 = f2.pop(0)
                f2.insert(0, cat(num1, num2))
            if int(f2[0]) == int(test_value[f]) and len(f2) == 1:
                # print("h")
                good.append(f2[0])
                break
    print(good)


old2()
