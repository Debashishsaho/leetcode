class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappush, heappop
        heapify(nums)
        count=0
        while len(nums)>1:
            x1=heappop(nums)
            x2=heappop(nums)
            # print(x1,x2)
            if x1>=k:
                return count
            heappush(nums,min(x1,x2)*2 + max(x1,x2))
            count+=1
        return count