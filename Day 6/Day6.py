import copy

lines = []
player = ()
board_size = [0, 0]


def direction_change(dir2):
    if dir2 == "North":
        dir2 = "East"
    elif dir2 == "South":
        dir2 = "West"
    elif dir2 == "East":
        dir2 = "South"
    elif dir2 == "West":
        dir2 = "North"
    return dir2


def part1(dir, player2, board_size, lines):
    dir = "North"
    safe = []
    player = copy.deepcopy(player2)
    while (player[0] >= 0 and player[0] < board_size[0]) and (
        player[1] >= 0 and player[1] <= board_size[1]
    ):
        try:
            if dir == "North" and lines[player[0] - 1][player[1]] != "#":
                player[0] -= 1
                # lines[player[0]][player[1]] = "^"
                # lines[player[0] + 1][player[1]] = "X"
            elif dir == "South" and lines[player[0] + 1][player[1]] != "#":
                player[0] += 1
                # lines[player[0]][player[1]] = "^"
                # lines[player[0] - 1][player[1]] = "X"
            elif dir == "East" and lines[player[0]][player[1] + 1] != "#":
                player[1] += 1
                # lines[player[0]][player[1]] = "^"
                # lines[player[0]][player[1] - 1] = "X"
            elif dir == "West" and lines[player[0]][player[1] - 1] != "#":
                player[1] -= 1
                # lines[player[0]][player[1]] = "^"
                # lines[player[0]][player[1] + 1] = "X"
            else:
                dir = direction_change(dir)
        except:
            # lines[player[0]][player[1]] = "X"
            if dir == "North":
                player[0] -= 1
            elif dir == "South":
                player[0] += 1
            elif dir == "East":
                player[1] += 1
            elif dir == "West":
                player[1] -= 1
        if player not in safe:
            safe.append(copy.deepcopy(player))
    return safe


def part2(player, board_size, lines2):
    dir = "North"
    safe = part1(dir, player, board_size, lines2)
    # print(safe)
    block = 0
    counting = 0
    start = copy.deepcopy(player)
    # print(len(safe))
    for safe_place in safe:
        counting += 1
        j = safe_place[1]
        i = safe_place[0]
        dir = "North"
        player = copy.deepcopy(start)
        lines = copy.deepcopy(lines2)
        locations = []
        # print(lines[i][j])
        if i < board_size[0] and j <= board_size[1] and lines[i][j] == ".":
            print("i: " + str(i) + " j: " + str(j) + " iter: " + str(counting))
            lines[i][j] = "#"
            while (
                player[0] >= 0
                and player[0] <= board_size[0]
                and player[1] >= 0
                and player[1] <= board_size[1]
            ):
                # if i == 6 and j == 3:
                # for l in lines:
                #    print("".join(l), end="")
                # print("\n-------------------")

                if (player, dir) in locations:
                    print("i:" + str(i) + " j:" + str(j) + " Looping")
                    block += 1
                    break
                try:
                    if dir == "North" and lines[player[0] - 1][player[1]] != "#":
                        locations.append((copy.copy(player), "North"))
                        player[0] -= 1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0] + 1][player[1]] == "^":
                            lines[player[0] + 1][player[1]] = "."

                    elif dir == "South" and lines[player[0] + 1][player[1]] != "#":
                        locations.append((copy.copy(player), "South"))
                        player[0] += 1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0] - 1][player[1]] == "^":
                            lines[player[0] - 1][player[1]] = "."

                    elif dir == "East" and lines[player[0]][player[1] + 1] != "#":
                        locations.append((copy.copy(player), "East"))
                        player[1] += 1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0]][player[1] - 1] == "^":
                            lines[player[0]][player[1] - 1] = "."

                    elif dir == "West" and lines[player[0]][player[1] - 1] != "#":
                        locations.append((copy.copy(player), "West"))
                        player[1] -= 1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0]][player[1] + 1] == "^":
                            lines[player[0]][player[1] + 1] = "."
                    else:
                        dir = direction_change(dir)
                except:
                    if dir == "North":
                        player[0] -= 1
                    elif dir == "South":
                        player[0] += 1
                    elif dir == "East":
                        player[1] += 1
                    elif dir == "West":
                        player[1] -= 1
    print(block)


with open(r"day6.txt", "r") as fp:
    for count, line in enumerate(fp):
        board_size[1] += 1
        board_size[0] = len(line)
        lines.append(list(line))
        for k in range(len(line)):
            if line[k] == "^":
                player = [count, k]


part2(player, board_size, lines)

total = 0
for l in lines:
    total += l.count("O")
    # print("".join(l),end="")
# print()
# print(total)
