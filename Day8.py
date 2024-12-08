antenna = {}
boundary = [0, 0]
anti = {}
with open(r"day8.txt", "r") as fp:
    for count, line in enumerate(fp):
        line = line.strip("\n")
        boundary[1] = len(line)
        for i in range(len(line)):
            if line[i] != ".":
                if line[i] not in antenna.keys():
                    antenna[line[i]] = []
                    anti[line[i]] = []
                antenna[line[i]].append([count, i])
        boundary[0] = count + 1

for a in antenna:
    if len(antenna[a]) > 1:
        for j in range(len(antenna[a])):
            anti[a].append(antenna[a][j])
            for k in range(j + 1, len(antenna[a])):
                d = [
                    antenna[a][k][0] - antenna[a][j][0],
                    antenna[a][k][1] - antenna[a][j][1],
                ]

                d2 = [antenna[a][j][0] - d[0], antenna[a][j][1] - d[1]]
                d1 = [antenna[a][k][0] + d[0], antenna[a][k][1] + d[1]]

                # print(f"{antenna[a][j]} - {d} = {d2}")
                # print(f"{antenna[a][k]} + {d} = {d1}")
                # print(f"point {antenna[a][k]} and {antenna[a][j]} yield {d}")
                # print("--------------")
                if 0 <= d1[0] < boundary[0] and 0 <= d1[1] < boundary[1]:
                    anti[a].append(d1)
                if 0 <= d2[0] < boundary[0] and 0 <= d2[1] < boundary[1]:
                    anti[a].append(d2)

                while 0 <= d1[0] < boundary[0] and 0 <= d1[1] < boundary[1]:
                    d1 = [d1[0] + d[0], d1[1] + d[1]]
                    if 0 <= d1[0] < boundary[0] and 0 <= d1[1] < boundary[1]:
                        anti[a].append(d1)
                while 0 <= d2[0] < boundary[0] and 0 <= d2[1] < boundary[1]:
                    d2 = [d2[0] - d[0], d2[1] - d[1]]
                    if 0 <= d2[0] < boundary[0] and 0 <= d2[1] < boundary[1]:
                        anti[a].append(d2)

# print(anti)
unique = []
for a in anti:
    for i in range(len(anti[a])):
        if anti[a][i] not in unique:
            unique.append(anti[a][i])

# print(unique)
print(len(unique))
