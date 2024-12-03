import pandas as pd

c = pd.read_csv("Day1.csv", sep="  ", engine="python")

# sort1 = [3, 4, 2, 1, 3, 3]
# sort2 = [4, 3, 5, 3, 9, 3]

sorted1 = []
sorted2 = []

sorted1 = sorted(c["Column1"])
sorted2 = sorted(c["Column2"])

# sorted1 = sorted(sort1)
# sorted2 = sorted(sort2)

distance = 0

for i in range(len(sorted1)):
    distance += abs(sorted1[i] - sorted2[i])


sim_score = 0
flag = False

for i in range(len(sorted1)):
    count = 0
    for j in range(len(sorted2)):
        if sorted1[i] == sorted2[j]:
            count += 1
            flag = True
        elif flag == True:
            flag = False
            continue
        else:
            flag = False
    sim_score += sorted1[i] * count


print(sim_score)
