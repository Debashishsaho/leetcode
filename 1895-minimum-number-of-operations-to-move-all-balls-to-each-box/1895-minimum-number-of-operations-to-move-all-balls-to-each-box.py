class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        prefix_sum=[0]*n
        sufix_sum=[0]*n
        ans=[0]*n
        count=0
        for i in range(n):
            if count==0:
                prefix_sum[i]=0
                if boxes[i]=="1":
                    count+=1
                continue
            prefix_sum[i] += prefix_sum[i-1] + count
            if boxes[i]=="1":
                count+=1
        count=0
        for i in range(n-1,-1,-1):
            if count==0:
                sufix_sum[i]=0
                ans[i]=prefix_sum[i]+sufix_sum[i]
                if boxes[i]=="1":
                    count+=1
                continue
            sufix_sum[i] += sufix_sum[i+1] + count
            if boxes[i]=="1":
                count+=1
            ans[i]=prefix_sum[i]+sufix_sum[i]
        return ans