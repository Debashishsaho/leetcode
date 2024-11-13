class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        # print(nums)
        def countLess(sume):
            i=0
            j=len(nums)-1
            count=0
            while i<j:
                val=nums[i]+nums[j]
                if val>sume:
                    j-=1
                else:
                    count+=(j-i)
                    i+=1
            return count
        return countLess(upper)-countLess(lower-1)