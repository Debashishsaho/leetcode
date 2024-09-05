class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        sume=(mean*(n+m))-sum(rolls)
        if sume<0:
            return []
        quotient=sume//n
        reminder=sume%n
        if (quotient>6 and reminder>=0) or (quotient>=6 and reminder>0) or quotient<=0:
            return []
        combination=[quotient]*n
        print(combination,reminder)
        for i in range(reminder):
            combination[i] +=1
        return combination