class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0: return 0
        
        numIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    numIslands += self.dfs(grid, i, j)
        
        return numIslands
    
    def dfs(self, grid: List[List[str]], i: int, j: int) -> int:
        
        # If out of bounds or if number is 0, do nothing
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j] == '0': return 0
        
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        return 1