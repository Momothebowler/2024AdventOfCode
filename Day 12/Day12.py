plot_list = [element.strip("\n") for element in open("day12.txt")]
plots = {
    (plot_list[i][j], i, j)
    for i in range(len(plot_list))
    for j in range(len(plot_list[i]))
}
p = {}
for i in plots:
    if i[0] not in p.keys():
        p[i[0]] = []

    p[i[0]].append(i)

areas = {}


def reduce(r):
    group = {}
    traversed = []
    queue = [r[0]]

    while queue:

        i = queue.pop(0)
        try:
            r.remove(i)
        except:
            print(r)
            print()
            print(i)
            print("------------")

        if i[0] not in group.keys():
            group[i[0]] = []
        group[i[0]].append(i)

        if i in queue:
            queue.remove(i)

        traversed.append(i)

        right = (i[0], i[1] + 1, i[2]) in r
        left = (i[0], i[1] - 1, i[2]) in r
        down = (i[0], i[1], i[2] + 1) in r
        up = (i[0], i[1], i[2] - 1) in r

        if right and (i[0], i[1] + 1, i[2]) not in traversed:
            queue.append((i[0], i[1] + 1, i[2]))

        if left and (i[0], i[1] - 1, i[2]) not in traversed:
            queue.append((i[0], i[1] - 1, i[2]))

        if up and (i[0], i[1], i[2] - 1) not in traversed:
            queue.append((i[0], i[1], i[2] - 1))

        if down and (i[0], i[1], i[2] + 1) not in traversed:
            queue.append((i[0], i[1], i[2] + 1))

        if len(queue) == 0 and len(r) > 0:
            for l in range(len(r)):
                t = list(r[l])
                t[0] = t[0] + "1"
                r[l] = tuple(t)
            queue.append(r[0])
    return group


def check_inside(r):
    removing = []
    perim = 0
    for i in r:
        s = 0
        seen = []
        for j in r:
            if i == j:
                continue
            if j not in seen and i[1] + 1 == j[1] and i[2] == j[2]:
                s += 1
                seen.append(j)
            if j not in seen and i[1] - 1 == j[1] and i[2] == j[2]:
                s += 1
                seen.append(j)
            if j not in seen and i[2] + 1 == j[2] and i[1] == j[1]:
                s += 1
                seen.append(j)
            if j not in seen and i[2] - 1 == j[2] and i[1] == j[1]:
                s += 1
                seen.append(j)
            if s >= 4:
                removing.append(i)
                break
        if s <= 3:
            perim += 4 - s
            continue

    for i in removing:
        r.remove(i)
    return r, perim


area = {}
perimeter = {}
r = {}
for i in p:
    k = reduce(p[i])
    for j in k.keys():
        r[j] = k[j]

q = {}
for i in r.keys():
    area[i] = len(r[i])

    q[i], perim = check_inside(r[i])
    perimeter[i] = perim

cost = 0
for i in q:
    plot_area = area[i]
    cost += plot_area * perimeter[i]

print(cost)
