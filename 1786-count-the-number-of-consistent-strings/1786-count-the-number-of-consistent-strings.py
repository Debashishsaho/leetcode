class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowed_set=set(allowed)
        for word in words:
            if all(char in allowed_set for char in set(word)):
                count+=1
        return count