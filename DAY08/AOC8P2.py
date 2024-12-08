from collections import defaultdict

def parse_input(map_data):
    return [(x, y, cell) for y, row in enumerate(map_data) for x, cell in enumerate(row.strip()) if cell != "."]

def calculate_antinodes(antennas, width, height):
    antinode_positions = set()
    freq_map = defaultdict(list)

    for x, y, freq in antennas:
        freq_map[freq].append((x, y))

    for positions in freq_map.values():
        n = len(positions)
        if n < 2:
            continue  # Skip frequencies with only one antenna
        
        # Add all antenna positions as potential antinodes
        antinode_positions.update(positions)

        # Check every pair of antennas
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i+1:]:
                dx, dy = x2 - x1, y2 - y1

                # Extend in both directions
                for step in range(-max(width, height), max(width, height) + 1):
                    x, y = x1 + step * dx, y1 + step * dy
                    if 0 <= x < width and 0 <= y < height:
                        antinode_positions.add((x, y))

    return antinode_positions

with open("input.txt", "r") as file:
    lines = file.readlines()

antennas = parse_input(lines)
width, height = len(lines[0].strip()), len(lines)
antinodes = calculate_antinodes(antennas, width, height)
print(f"Number of unique antinodes: {len(antinodes)}")
