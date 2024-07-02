class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        hash_map=collections.Counter(nums1)
        res=[]
        for num in nums2:
            if hash_map[num] > 0:
                res.append(num)
                hash_map[num]-=1
        return res
