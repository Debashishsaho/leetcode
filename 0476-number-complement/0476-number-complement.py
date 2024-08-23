class Solution:
    def findComplement(self, num: int) -> int:
        index=0
        res=0
        while num>0:
            if (num&1)==0:
                res +=(2**index)*1
            index+=1
            num=(num>>1)
        return res   