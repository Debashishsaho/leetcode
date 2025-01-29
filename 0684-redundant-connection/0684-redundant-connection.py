class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        p = list(range(len(edges)+1))
        for a,b in edges:
            p_a=find(a)
            p_b=find(b)
            if p_a == p_b:
                return [a,b]
            p[p_a]=p_b
        return []