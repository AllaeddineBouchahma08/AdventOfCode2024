import re

with open("input.txt", "r") as file:
    lines = file.readlines()
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d+),(\d+)\)"
mul_enabled = True
total = 0
for line in lines:
    tokens = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)
    
    for token in tokens:
        if re.match(do_pattern, token):
            mul_enabled = True
        elif re.match(dont_pattern, token):
            mul_enabled = False
        elif mul_enabled:
            match = re.match(mul_pattern, token)
            if match:
                a, b = map(int, match.groups())  
                total += a * b  

print(total)
