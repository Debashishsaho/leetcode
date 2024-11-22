class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        hash_map=collections.Counter(s)
        if any(hash_map[char]<k for char in 'abc'):
            return -1
        j=0
        n=len(s)
        maxi=-1
        for i in range(n):
            hash_map[s[i]] -=1
            while hash_map[s[i]]<k:
                hash_map[s[j]]+=1
                j+=1
            # print(i-j,i,j)
            maxi=max(maxi,i-j)
        return n-maxi-1