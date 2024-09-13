class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        prefix_xor=[0]*n
        prefix_xor[0]=arr[0]
        for i in range(1,n):
            prefix_xor[i] = prefix_xor[i-1]^arr[i]
        res=[0]*len(queries)
        for i in range(len(queries)):
            if queries[i][0]==0:
                res[i]=prefix_xor[queries[i][1]]
                continue
            res[i]=prefix_xor[queries[i][0]-1] ^ prefix_xor[queries[i][1]]
        return res