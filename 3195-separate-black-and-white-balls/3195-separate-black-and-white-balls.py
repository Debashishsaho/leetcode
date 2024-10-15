class Solution:
    def minimumSteps(self, s: str) -> int:
        one_count=0
        n=len(s)
        res=0
        for i in range(n-1,-1,-1):
            if s[i]=="1":
                one_count+=1
                res += (n-i-1)-one_count+1
        return res
