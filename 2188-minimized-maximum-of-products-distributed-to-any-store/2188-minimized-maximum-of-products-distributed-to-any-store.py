class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l=1
        r=max(quantities)
        def cal(m):
            return sum((q-1)//m+1 for q in quantities)
        while l<r:
            mid=(l+r)//2
            if cal(mid)<=n:
                r=mid
            else:
                l=mid+1
        return l