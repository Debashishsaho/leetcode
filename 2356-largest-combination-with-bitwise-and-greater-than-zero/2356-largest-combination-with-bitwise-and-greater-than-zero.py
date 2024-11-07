class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count=0
        for bit_set in range(32):
            count_set=0
            for num in candidates:
                if (num >> bit_set) & 1:
                    count_set +=1
            count = max(count,count_set)
        return count