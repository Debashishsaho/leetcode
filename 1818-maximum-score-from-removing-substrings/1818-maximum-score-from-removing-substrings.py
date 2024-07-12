class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x<y:
            return self.maximumGain(s[::-1],y,x)
        stack_ab=[]
        stack_ba=[]
        total=0
        #ab
        for char in s:
            if char!='b':
                stack_ab.append(char)
            else:
                if stack_ab and stack_ab[-1]=='a':
                    stack_ab.pop()
                    total+=x
                else:
                    stack_ab.append(char)
        #ba
        while stack_ab:
            char=stack_ab.pop()
            if char!='b':
                stack_ba.append(char)
            else:
                if stack_ba and stack_ba[-1]=='a':
                    stack_ba.pop()
                    total+=y
                else:
                    stack_ba.append(char)
        return total

