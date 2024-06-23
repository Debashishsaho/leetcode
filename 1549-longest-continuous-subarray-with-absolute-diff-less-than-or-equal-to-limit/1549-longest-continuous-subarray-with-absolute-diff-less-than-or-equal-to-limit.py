from sortedcontainers import SortedList
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sorted_list = SortedList()
        max_length = 0
        window_start = 0
        for window_end, value in enumerate(nums):
            sorted_list.add(value)
            while sorted_list[-1] - sorted_list[0] > limit:
                sorted_list.remove(nums[window_start])
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length