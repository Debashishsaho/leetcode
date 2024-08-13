class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(ind,path,remaining):
            if remaining==0:
                res.append(path[:])
            for i in range(ind,len(candidates)):
                if remaining<0:
                    break
                if i!=ind and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1,path,remaining-candidates[i])
                path.pop()
        candidates.sort()
        res=[]
        dfs(0,[],target)
        return res