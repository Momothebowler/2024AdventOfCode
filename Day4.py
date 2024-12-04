import pandas as pd
import re

consider = []

for line in open("Day4.csv"):
    consider.append(line.strip("\n"))


def part1():
    total = 0
    for j in range(len(consider)):
        for i in range(len(consider[j])):
            if consider[j][i] == "X":
                # Right
                if i <= len(consider[j]) - 4 and consider[j][i + 1] == "M":
                    if consider[j][i + 2] == "A":
                        if consider[j][i + 3] == "S":
                            total += 1
                # Down
                if j <= len(consider) - 4 and consider[j + 1][i] == "M":
                    if consider[j + 2][i] == "A":
                        if consider[j + 3][i] == "S":
                            total += 1
                # Right Diag
                if (
                    i <= len(consider[j]) - 4
                    and j <= len(consider) - 4
                    and consider[j + 1][i + 1] == "M"
                ):
                    if consider[j + 2][i + 2] == "A":
                        if consider[j + 3][i + 3] == "S":
                            total += 1
                # Left Diag
                if j <= len(consider) - 4 and i >= 3 and consider[j + 1][i - 1] == "M":
                    if consider[j + 2][i - 2] == "A":
                        if consider[j + 3][i - 3] == "S":
                            total += 1
                # Up
                if j >= 3 and consider[j - 1][i] == "M":
                    if consider[j - 2][i] == "A":
                        if consider[j - 3][i] == "S":
                            total += 1

            if consider[j][i] == "S":
                # Right
                if i <= len(consider[j]) - 4 and consider[j][i + 1] == "A":
                    if consider[j][i + 2] == "M":
                        if consider[j][i + 3] == "X":
                            total += 1
                # Right Diag
                if (
                    i <= len(consider[j]) - 4
                    and j <= len(consider) - 4
                    and consider[j + 1][i + 1] == "A"
                ):
                    if consider[j + 2][i + 2] == "M":
                        if consider[j + 3][i + 3] == "X":
                            total += 1
                # Left Diag
                if j <= len(consider) - 4 and consider[j + 1][i - 1] == "A" and i >= 3:
                    if consider[j + 2][i - 2] == "M":
                        if consider[j + 3][i - 3] == "X":
                            total += 1
    return total


def part2():
    total = 0
    for j in range(len(consider) - 2):
        for i in range(len(consider[j]) - 2):
            # Top left
            if consider[j][i] == "M":
                if consider[j + 1][i + 1] == "A":
                    # Top right
                    if consider[j][i + 2] == "S":
                        # Bottom Left
                        if consider[j + 2][i] == "M":
                            # Bottom Right
                            if consider[j + 2][i + 2] == "S":
                                total += 1
                    # Top right
                    if consider[j][i + 2] == "M":
                        # Bottom Left
                        if consider[j + 2][i] == "S":
                            # Bottom Right
                            if consider[j + 2][i + 2] == "S":
                                total += 1
            # Top left
            if consider[j][i] == "S":
                if consider[j + 1][i + 1] == "A":
                    # Top right
                    if consider[j][i + 2] == "S":
                        # Bottom Left
                        if consider[j + 2][i] == "M":
                            # Bottom Right
                            if consider[j + 2][i + 2] == "M":
                                total += 1
                    # Top right
                    if consider[j][i + 2] == "M":
                        # Bottom Left
                        if consider[j + 2][i] == "S":
                            # Bottom Right
                            if consider[j + 2][i + 2] == "M":
                                total += 1

    return total


print(part2())
