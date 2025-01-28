class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            fish_count=grid[i][j]
            grid[i][j]=0
            for dx,dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                x,y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < m and grid[x][y]:
                    fish_count +=dfs(x,y)
            return fish_count
        maxi=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    maxi=max(maxi,dfs(i,j))
        return maxi
        


