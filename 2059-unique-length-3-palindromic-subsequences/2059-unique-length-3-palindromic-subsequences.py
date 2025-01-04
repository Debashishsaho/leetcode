class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        from string import ascii_lowercase
        count=0
        for c in ascii_lowercase:
            l=s.find(c)
            r=s.rfind(c)
            if r - l > 1:
                count += len(set(s[l+1:r]))
        return count