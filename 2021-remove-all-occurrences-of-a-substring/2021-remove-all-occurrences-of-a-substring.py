class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n=len(s)
        k=len(part)

        stack = ['']*n
        j=0
        for i,c in enumerate(s):
            stack[j]=c
            j+=1
            if j>=k and ''.join(stack[j-k:j])==part:
                j -=k
        return ''.join(stack[:j])
