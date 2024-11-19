class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        maxi=0
        seen=set()
        left=0
        current_sum=0
        for i in range(n):
            while nums[i] in seen or len(seen)==k:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left+=1
            current_sum +=nums[i]
            seen.add(nums[i])
            if len(seen)==k:
                maxi=max(maxi,current_sum)
        return maxi