class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                increment=nums[i-1]-nums[i] +1
                nums[i] +=increment
                count+=increment
        return count