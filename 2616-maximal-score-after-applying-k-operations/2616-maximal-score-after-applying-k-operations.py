class Solution:
    import math
    def maxKelements(self, nums: List[int], k: int) -> int:
        score=0
        max_heap=[-num for num in nums]
        heapq.heapify(max_heap)
        for i in range(k):
            max_value=-heapq.heappop(max_heap)
            heapq.heappush(max_heap,-math.ceil(max_value/3))
            score += max_value
        return score