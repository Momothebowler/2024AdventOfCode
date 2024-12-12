import functools
import math
from collections import defaultdict

text_alt = ""
# text_alt = "125 17"

stone_list = [int(element) for element in text_alt.split()]
stone_set = set(stone_list)
stones = {stone: stone_list.count(stone) for stone in stone_set}
# print(stones)

after_stones = []
blinks = 75


def part1():
    for i in range(1, blinks + 1):
        while len(text_alt) > 0:
            stone = text_alt.pop(0)
            if stone == "0":
                after_stones.append("1")
            elif len(stone) % 2 == 0:
                first = stone[: len(stone) // 2]
                second = stone[len(stone) // 2 :]
                after_stones.append(str(int(first)))
                after_stones.append(str(int(second)))
            else:
                after_stones.append(str(int(stone) * 2024))
        text_alt = after_stones
        # print(f"After {i} blink: \n{len(after_stones)}")
        after_stones = []


count = len(text_alt)


# @functools.cache
def next_stone(stone, iter=0):
    global count
    if iter == 75:
        return 0

    if stone != 0:
        n_digits = math.floor(math.log10(stone)) + 1
    if stone == 0:
        # if iter == 5:
        # print("1", end=" ")
        next_stone(1, iter + 1)

    elif n_digits % 2 == 0:
        # if iter == 5:
        # print(str(int(stone[: len(stone) // 2])), end=" ")
        # print(str(int(stone[len(stone) // 2 :])), end=" ")
        next_stone(stone // 10 ** (n_digits // 2), iter + 1)
        next_stone(
            stone - stone // 10 ** (n_digits // 2) * 10 ** (n_digits // 2), iter + 1
        )
        count += 1
    else:
        # if iter == 5:
        # print(str(int(stone) * 2024), end=" ")
        next_stone(stone * 2024, iter + 1)


def blink():
    global stones
    new_stones = defaultdict(int)
    for stone in stones:
        number_stones = stones[stone]
        if stone == 0:
            new_stones[1] += number_stones
        elif len(str(stone)) % 2 == 0:
            str_rep = str(stone)
            stone_1 = int(str_rep[: len(str_rep) // 2])
            stone_2 = int(str_rep[len(str_rep) // 2 :])
            new_stones[stone_1] += number_stones
            new_stones[stone_2] += number_stones
        else:
            new_stones[2024 * stone] += number_stones
    stones = new_stones

    return stones


for i in range(1075):
    # print(stoni)
    stoni = blink()

print(sum(stoni.values()))
