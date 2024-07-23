class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map={}
        for num in nums:
            hash_map[num] = hash_map.get(num,0)+1
        sorted_key=sorted(hash_map.items(),key=lambda item:(item[1],-item[0]))
        result=[]
        for num,freq in sorted_key:
            result.extend([num]*freq)
        return result