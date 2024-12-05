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

def fix_line(line, rules):
    while True:
        is_correct = True
        for i in range(len(line) - 1):
            current, next_element = line[i], line[i + 1]
            if next_element not in rules.get(current, []):
                if current in rules.get(next_element, []): 
                    line[i], line[i + 1] = line[i + 1], line[i]
                    is_correct = False
        if is_correct:
            break
    return line

incorrect = [
    line for line in list_section
    if not all(line[i + 1] in dict_section.get(line[i], []) for i in range(len(line) - 1))
]

corrected_lines = []
for line in incorrect:
    corrected_line = fix_line(line, dict_section)
    corrected_lines.append(corrected_line)

middle_sum = sum(
    line[len(line) // 2] for line in corrected_lines if len(line) % 2 == 1
)
print(middle_sum)
