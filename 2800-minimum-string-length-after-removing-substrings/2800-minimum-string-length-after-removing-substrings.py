class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        n=len(s)
        for i in range(len(s)):
            if stack and stack[-1]=='A' and s[i]=='B':
                stack.pop()
            elif stack and stack[-1]=='C' and s[i]=='D':
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)