class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hash_map = {}
        res=-1
        for i in range(len(nums)):
            val = nums[i]
            sume=0
            while val>0:
                sume += val%10
                val //=10
            if sume in hash_map:
                res=max(res,hash_map[sume]+nums[i])
                hash_map[sume] = max(nums[i],hash_map[sume])
            else:
                hash_map[sume] = nums[i]
        return res