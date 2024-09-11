class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xorO=start ^ goal
        return bin(xorO).count('1')