def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    patterns = {"MAS", "SAM"}  # Valid diagonal patterns
    count = 0

    # Helper function to check if a diagonal matches a pattern
    def check_diagonal(x, y, dx1, dy1, dx2, dy2):
        try:
            d1 = grid[x + dx1][y + dy1] + grid[x][y] + grid[x - dx1][y - dy1]
            d2 = grid[x + dx2][y + dy2] + grid[x][y] + grid[x - dx2][y - dy2]
            return d1 in patterns and d2 in patterns
        except IndexError:
            return False

    
    for x in range(1, rows - 1):  # Avoid edges
        for y in range(1, cols - 1):  # Avoid edges
            if grid[x][y] == "A":
                if check_diagonal(x, y, 1, 1, 1, -1):  # Check diagonals
                    count += 1

    return count
with open("input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]
print(count_xmas(grid))  
