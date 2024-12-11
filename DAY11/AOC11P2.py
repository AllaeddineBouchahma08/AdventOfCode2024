#optimized version 
from collections import Counter
def blink_counter(stones_counter):
    new_stones_counter = Counter()
    for stone, count in stones_counter.items():
        if stone == 0:
            new_stones_counter[1] += count
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half].lstrip('0') or '0')
            right = int(str(stone)[half:].lstrip('0') or '0')
            new_stones_counter[left] += count
            new_stones_counter[right] += count
        else:
            new_stones_counter[stone * 2024] += count
    return new_stones_counter
stones = [28591,78,0,3159881,4254,524155,598,1]
stones_counter = Counter(stones)
for _ in range(75):
    stones_counter = blink_counter(stones_counter)
total_stones = sum(stones_counter.values())
print(total_stones)