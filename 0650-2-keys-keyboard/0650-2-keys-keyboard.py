class Solution:
    def minSteps(self, n: int) -> int:
        def isprime(n):
            val=0
            for i in range(2, (n//2)+1):
                if n % i == 0:
                    val=i
            if val==0:
                return True
            else:
                return val
        if n==1:
            return 0
        elif isprime(n)==True:
            return n
        dp=[0]*(n+1)
        dp[1]=0
        for i in range(2,n+1):
            if i<=5:
                dp[i]=i
            else:
                if isprime(i)==True:
                    dp[i]=i
                else:
                    ind=isprime(i)
                    dp[i]= dp[ind]+(i//ind)
        return dp[n]