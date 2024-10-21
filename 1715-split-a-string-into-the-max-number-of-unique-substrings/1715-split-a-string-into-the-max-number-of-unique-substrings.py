class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start,seen):
            if start==len(s):
                return 0
            max_limit=0
            for i in range(start+1,len(s)+1):
                sub_string=s[start:i]
                if sub_string not in seen:
                    seen.add(sub_string)
                    max_limit=max(max_limit,1+backtrack(i,seen))
                    seen.remove(sub_string)
            return max_limit
        return backtrack(0,set())