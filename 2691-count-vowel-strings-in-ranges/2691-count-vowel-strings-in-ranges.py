class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        count=[0]*(n+1)
        vowels={'a','e','i','o','u'}
        for i in range(n):
            is_vowel=words[i][0] in vowels and words[i][-1] in vowels
            count[i+1] = count[i]+ (1 if is_vowel else 0)
        res=[]
        for start,end in queries:
            res.append(count[end+1]-count[start])
        return res
