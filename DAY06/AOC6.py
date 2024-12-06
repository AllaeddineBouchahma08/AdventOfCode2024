with open("input.txt", "r") as file:
    lines = file.readlines()
def find_position_of_caret(grid):
    for row_index, row in enumerate(grid):
        col_index = row.find('^') 
        if col_index != -1:      
            return row_index, col_index
    return None  
def go_direction(pos, direction, grid):
    row, col = pos
    grid = [list(line.strip()) for line in grid]  
    grid[row][col] = 'X'  
    if direction == 'up' and row > 0:
        if grid[row - 1][col] != '#':  
            row -= 1
            grid[row][col] = '^'
        else:  
            direction = 'right'
    elif direction == 'down' and row < len(grid) - 1:
        if grid[row + 1][col] != '#': 
            row += 1
            grid[row][col] = 'v'
        else:  
            direction = 'left'
    elif direction == 'left' and col > 0:
        if grid[row][col - 1] != '#': 
            col -= 1
            grid[row][col] = '<'
        else:  
            direction = 'up'
    elif direction == 'right' and col < len(grid[row]) - 1:
        if grid[row][col + 1] != '#':  
            col += 1
            grid[row][col] = '>'
        else:  
            direction = 'down'
    else:
        
        return (None, None), [''.join(line) for line in grid], direction

    grid = [''.join(line) for line in grid]  
    return (row, col), grid, direction

def count_X_on_grid(grid):
    return sum(row.count('X') for row in grid)

pos = find_position_of_caret(lines)
direction = 'up'  

while pos:
    row, col = pos
    pos, lines, direction = go_direction(pos, direction, lines)
    if pos == (None, None):
        num_X = count_X_on_grid(lines)
        print(num_X)
        break