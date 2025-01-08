class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i,word in enumerate(words):
            for chk in words[i+1:]:
                count += chk.startswith(word) and chk.endswith(word)
        return count