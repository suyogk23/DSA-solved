class Solution:
    # solution by @suyogk23 (GitHub)
    # 1. Store each row and column in a hashmap (Counter).
    # 2. Count how many times each row/col occurs.
    # 3. For each matching row = col, add row_count * col_count
    #   (like a cartesian product, since every row instance can pair with every col instance).
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        cols = defaultdict(int)

        for k in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][k])
            col = tuple(col)
            cols[col] += 1

        for i in range(n):
            row = tuple(grid[i])
            rows[row] += 1
        
        ans = 0
        for key in rows:
            ans += rows[key] * cols[key]

        return ans
            
