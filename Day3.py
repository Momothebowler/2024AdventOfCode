import re

def mul(x,y):
    return x*y

sum = 0
text =""
for line in open("day3.txt"):
    for l in line:
        text+=l
        
i = text.find("don't")
begin = text[0:i]
#text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
trial = re.findall("(do\(\).*(don\'t\(\))*)*",text) 
print(trial)
text2 = str(begin)
for t in trial:
    text2 += t[0]



call_funcs = re.findall("(mul\([0-9]+,[0-9]+\))",text2)
for call in call_funcs:
    nums = re.findall("[0-9]+",str(call))
    sum += mul(float(nums[0]),float(nums[1]))
    
print(sum)