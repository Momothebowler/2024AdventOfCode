import re

i = 0
machines = {}
c = 0
for lines in open("day13.txt", "r"):
    c += 1
    l = lines.strip("\n")
    if (c // 4) not in machines.keys() and l != "":
        machines[c // 4] = []
    if l != "":
        machines[c // 4].append(l)
# print(machines)
inc = 10000000000000
total_cost = 0


def part1():
    for machine in machines:
        print(machine)
        i = 0
        button1 = re.findall("(\+\d*)+", machines[machine][0])
        button2 = re.findall("(\+\d*)+", machines[machine][1])
        x_goal = int(re.findall("X=\d*", machines[machine][2])[0].strip("X=")) + inc
        y_goal = int(re.findall("Y=\d*", machines[machine][2])[0].strip("Y=")) + inc
        solutions = []
        while True:
            i += 1

            # Button B Presses
            x_press = (int(button1[0].strip("+")) * i * inc - x_goal) / (
                -1 * int(button2[0].strip("+")) * inc
            )
            y_press = (int(button1[1].strip("+")) * i * inc - y_goal) / (
                -1 * int(button2[1].strip("+")) * inc
            )

            if x_press < 0 or y_press < 0:
                break
            if (
                (x_press).is_integer()
                and (y_press).is_integer()
                and int(x_press) == int(y_press)
            ):
                solutions.append([i, int(x_press)])

        if len(solutions) > 0:
            minimum = solutions[0][0] * 3 + solutions[0][1]
            for j in solutions:
                minimum = min(minimum, j[0] * 3 + j[1])
            total_cost += minimum
        # print("-----------")
    print(total_cost)


total = 0
for machine in machines:
    button1 = re.findall("(\+\d*)+", machines[machine][0])
    button2 = re.findall("(\+\d*)+", machines[machine][1])
    x_goal = int(re.findall("X=\d*", machines[machine][2])[0].strip("X=")) + inc
    y_goal = int(re.findall("Y=\d*", machines[machine][2])[0].strip("Y=")) + inc

    button2_presses = (x_goal * int(button1[1]) - y_goal * int(button1[0])) / (
        int(button2[0]) * int(button1[1]) - int(button2[1]) * int(button1[0])
    )
    button1_presses = (x_goal - button2_presses * int(button2[0])) / int(button1[0])
    if button2_presses.is_integer() and button1_presses.is_integer():

        total += int(button1_presses) * 3 + int(button2_presses)
print(total)
