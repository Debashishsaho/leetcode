class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sumrow0 = sum(grid[0])
        sumrow1 = 0
        ans=float('inf')
        for i in range(len(grid[0])):
            sumrow0 -= grid[0][i]
            ans = min(ans,max(sumrow0,sumrow1))
            sumrow1 += grid[1][i]
        return ans