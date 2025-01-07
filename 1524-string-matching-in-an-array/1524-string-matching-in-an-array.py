class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        val=set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if words[i] in words[j]:
                        val.add(words[i])
        return list(val)
