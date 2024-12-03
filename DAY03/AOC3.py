import re
with open("input.txt", "r") as file:
    lines = file.readlines()
regex = r"mul\((\d+),(\d+)\)"
total = 0
for line in lines:
    match= re.findall(regex, line)
    for m in match:
        a,b= map(int, m)
        total=total+a*b
print(total)
