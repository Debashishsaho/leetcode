class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        sufix_sum = [0]*n
        sufix_sum[n-1] = nums[n-1]
        count=0
        prefix_sum=0
        for i in range(n-2,-1,-1):
            sufix_sum[i]= sufix_sum[i+1]+nums[i]
        for i in range(n-1):
            prefix_sum +=nums[i]
            if prefix_sum >= sufix_sum[i+1]:
                count+=1
        return count   