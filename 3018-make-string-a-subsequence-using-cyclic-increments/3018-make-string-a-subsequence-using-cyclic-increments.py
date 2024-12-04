class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ind=0
        for char in str1:
            next_char = "a" if char=="z" else chr(ord(char)+1)

            if ind<len(str2):
                if str2[ind] in [char,next_char]:
                    ind+=1
        return ind==len(str2)