class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_repeats = len(sequence) // len(word)
        for i in range(max_repeats, 0, -1):
            if sequence.count(word * i) > 0:
                return i
        return 0