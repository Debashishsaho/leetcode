class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)
        val=1
        count=0
        for i in range(1,n):
            if s[i]!=s[i-1] and val%2!=0:
                val=0
                count+=1
            elif s[i]!=s[i-1] and val%2==0:
                val=1
            else:
                val+=1
        return count