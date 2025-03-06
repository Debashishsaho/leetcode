class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        li = [i for i in range(1,n**2+1)]
        b=[]
        for i in range(n):
            for j in range(n):
                if grid[i][j] in li:
                    li.remove(grid[i][j])
                else:
                    b.append(grid[i][j])
        return b+li