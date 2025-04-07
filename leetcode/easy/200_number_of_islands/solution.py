def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def mark_island_as_visited(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
            return

        grid[r][c] = 0

        mark_island_as_visited(r - 1, c) 
        mark_island_as_visited(r + 1, c)
        mark_island_as_visited(r, c - 1)
        mark_island_as_visited(r, c + 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                island_count += 1
                mark_island_as_visited(row, col)

    return island_count


matrix = [
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1]
]

print(f"Número de ilhas: {count_islands(matrix)}")
