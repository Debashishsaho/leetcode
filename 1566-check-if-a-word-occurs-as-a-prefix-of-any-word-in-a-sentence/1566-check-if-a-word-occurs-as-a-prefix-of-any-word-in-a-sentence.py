class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        li=sentence.split(" ")
        mini=float("inf")
        n=len(searchWord)
        for i in range(len(li)):
            if searchWord==li[i][:n]:
                mini=min(mini,i)
        return -1 if mini==float("inf") else mini+1