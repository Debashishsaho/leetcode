class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li=[False]*n
        count=n
        fp=0
        while count>1:
            for _ in range(k):
                while li[fp%n]:
                    fp+=1
                fp+=1
            li[(fp-1)%n]=True
            count-=1
        fp=0
        while li[fp]:
            fp+=1
        return fp+1