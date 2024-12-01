with open("input1.txt", "r") as file:
    lines = file.readlines()


column1 = []
column2 = []

for line in lines:
    col1, col2 = line.split()
    column1.append(int(col1))  
    column2.append(int(col2))  
total=0
for i in range(len(column1)):
    total=total+(column1[i]*column2.count(column1[i]))
print(total)
