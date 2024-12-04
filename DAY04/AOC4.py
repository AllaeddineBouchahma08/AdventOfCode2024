with open("input.txt", "r") as file:
    grid = file.readlines()
def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),    # Right
        (0, -1),   # Left
        (1, 0),    # Down
        (-1, 0),   # Up
        (1, 1),    # Down-Right
        (-1, -1),  # Up-Left
        (1, -1),   # Down-Left
        (-1, 1)    # Up-Right
    ]
    target = "XMAS"
    target_length = len(target)
    count = 0
    def search_direction(x, y, dx, dy):
        for i in range(target_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != target[i]:
                return False
        return True
    
    for row in range(rows):
        for col in range(cols):
            # Check for 'X' to start the search
            if grid[row][col] == 'X':
                # Search in all directions
                for dx, dy in directions:
                    if search_direction(row, col, dx, dy):
                        count += 1
    
    return count

# Example usage:

print(count_xmas(grid))  # Output: 18
