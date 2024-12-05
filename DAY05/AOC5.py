with open("input.txt", "r") as file:
    data = file.read().splitlines()
split_index = data.index("")
first_section = data[:split_index]
second_section = data[split_index + 1:]
dict_section = {}
for line in first_section:
    key, value = map(int, line.split('|'))
    dict_section.setdefault(key, []).append(value)
list_section = [list(map(int, line.split(','))) for line in second_section]
result = [
    line for line in list_section
    if all(line[i + 1] in dict_section.get(line[i], []) for i in range(len(line) - 1))
]
middle_sum = sum(line[len(line) // 2] for line in result if len(line) % 2 == 1)

print(middle_sum)
