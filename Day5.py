import re


def part1():
    pairs = []
    updates = []
    good = []
    for line in open("day5_alt.txt"):
        rule = re.findall("(\d+\|\d+)", line)
        update = re.findall(".*,+.*", line)
        # print(update)
        if rule:
            pairs.append(rule[0].split("|"))
        if update:
            updates.append(update[0].split(","))

    for i in range(len(updates)):
        works = 0
        for j in range(len(pairs)):
            for k in range(len(updates[i]) - 1):
                if updates[i][k] == pairs[j][0] and updates[i][k + 1] == pairs[j][1]:
                    works += 1

        if works == len(updates[i]) - 1:
            good.append(updates[i])

    sum = 0
    for i in good:
        sum += int(i[int((len(i) - 1) / 2)])
    print(sum)


def part2():
    pairs = []
    updates = []
    dict = {}

    for line in open("day5.txt"):
        rule = re.findall("(\d+\|\d+)", line)
        update = re.findall(".*,+.*", line)
        if rule:
            pairs.append(rule[0].split("|"))
        if update:
            updates.append(update[0].split(","))

    for i in pairs:
        if i[0] not in dict.keys():
            dict[i[0]] = []
        dict[i[0]].append(i[1])

    updated = []
    for i in updates:
        temp = []
        for j in range(len(i) - 1):
            if i[j + 1] in dict[i[j]]:
                temp.append(i[j])
            else:
                shift = len(temp)
                for k in range(len(i) - shift):
                    if i[j] != "" and i[k + shift] in dict[i[j]]:
                        temp.append(i[j])
                        i[j] = ""

            if j == len(i) - 1:
                temp.append(i[j + 1])
        updated.append(temp)

    updated = updates
    updated = sorted(updates, key=dict.get)
    print(updated)
    sum = 0
    for i in updated:
        sum += int(i[int((len(i) - 1) / 2)])
    print(sum)


part2()
