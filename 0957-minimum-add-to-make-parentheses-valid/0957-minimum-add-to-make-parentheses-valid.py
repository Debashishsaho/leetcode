class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count=0
        imblance=0
        for b in s:
            if b=="(":
                open_count +=1
            elif open_count>0 and b==")":
                open_count -=1
            else:
                imblance +=1
        return open_count+imblance
