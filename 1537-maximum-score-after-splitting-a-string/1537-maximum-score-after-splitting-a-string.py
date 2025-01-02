class Solution:
    def maxScore(self, s: str) -> int:
        counts=s.count('1')
        if counts==0:
            return 1
        maxi=0
        zero=0
        for i in range(len(s)-1):
            if s[i]=='0':
                zero+=1
            else:
                counts -=1
            maxi=max(maxi,zero+counts)
        return maxi