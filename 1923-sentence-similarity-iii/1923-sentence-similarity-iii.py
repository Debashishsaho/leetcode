class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        word1,word2=sentence1.split(),sentence2.split()
        n1,n2=len(word1),len(word2)
        if n1<n2:
            word1,word2=word2,word1
            n1,n2=n2,n1
        start=end=0
        while start<n2 and word1[start]==word2[start]:
            start+=1
        while end<n2 and word1[n1-1-end]==word2[n2-1-end]:
            end+=1
        return start+end>=n2
