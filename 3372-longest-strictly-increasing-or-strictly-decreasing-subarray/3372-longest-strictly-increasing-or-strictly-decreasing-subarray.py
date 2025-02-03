class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def incrO(start,end,nums):
            for i in range(start+1,end+1):
                if nums[i]<=nums[i-1]:
                    return False
            return True
        def decrO(start,end,nums):
            for i in range(start+1,end+1):
                if nums[i]>=nums[i-1]:
                    return False
            return True
            
        res=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if incrO(i,j,nums) or decrO(i,j,nums):
                    res=max(res,j-i+1)
        return res
