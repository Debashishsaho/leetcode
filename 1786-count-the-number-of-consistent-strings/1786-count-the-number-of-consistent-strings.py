class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        flag=0
        for i in range(len(words)):
            chk=set(words[i])
            for char in chk:
                if char not in allowed:
                    flag=1
                    break
            if flag==0:
                count+=1
            else:
                flag=0
        return count