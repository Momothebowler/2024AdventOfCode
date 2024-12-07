import copy

lines = []
player = ()
board_size = [0,0]

def direction_change(dir2):
    if dir2 == "North":
        dir2 = "East"
    elif dir2 == "South":
        dir2 = "West"
    elif dir2 == "East":
        dir2 = "South"
    elif dir2 == "West":
        dir2 = "North"
    return dir2
        
with open(r"day6.txt", 'r') as fp:
    for count, line in enumerate(fp):
        board_size[1] += 1
        board_size[0] = len(line)
        lines.append(list(line))
        for k in range(len(line)):
            if line[k] == "^":
                player = [count,k]
                

dir = "North"
safe = []
def part1(dir, player, board_size, lines):
    while (player[0] >= 0 and player[0] < board_size[0]) and (player[1] >= 0 and player[1] <= board_size[1]):
        try:
            safe.append(copy.deepcopy(player))
            if dir == "North" and lines[player[0]-1][player[1]] != "#":
                player[0]-=1
                lines[player[0]][player[1]] = "^"
                lines[player[0]+1][player[1]] = "X" 
            elif dir == "South" and lines[player[0]+1][player[1]] != "#":
                player[0]+=1
                lines[player[0]][player[1]] = "^"
                lines[player[0]-1][player[1]] = "X"  
            elif dir == "East" and lines[player[0]][player[1]+1] != "#":
                player[1]+=1
                lines[player[0]][player[1]] = "^"
                lines[player[0]][player[1]-1] = "X" 
            elif dir == "West" and lines[player[0]][player[1]-1] != "#":
                player[1]-=1
                lines[player[0]][player[1]] = "^"
                lines[player[0]][player[1]+1] = "X" 
            else:
                dir = direction_change(dir)
        except:
            lines[player[0]][player[1]] = "X"
            if dir == "North":
                player[0]-=1
            elif dir == "South":
                player[0]+=1
            elif dir == "East":
                player[1]+=1 
            elif dir == "West":
                player[1]-=1
        
       
def part2(dir, player, board_size, lines2):  
    block = 0
    counting = 0
    start = copy.deepcopy(player) 
    print(safe)
    for safe_place in safe:
        counting+= 1
        j = safe_place[0]
        i = safe_place[1]
        print("j: " + str(j)+ " i: " + str(i) + " iter: " + str(counting))
        dir = "North"
        player = copy.deepcopy(start)
        lines = copy.deepcopy(lines2) 
        locations = []
        if lines[i][j] == ".":
            lines[i][j] = "#"
            while player[0] >= 0 and player[0] <= board_size[0] and player[1] >= 0 and player[1] <= board_size[1]:
                #if i == 6 and j == 3:
                        
                    
                #for l in lines:
                #    print("".join(l),end="")
                #print("\n-------------------")
            
                if (player,dir) in locations:
                    print("i:" + str(i) + " j:"+ str(j) + " Looping")
                    block += 1
                    break
                try:
                    if dir == "North" and lines[player[0]-1][player[1]] != "#":
                        locations.append((copy.copy(player),"North"))
                        player[0]-=1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0]+1][player[1]] == "^":
                            lines[player[0]+1][player[1]] = "." 
                        
                    elif dir == "South" and lines[player[0]+1][player[1]] != "#":
                        locations.append((copy.copy(player),"South"))
                        player[0]+=1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0]-1][player[1]] == "^":
                            lines[player[0]-1][player[1]] = "." 
                            
                    elif dir == "East" and lines[player[0]][player[1]+1] != "#":
                        locations.append((copy.copy(player),"East"))
                        player[1]+=1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0]][player[1]-1] == "^":
                            lines[player[0]][player[1]-1] = "." 
                        
                    elif dir == "West" and lines[player[0]][player[1]-1] != "#":
                        locations.append((copy.copy(player),"West"))
                        player[1]-=1
                        lines[player[0]][player[1]] = "^"
                        if lines[player[0]][player[1]+1] == "^":
                            lines[player[0]][player[1]+1] = "." 
                    else:
                        dir = direction_change(dir)
                except:
                    if dir == "North":
                        player[0]-=1
                    elif dir == "South":
                        player[0]+=1
                    elif dir == "East":
                        player[1]+=1 
                    elif dir == "West":
                        player[1]-=1
    print(block)
      
part1(dir,player,board_size,lines)
part2(dir, player, board_size, lines)        
                
total = 0
for l in lines:
    total += l.count("O")
    #print("".join(l),end="")
#print()
#print(total)