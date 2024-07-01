class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_repeats = len(sequence) // len(word)
        for i in range(max_repeats, -1, -1):
            if word*i in sequence:
                return i