lines = []

for l in open("day10_alt.txt"):
    lines.append(l.strip())


starts = []
for l in range(len(lines)):
    for i in range(len(lines[l])):
        if lines[l][i] == "0":
            starts.append([l, i, 0])
sums = 0
print(starts)
while len(starts) > 0:
    start = starts.pop()
    # while start[2] <= 9:
    print(start)
    posy = start[0]
    posx = start[1]
    if int(lines[posy][posx]) == 9:
        sums += 1
        continue
    elif start[2] == 9:
        continue

    if posy > 0 and int(lines[posy - 1][posx]) == int(lines[posy][posx]) + 1:
        starts.append([posy - 1, posx, start[2] + 1])

    if (
        posy < len(lines) - 1
        and int(lines[posy + 1][posx]) == int(lines[posy][posx]) + 1
    ):
        starts.append([posy + 1, posx, start[2] + 1])
        # print("e")

    if posx > 0 and int(lines[posy][posx - 1]) == int(lines[posy][posx]) + 1:
        starts.append([posy, posx - 1, start[2] + 1])
        # print([posy, posx - 1, start[2] + 1])
        # print("-----------------")

    if (
        posx < len(lines[posy]) - 1
        and int(lines[posy][posx + 1]) == int(lines[posy][posx]) + 1
    ):
        starts.append([posy, posx + 1, start[2] + 1])
        # print("g")
print(sums)
