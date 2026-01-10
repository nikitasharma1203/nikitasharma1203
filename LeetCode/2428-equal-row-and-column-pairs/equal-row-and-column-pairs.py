class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        row_map = {}

        for row in grid:
            row_tuple = tuple(row)
            row_map[row_tuple] = row_map.get(row_tuple, 0) + 1

        count = 0
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            count += row_map.get(col_tuple, 0)

        return count
