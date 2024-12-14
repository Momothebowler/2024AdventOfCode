import math

robots = {}
# alt_bounds = [11, 7]  # wide, tall
bounds = [101, 103]
count = 0
for line in open(f"day14.txt", "r"):
    robot = line.strip("\n").split(" ")
    position = robot[0].strip("p=").split(",")
    velocity = robot[1].strip("v=").split(",")
    count += 1
    robots[count] = {
        "position": [int(position[0]), int(position[1])],
        "velocity": [int(velocity[0]), int(velocity[1])],
    }


def screen_wrap(position, bounds):
    # wdith, height
    while position[1] <= 0:
        # good
        position[1] = bounds[1] + position[1]
    while position[1] >= bounds[1]:
        # good?
        position[1] = position[1] - bounds[1]

    while position[0] <= 0:
        # good?
        position[0] = bounds[0] + position[0]
    while position[0] >= bounds[0]:
        # good?
        position[0] = position[0] - bounds[0]
    # print(position)
    # print(velocity)
    return position


seconds = 101 * 103  # 2 is 3
prev_safety = 100000000000000000000000
for k in range(1, seconds):

    if k % 10 == 0:
        print(k)

    quadrants = [0, 0, 0, 0]
    for robot in robots:
        pos = [0, 0]
        pos[0] = (
            robots[robot]["position"][0] + robots[robot]["velocity"][0] * k
        ) % bounds[0]
        pos[1] = (
            robots[robot]["position"][1] + robots[robot]["velocity"][1] * k
        ) % bounds[1]
        mid_vert = math.floor(bounds[0] / 2)
        mid_hort = math.floor(bounds[1] / 2)
        if pos[0] == mid_vert or pos[1] == mid_hort:
            continue
        if pos[0] < mid_vert and pos[1] < mid_hort:
            quadrants[0] += 1
        elif pos[0] > mid_vert and pos[1] < mid_hort:
            quadrants[1] += 1
        elif pos[0] < mid_vert and pos[1] > mid_hort:
            quadrants[2] += 1
        elif pos[0] > mid_vert and pos[1] > mid_hort:
            quadrants[3] += 1

    safety = 1
    for j in quadrants:
        safety *= j
    prev_safety = min(safety, prev_safety)
    if prev_safety < safety:
        continue

    elif prev_safety >= safety:
        print(f"{k}: {safety} >= {prev_safety}")
        f = open(f"trees/tree{k}.txt", "w")
        for i in range(bounds[1]):  # height
            for j in range(bounds[0]):  # width
                on_spot = 0
                for robot in robots:
                    if (
                        robots[robot]["position"][0] + robots[robot]["velocity"][0] * k
                    ) % bounds[0] == j and (
                        robots[robot]["position"][1] + robots[robot]["velocity"][1] * k
                    ) % bounds[
                        1
                    ] == i:
                        on_spot += 1
                if on_spot > 0:
                    f.write(str(on_spot))
                else:
                    f.write(".")
            f.write("\n")
        f.close()
