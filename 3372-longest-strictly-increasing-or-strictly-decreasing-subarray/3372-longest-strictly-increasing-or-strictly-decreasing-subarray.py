class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        longest_subarray = 1
        current_length = 1
        increasing = nums[1] > nums[0]
        
        for i in range(1, len(nums)):
            if (increasing and nums[i] >= nums[i - 1]) or (not increasing and nums[i] <= nums[i - 1]):
                current_length += 1
                longest_subarray = max(longest_subarray, current_length)
            else:
                current_length = 2
                increasing = not increasing
        
        return longest_subarray
