class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        while start>0 and goal>0:
            st=0 if start & 1==0 else 1
            go=0 if goal & 1==0 else 1
            if st^go!=0:
                count+=1
            start >>=1
            goal >>=1
        while start>0:
            st=0 if start & 1==0 else 1
            if st!=0:
                count+=1   
            start >>=1
        while goal>0:
            go=0 if goal & 1==0 else 1
            if go!=0:
                count+=1
            goal >>=1
        return count