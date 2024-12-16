import copy


def day1():
    depth = 0
    walls = set()
    character = [0, 0]
    boxes = set()
    instructions = []
    for line in open("day15.txt"):
        for chara in range(len(line)):
            if line[chara] == "#":
                walls.add((depth, chara))
            elif line[chara] == "O":
                boxes.add((depth, chara))
            elif line[chara] == "@":
                character = [depth, chara]
            elif (
                line[chara] == "<"
                or line[chara] == ">"
                or line[chara] == "^"
                or line[chara] == "v"
            ):
                instructions.append(line[chara])

        depth += 1
    bounds = [50, 50]

    def print_warehouse(character, boxes, walls, bounds):
        for i in range(bounds[0]):
            for j in range(bounds[1]):
                if (i, j) in walls:
                    print("#", end="")
                elif (i, j) in boxes:
                    print("O", end="")
                elif i == character[0] and j == character[1]:
                    print("@", end="")
                else:
                    print(".", end="")
            print()

    while len(instructions) > 0:
        # print(instructions)

        # print(boxes)
        move_to = instructions.pop(0)

        # print(character)
        # print_warehouse(character, boxes, walls, bounds)
        # print(move_to)
        if move_to == "<":
            if (character[0], character[1] - 1) not in walls:
                boxes_to_move = set()
                for i in range(1, character[1] + 1):
                    look = (character[0], character[1] - i)
                    if look in boxes:
                        boxes_to_move.add(look)
                    elif look not in boxes and look not in walls:
                        break
                    elif (
                        look in walls
                        and (
                            character[0],
                            character[1] - i + 1,
                        )
                        in boxes
                    ):

                        boxes_to_move = set()
                        break
                # print(boxes_to_move)
                for box in boxes_to_move:
                    boxes.remove(box)
                for box in boxes_to_move:
                    boxes.add((box[0], box[1] - 1))
                if (
                    len(boxes_to_move) > 0
                    or (character[0], character[1] - 1) not in boxes
                ):
                    character = [character[0], character[1] - 1]

        elif move_to == ">":
            if (character[0], character[1] + 1) not in walls:
                boxes_to_move = set()
                for i in range(1, bounds[1] - character[1]):
                    look = (character[0], character[1] + i)
                    if look in boxes:
                        boxes_to_move.add(look)
                    elif look not in boxes and look not in walls:
                        break
                    elif (
                        look in walls
                        and (
                            character[0],
                            character[1] + i - 1,
                        )
                        in boxes
                    ):

                        boxes_to_move = set()
                        break
                # print(boxes_to_move)
                for box in boxes_to_move:
                    boxes.remove(box)
                for box in boxes_to_move:
                    boxes.add((box[0], box[1] + 1))
                if (
                    len(boxes_to_move) > 0
                    or (character[0], character[1] + 1) not in boxes
                ):
                    character = [character[0], character[1] + 1]

        elif move_to == "^":
            if (character[0] - 1, character[1]) not in walls:
                boxes_to_move = set()
                for i in range(1, character[0] + 1):
                    look = (character[0] - i, character[1])
                    if look in boxes:
                        boxes_to_move.add(look)
                    elif look not in boxes and look not in walls:
                        break
                    elif (
                        look in walls
                        and (
                            character[0] - i + 1,
                            character[1],
                        )
                        in boxes
                    ):

                        boxes_to_move = set()
                        break
                # print(boxes_to_move)
                for box in boxes_to_move:
                    boxes.remove(box)
                for box in boxes_to_move:
                    boxes.add((box[0] - 1, box[1]))
                if (
                    len(boxes_to_move) > 0
                    or (character[0] - 1, character[1]) not in boxes
                ):
                    character = [character[0] - 1, character[1]]
        else:
            if (character[0] + 1, character[1]) not in walls:
                boxes_to_move = set()
                for i in range(1, bounds[0] - character[0]):
                    look = (character[0] + i, character[1])
                    # print(look)
                    if look in boxes:
                        boxes_to_move.add(look)
                    elif look not in boxes and look not in walls:
                        # print("h")
                        break
                    elif (
                        look in walls
                        and (
                            character[0] + i - 1,
                            character[1],
                        )
                        in boxes
                    ):

                        boxes_to_move = set()
                        break
                # print(boxes_to_move)
                for box in boxes_to_move:
                    boxes.remove(box)
                for box in boxes_to_move:
                    boxes.add((box[0] + 1, box[1]))
                if (
                    len(boxes_to_move) > 0
                    or (character[0] + 1, character[1]) not in boxes
                ):
                    character = [character[0] + 1, character[1]]

        # print("AAAAAAAAAAAAAAAAAAAAAAAAA")
        # print(move_to)

    print_warehouse(character, boxes, walls, bounds)
    score = 0
    for i in boxes:
        score += i[0] * 100 + i[1]
    print(score)


def day2():
    depth = 0
    walls = set()
    character = [0, 0]
    boxes = set()
    instructions = []
    for line in open("day15.txt"):
        for chara in range(len(line)):
            if line[chara] == "#":
                walls.add((depth, chara * 2))
                walls.add((depth, chara * 2 + 1))
            elif line[chara] == "O":
                boxes.add((depth, chara * 2, 1))  # left part
                boxes.add((depth, chara * 2 + 1, 2))  # right part
            elif line[chara] == "@":
                character = [depth, chara * 2]
            elif (
                line[chara] == "<"
                or line[chara] == ">"
                or line[chara] == "^"
                or line[chara] == "v"
            ):
                instructions.append(line[chara])

        depth += 1
    bounds = [10, 10 * 2]

    def print_warehouse(character, boxes, walls, bounds):
        for i in range(bounds[0]):
            for j in range(bounds[1]):
                if (i, j) in walls:
                    print("#", end="")
                elif (i, j, 1) in boxes:
                    print("[", end="")
                elif (i, j, 2) in boxes:
                    print("]", end="")
                elif i == character[0] and j == character[1]:
                    print("@", end="")
                else:
                    print(".", end="")
            print()

    # print_warehouse(character, boxes, walls, bounds)
    while len(instructions) > 0:
        move_to = instructions.pop(0)
        # print_warehouse(character, boxes, walls, bounds)
        # print(move_to)
        if move_to == "<":
            if (character[0], character[1] - 1) not in walls:
                boxes_to_move = []
                look_l = (character[0], character[1] - 1, 2)
                look_r = (character[0], character[1] - 2, 1)

                if look_l in boxes:
                    boxes_to_move.append(look_r)

                # print(boxes_to_move)
                check = copy.deepcopy(boxes_to_move)
                while len(check) > 0:
                    box_check = check.pop(0)
                    if (box_check[0], box_check[1] - 2, 1) in boxes:
                        boxes_to_move.append((box_check[0], box_check[1] - 2, 1))
                        check.append((box_check[0], box_check[1] - 2, 1))

                # print(boxes_to_move)
                for box in boxes_to_move:
                    if (box[0], box[1] - 1) in walls:
                        boxes_to_move = []

                while len(boxes_to_move) > 0:
                    box = boxes_to_move.pop()
                    look_left = (box[0], box[1] - 1)

                    if look_left in walls:
                        boxes_to_move.remove((box[0], box[1] + 1, 2))
                        break
                    elif (box[0], box[1] - 1, 1) not in boxes:
                        boxes.add((box[0], box[1] - 1, 1))
                        boxes.add((box[0], box[1], 2))
                        boxes.remove((box[0], box[1] + 1, 2))
                        boxes.remove((box[0], box[1], 1))

                if (character[0], character[1] - 1) not in walls and (
                    character[0],
                    character[1] - 1,
                    2,
                ) not in boxes:
                    character = [character[0], character[1] - 1]

        elif move_to == ">":
            if (character[0], character[1] + 1) not in walls:
                boxes_to_move = []
                look_l = (character[0], character[1] + 1, 1)
                look_r = (character[0], character[1] + 2, 2)

                if look_l in boxes:
                    boxes_to_move.append(look_r)

                # print(boxes_to_move)
                check = copy.deepcopy(boxes_to_move)
                while len(check) > 0:
                    box_check = check.pop(0)
                    if (box_check[0], box_check[1] + 2, 2) in boxes:
                        boxes_to_move.append((box_check[0], box_check[1] + 2, 2))
                        check.append((box_check[0], box_check[1] + 2, 2))

                # print(boxes_to_move)
                for box in boxes_to_move:
                    if (box[0], box[1] + 1) in walls:
                        boxes_to_move = []

                while len(boxes_to_move) > 0:
                    box = boxes_to_move.pop()
                    look_left = (box[0], box[1] + 1)

                    if look_left in walls:
                        boxes_to_move.remove((box[0], box[1] - 1, 1))
                        break
                    elif (box[0], box[1] + 1, 2) not in boxes:
                        boxes.add((box[0], box[1] + 1, 2))
                        boxes.add((box[0], box[1], 1))
                        boxes.remove((box[0], box[1] - 1, 1))
                        boxes.remove((box[0], box[1], 2))

                if (character[0], character[1] + 1) not in walls and (
                    character[0],
                    character[1] + 1,
                    1,
                ) not in boxes:
                    character = [character[0], character[1] + 1]

        elif move_to == "^":
            if (character[0] - 1, character[1]) not in walls:
                boxes_to_move = []
                look_l = (character[0] - 1, character[1], 1)  # "["
                look2_r = (character[0] - 1, character[1], 2)  # "]"
                # Right above ^; Left or Right of above v
                look_r = (character[0] - 1, character[1] + 1, 2)  # "]"
                look2_l = (character[0] - 1, character[1] - 1, 1)  # "["

                if look_l in boxes:
                    boxes_to_move.append(look_l)
                    boxes_to_move.append(look_r)
                if look2_r in boxes:
                    boxes_to_move.append(look2_r)
                    boxes_to_move.append(look2_l)
                check = copy.deepcopy(boxes_to_move)
                while len(check) > 0:
                    box_check = check.pop(0)
                    if (box_check[0] - 1, box_check[1], 1) in boxes:
                        boxes_to_move.append((box_check[0] - 1, box_check[1], 1))
                        boxes_to_move.append((box_check[0] - 1, box_check[1] + 1, 2))
                        check.append((box_check[0] - 1, box_check[1], 1))
                        check.append((box_check[0] - 1, box_check[1] + 1, 2))
                    elif (box_check[0] - 1, box_check[1], 2) in boxes:
                        boxes_to_move.append((box_check[0] - 1, box_check[1], 2))
                        boxes_to_move.append((box_check[0] - 1, box_check[1] - 1, 1))
                        check.append((box_check[0] - 1, box_check[1], 1))
                        check.append((box_check[0] - 1, box_check[1] - 1, 1))

                for box in boxes_to_move:
                    if (box[0] - 1, box[1]) in walls:
                        boxes_to_move = []

                while len(boxes_to_move) > 0:
                    box = boxes_to_move.pop()
                    if box[2] == 1:
                        look_up = (box[0] - 1, box[1])
                        look_up2 = (box[0] - 1, box[1] + 1)
                    if box[2] == 2:
                        look_up = (box[0] - 1, box[1])
                        look_up2 = (box[0] - 1, box[1] - 1)

                    if look_up in walls or look_up2 in walls:
                        if box[2] == 1:
                            boxes_to_move.remove((box[0], box[1] + 1, 2))
                        if box[2] == 2:
                            boxes_to_move.remove((box[0], box[1] - 1, 1))
                        break
                    elif box[2] == 1 and (box[0] - 1, box[1], 1) not in boxes:
                        boxes.remove(box)
                        boxes.remove((box[0], box[1] + 1, 2))
                        boxes.add((box[0] - 1, box[1], 1))
                        boxes.add((box[0] - 1, box[1] + 1, 2))
                    elif box[2] == 2 and (box[0] - 1, box[1], 2) not in boxes:
                        boxes.remove(box)
                        boxes.remove((box[0], box[1] - 1, 1))
                        boxes.add((box[0] - 1, box[1], 2))
                        boxes.add((box[0] - 1, box[1] - 1, 1))

                if (character[0] - 1, character[1]) not in walls and (
                    (character[0] - 1, character[1], 1) not in boxes
                    and (character[0] - 1, character[1], 2) not in boxes
                ):
                    character = [character[0] - 1, character[1]]

        else:
            if (character[0] + 1, character[1]) not in walls:
                boxes_to_move = []
                look_l = (character[0] + 1, character[1], 1)  # "["
                look2_r = (character[0] + 1, character[1], 2)  # "]"
                # Right above ^; Left or Right of above v
                look_r = (character[0] + 1, character[1] + 1, 2)  # "]"
                look2_l = (character[0] + 1, character[1] - 1, 1)  # "["

                if look_l in boxes:
                    boxes_to_move.append(look_l)
                    boxes_to_move.append(look_r)
                if look2_r in boxes:
                    boxes_to_move.append(look2_r)
                    boxes_to_move.append(look2_l)
                check = copy.deepcopy(boxes_to_move)
                while len(check) > 0:
                    box_check = check.pop(0)
                    if (box_check[0] + 1, box_check[1], 1) in boxes:
                        boxes_to_move.append((box_check[0] + 1, box_check[1], 1))
                        boxes_to_move.append((box_check[0] + 1, box_check[1] + 1, 2))
                        check.append((box_check[0] + 1, box_check[1], 1))
                        check.append((box_check[0] + 1, box_check[1] + 1, 2))
                    elif (box_check[0] + 1, box_check[1], 2) in boxes:
                        boxes_to_move.append((box_check[0] + 1, box_check[1], 2))
                        boxes_to_move.append((box_check[0] + 1, box_check[1] - 1, 1))
                        check.append((box_check[0] + 1, box_check[1], 1))
                        check.append((box_check[0] + 1, box_check[1] - 1, 1))

                for box in boxes_to_move:
                    if (box[0] + 1, box[1]) in walls:
                        boxes_to_move = []

                while len(boxes_to_move) > 0:
                    box = boxes_to_move.pop()
                    if box[2] == 1:
                        look_up = (box[0] + 1, box[1])
                        look_up2 = (box[0] + 1, box[1] + 1)
                    if box[2] == 2:
                        look_up = (box[0] + 1, box[1])
                        look_up2 = (box[0] + 1, box[1] - 1)

                    if look_up in walls or look_up2 in walls:
                        if box[2] == 1:
                            boxes_to_move.remove((box[0], box[1] + 1, 2))
                        if box[2] == 2:
                            boxes_to_move.remove((box[0], box[1] - 1, 1))
                        break
                    elif box[2] == 1 and (box[0] + 1, box[1], 1) not in boxes:
                        boxes.remove(box)
                        boxes.remove((box[0], box[1] + 1, 2))
                        boxes.add((box[0] + 1, box[1], 1))
                        boxes.add((box[0] + 1, box[1] + 1, 2))
                    elif box[2] == 2 and (box[0] + 1, box[1], 2) not in boxes:
                        boxes.remove(box)
                        boxes.remove((box[0], box[1] - 1, 1))
                        boxes.add((box[0] + 1, box[1], 2))
                        boxes.add((box[0] + 1, box[1] - 1, 1))

                if (character[0] + 1, character[1]) not in walls and (
                    (character[0] + 1, character[1], 1) not in boxes
                    and (character[0] + 1, character[1], 2) not in boxes
                ):
                    character = [character[0] + 1, character[1]]

        # print("AAAAAAAAAAAAAAAAAAAAAAAAA")
        # print(move_to)
    score = 0
    for i in boxes:
        if i[2] == 1:
            score += i[0] * 100 + i[1]
    print_warehouse(character, boxes, walls, bounds)
    print(score)


# print(instructions)
# print(character)
# print(boxes)
# move character
# check if box or wall in character direction
day2()
