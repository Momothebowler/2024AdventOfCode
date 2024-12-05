import re
from functools import cmp_to_key

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

def sorting(x,y,dict):
    if y in dict[x]:
        return -1
    else:
        return 1

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
        if i[1] not in dict.keys():
            dict[i[1]] = []
        dict[i[0]].append(i[1])

    updated = []
    for i in updates:
        bad = True
        for k in range(len(i) - 1):
            if i[k+1] not in dict[i[k]]:
                bad = False
                break
        if not bad:
            updated.append(sorted(i,key=cmp_to_key(lambda item1, item2: sorting(item1,item2,dict))))

    #print(updated)
    sum = 0
    for i in updated:
        sum += int(i[int((len(i) - 1) / 2)])
    print(sum)


part2()
