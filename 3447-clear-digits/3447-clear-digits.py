class Solution:
    def clearDigits(self, s: str) -> str:
        new_s=""
        for char in s:
            if char.isdigit():
                new_s = new_s[:-1]
                continue
            new_s +=char
        return new_s