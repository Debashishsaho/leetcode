class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        if n==1:
            return books[0][1]
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=books[0][1]
        for i in range(2,n+1):
            height=books[i-1][1]
            width=books[i-1][0]
            dp[i]=dp[i-1]+height
            j=i-1
            while j>0 and width<shelfWidth:
                width +=books[j-1][0]
                if (width>shelfWidth):
                    break
                height=max(height,books[j-1][1])
                dp[i]=min(dp[i],dp[j-1]+height)
                j -=1
        return dp[n]