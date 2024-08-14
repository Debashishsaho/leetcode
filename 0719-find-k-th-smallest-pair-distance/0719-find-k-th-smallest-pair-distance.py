class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs_with_max_distance(dist):
            count = 0
            for i, upper_bound in enumerate(nums):
                lower_bound = upper_bound - dist
                insertion_point = bisect_left(nums, lower_bound, 0, i)
                count += i - insertion_point
            return count

        nums.sort()
        max_possible_distance = nums[-1] - nums[0]
        smallest_distance = bisect_left(range(max_possible_distance + 1), k,        key=count_pairs_with_max_distance)
        return smallest_distance