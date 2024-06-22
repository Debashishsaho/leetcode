class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def oddCount(val):
            count=0
            res=0
            start=0
            end=0
            while end<len(nums):
                if nums[end]%2==1:
                    count+=1
                while count>val:
                    if nums[start]%2==1:
                        count-=1
                    start+=1
                res +=(end-start)+1
                end+=1
            return res
        return oddCount(k)-oddCount(k-1)