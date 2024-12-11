from collections import deque

# Read and parse the topographic map from 'input.txt'
with open('input.txt', 'r') as file:
    topographic_map = [list(map(int, line.strip())) for line in file]

# Function to calculate trailhead scores
def find_trailhead_scores(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def is_valid(x, y, current_height):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == current_height + 1
    
    def bfs(trailhead):
        visited = set()
        queue = deque([trailhead])
        reachable_nines = set()
        
        while queue:
            x, y = queue.popleft()
            
            if grid[x][y] == 9:
                reachable_nines.add((x, y))
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and is_valid(nx, ny, grid[x][y]):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        return len(reachable_nines)
    
    total_score = 0
    
    # Identify all trailheads
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                total_score += bfs((i, j))
    
    return total_score

# Compute the sum of scores of all trailheads
result = find_trailhead_scores(topographic_map)
print("Sum of scores of all trailheads:", result)
