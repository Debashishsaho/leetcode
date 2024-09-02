class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n<len(original) or m*n>len(original):
            return []
        dicto=[[0]*n for i in range(m)]
        k=0
        while k<n*m:
            i=k//n
            j=k%n
            dicto[i][j]=original[k]
            k+=1
        return dicto