line = ""
for lines in open("day9.txt"):
    line += lines

data = []
# line = "12345"
count = 0
for i in range(len(line)):
    if i % 2 == 0:
        for j in range(int(line[i])):
            data.append(count)
        count += 1
    else:
        for j in range(int(line[i])):
            data.append(".")


def p1():
    c = len(data) - 1
    b = 0
    while True:
        moved = False

        while b < c:
            while b < c and data[b] != ".":
                b += 1
            while b < c and data[c] == ".":
                c -= 1
                moved = True

            if b < c:
                data[b] = data[c]
                data[c] = "."
                b += 1
                c -= 1

        if not moved:
            break


def p2(d):
    tried = []
    c1 = len(d) - 1
    c2 = len(d) - 1
    while d[c1] != "0":
        # print(c2)
        while d[c1] == ".":
            c1 -= 1

        c2 = c1
        while d[c2] == d[c1]:
            c2 -= 1
        if c2 <= 0:
            break

        if c1 not in tried:
            b = 0
            tried.append(c1)
            while "." in d[b:]:

                while d[b] != ".":
                    b += 1
                b2 = b
                if b >= len(d):
                    break
                while d[b2] == ".":
                    b2 += 1

                    if b2 >= len(d):
                        break
                if b2 >= len(d):
                    break

                if c1 - c2 <= b2 - b and c2 > b2:
                    for i in range(c1 - c2):
                        d[b + i] = d[c1 - i]
                        d[c1 - i] = "."
                        f = open("day9_print.txt", "w")
                        f.write("".join(str(x) for x in d))
                        f.close()
                        # print("".join(str(x) for x in d))
                    break
                b = b2
            # print("".join(str(x) for x in d))

        c1 = c2
    return d


# print("".join(str(x) for x in data))
# data = p2(data)
sum = 0
# print(data)
# for i in range(len(data)):
# print(f"{i} * {data[i]}")
#    if data[i] != ".":
#        sum += i * int(data[i])

# print(sum)
# data = "".join(str(x) for x in data)
# print(data)
