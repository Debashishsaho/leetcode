class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini=nums[0]
        res=-1
        for i in range(1,len(nums)):
            if nums[i]>mini:
                res=max(res,abs(mini-nums[i]))
            else:
                mini=min(mini,nums[i])
            print(mini)
        return res