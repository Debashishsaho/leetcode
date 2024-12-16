class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        heapify(heap)
        for i in range(len(nums)):
            heappush(heap,(nums[i],i))
        for i in range(k):
            ele = heappop(heap)
            heappush(heap,(ele[0]*multiplier,ele[1]))
            nums[ele[1]]=ele[0]*multiplier
        return nums