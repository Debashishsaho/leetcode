class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total=sum(chalk)
        k%=total
        for i,amt in enumerate(chalk):
            if k<amt:
                return i
            k-=amt
        return -1