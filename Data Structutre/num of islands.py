def number_of_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(row, col):
        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            grid[row][col] == '0'):
            return

        grid[row][col] = '0'

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count


grid = [
    ['1', '1', '0', '0'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '1']
]

print(number_of_islands(grid))
