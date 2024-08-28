class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row,col=len(grid1),len(grid1[0])
        visited=set()
        def dfs(r,c):
            if r<0 or c<0 or r==row or c==col or (r,c) in visited or grid2[r][c]==0:
                return True
            res=True
            visited.add((r,c))
            if grid1[r][c]==0:
                res=False
            res=dfs(r+1,c) and res
            res=dfs(r-1,c) and res
            res=dfs(r,c+1) and res
            res=dfs(r,c-1) and res
            return res
        count=0
        for r in range(row):
            for c in range(col):
                if grid2[r][c] and (r,c) not in visited and dfs(r,c):
                    count+=1
        return count
