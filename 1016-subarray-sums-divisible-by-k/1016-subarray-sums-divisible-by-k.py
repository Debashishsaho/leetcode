class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        hash_map={}
        prevSum=0
        for i in range(len(nums)):
            prevSum +=nums[i]
            if prevSum%k==0:
                count+=1
            if (prevSum%k) in hash_map:
                count += hash_map[prevSum%k]
                hash_map[prevSum%k] +=1
            else:
                hash_map[prevSum%k]=1
        return count