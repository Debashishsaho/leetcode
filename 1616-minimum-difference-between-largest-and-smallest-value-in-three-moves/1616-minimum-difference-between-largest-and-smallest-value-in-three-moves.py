class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=4:
            return 0
        nums.sort()
        mini=float('inf')
        for i in range(4):
            diff=nums[n-1-3+i]- nums[i]
            mini=min(mini,diff)
        return mini
