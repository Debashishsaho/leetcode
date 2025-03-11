class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        end = 0 
        start = 0
        n=len(s)
        hash_map = {'a':0,'b':0,'c':0}
        flag = 0
        count=0
        while end<n:
            if flag==0:
                hash_map[s[end]] +=1
            if hash_map['a']>0 and hash_map['b']>0 and hash_map['c']>0:
                count += n - end
                hash_map[s[start]] -= 1
                start +=1
                flag=1
            else:
                flag=0
                end +=1
        return count
