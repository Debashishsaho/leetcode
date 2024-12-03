class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=[]
        prev=0
        for num in spaces:
            result.append(s[prev:num])
            result.append(" ")
            prev=num
        result.append(s[prev:])
        return "".join(result)