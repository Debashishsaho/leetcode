class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        val = derived[0]
        for i in range(1,len(derived)):
            val ^= derived[i]
        return False if val else True