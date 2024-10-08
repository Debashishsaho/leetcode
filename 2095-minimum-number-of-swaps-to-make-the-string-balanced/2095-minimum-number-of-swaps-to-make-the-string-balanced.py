class Solution:
    def minSwaps(self, s: str) -> int:
        count=0
        for b in s:
            if b=="[":
                count+=1
            elif count>0:
                count -=1
        return (count+1)//2