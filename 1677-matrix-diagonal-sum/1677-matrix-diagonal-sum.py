class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        res=0
        r=0
        c=0
        for i in range(2*n):
            if i<=n-1:
                res+=mat[r][c]
                r+=1
                c+=1
            else:
                r=i%n
                c=c-1
                res+=mat[r][c]
        if n%2:
            res -= mat[n//2][n//2]
        return res

