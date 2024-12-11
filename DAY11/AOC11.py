#naive solution
with open ("input.txt", "r") as file:
    lines = file.readlines()
stones=[int(x) for x in lines[0].split(" ")]
def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half].lstrip('0') or '0')
            right = int(str(stone)[half:].lstrip('0') or '0')
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    return new_stones
for i in range(25):
    stones = blink(stones)

print(len(stones))  