import re


def mul(x, y):
    return x * y


sum = 0
text = ""
for line in open("day3.txt"):
    text += line + "\\n"
# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


# call_funcs = re.findall("(mul\(\d+,\d+\))", text)
call_funcs = re.findall("don't\(\)|mul\(\d+,\d+\)|do\(\)", text)
# no_call_funcs = re.findall("(do\(\))", text)
lock = False
for call in call_funcs:
    if call == "don't()":
        lock = True

    if call == "do()":
        lock = False

    if not lock and call != "do()":
        nums = re.findall("[0-9]+", str(call))
        sum += mul(int(nums[0]), int(nums[1]))

print(sum)
