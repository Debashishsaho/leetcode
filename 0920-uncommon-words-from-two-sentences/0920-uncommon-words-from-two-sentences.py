class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        li1=collections.Counter(s1.split(' '))
        li2=collections.Counter(s2.split(' '))
        res=[]
        for chars in li1:
            if li1[chars]==1 and chars not in li2:
                res.append(chars)
        for chars in li2:
            if li2[chars]==1 and chars not in li1:
                res.append(chars)
        return res    