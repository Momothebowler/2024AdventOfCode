lines = []

for l in open("day10.txt"):
    lines.append(l.strip())


starts = []
for l in range(len(lines)):
    for i in range(len(lines[l])):
        if lines[l][i] == "0":
            starts.append([l, i, 0])

sums = 0
print(starts)
for s in starts:
    q = [s]
    traveled_final = []
    while len(q) > 0:
        start = q.pop()
        posy = start[0]
        posx = start[1]
        # uncomment for Part 1 solution
        if start[2] >= 9:  # and [posy, posx] not in traveled_final:
            print("--------------")
            if int(lines[posy][posx]) == 9:
                traveled_final.append([posy, posx])
                sums += 1
            continue

        if posy > 0 and int(lines[posy - 1][posx]) == int(lines[posy][posx]) + 1:
            q.append([posy - 1, posx, start[2] + 1])

        if (
            posy < len(lines) - 1
            and int(lines[posy + 1][posx]) == int(lines[posy][posx]) + 1
        ):
            q.append([posy + 1, posx, start[2] + 1])

        if posx > 0 and int(lines[posy][posx - 1]) == int(lines[posy][posx]) + 1:
            q.append([posy, posx - 1, start[2] + 1])

        if (
            posx < len(lines[posy]) - 1
            and int(lines[posy][posx + 1]) == int(lines[posy][posx]) + 1
        ):
            q.append([posy, posx + 1, start[2] + 1])


print(sums)
