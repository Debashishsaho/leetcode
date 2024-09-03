class Solution:
    def getLucky(self, s: str, k: int) -> int:
        char=""
        for num in s:
            char += str(ord(num)-97+1)
        value=int(char)
        while k>0:
            chk=0
            while value>0:
                digit=value%10
                chk +=digit
                value //=10
            value=chk
            k-=1
        return value