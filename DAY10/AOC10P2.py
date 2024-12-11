from collections import defaultdict

# Read and parse the topographic map from 'input.txt'
with open('input.txt', 'r') as file:
    topographic_map = [list(map(int, line.strip())) for line in file]

# Function to calculate trailhead ratings
def find_trailhead_ratings(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y, current_height, visited):
        # If we reach height 9, it's a valid hiking trail end
        if grid[x][y] == 9:
            return 1
        
        total_trails = 0
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and (nx, ny) not in visited
                and grid[nx][ny] == current_height + 1
            ):
                total_trails += dfs(nx, ny, grid[nx][ny], visited)
        visited.remove((x, y))
        return total_trails

    total_rating = 0

    # Identify all trailheads
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                total_rating += dfs(i, j, 0, set())
    
    return total_rating

# Compute the sum of ratings of all trailheads
result = find_trailhead_ratings(topographic_map)
print("Sum of ratings of all trailheads:", result)
