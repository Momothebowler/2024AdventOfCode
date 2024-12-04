
boom = 0 
boom2 = 0
inc = False
dec = False
lines = 0

def isSafe(nums):
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            #print(str(nums) + " =")
            return False
        elif abs(nums[i+1] - nums[i]) > 3:
            #print(str(nums) + " > 3 jump with "+ str(nums[i + 1]) + " - " + str(nums[i])) 
            return False
        if i >= 1:
            if nums[i - 1] > nums[i] < nums[i + 1]:
                #print(str(nums) + " decreasing then increasing")
                return False
            elif nums[i+1] < nums[i] > nums[i - 1]:
                #print(str(nums) + " increasing then decreasing")
                return False
    return True



with open("Day2.csv",'r') as file:
    for line in file:
        if line:
            lines += 1
        nums = line.strip().split(sep= " ")
        nums = list(map(int, nums))
        if not isSafe(nums):
            boom2 += 1
            for i in range(len(nums)):
                nums2 = nums[:i] + nums[i+1:]
                #print(nums2)
                if isSafe(nums2):
                    break
                    #print(i)
                    #print("nums:" + str(len(nums)))
                else:
                    #print(nums2)
                    if i == len(nums)-1:
                        boom +=1
                    continue
                
                

print(lines - boom)
print(lines - boom2)
