def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

def get_last_num(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] != '.':
            return i
    return -1

with open("input.txt", "r") as file:
    lines = file.read().strip()

ind = 0
free = False
list1 = []

for i in range(0, len(lines), 2):
    file_len = int(lines[i])
    free_len = int(lines[i + 1]) if i + 1 < len(lines) else 0
    
    for _ in range(file_len):
        list1.append(ind)
    ind += 1
    
    for _ in range(free_len):
        list1.append('.')

for i in range(len(list1)):
    if list1[i] == '.':
        last_num_idx = get_last_num(list1)
        if last_num_idx == -1 or last_num_idx <= i:
            break
        list1 = swap(list1, i, last_num_idx)

checksum = sum(pos * int(block) for pos, block in enumerate(list1) if block != '.')

print("Final compacted disk:", ''.join(map(str, list1)))
print("Filesystem checksum:", checksum)
