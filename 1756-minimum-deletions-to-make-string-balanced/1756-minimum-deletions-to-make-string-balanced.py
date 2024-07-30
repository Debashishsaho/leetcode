class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack=[]
        count=0
        for i in range(len(s)):
            if s[i]=='b':
                stack.append('b')
            if stack and s[i]=='a':
                stack.pop()
                count+=1
        return count