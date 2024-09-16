from datetime import datetime
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        formater="%H:%M"
        n=len(timePoints)
        diff=float('inf')
        li=[]  
        for time in timePoints:
            dt=datetime.strptime(time,formater)
            hour=dt.hour
            minute=dt.minute
            li.append([hour,minute])
        li=sorted(li,key=lambda x:(x[0],x[1]))
        total_min=24*60
        print(li)
        for i in range(n-1):
            val1=li[i][0]*60+li[i][1]
            val2=li[i+1][0]*60+li[i+1][1]
            diff=min(diff,abs(val2-val1))
            # print(diff,"diff")
        val1 = li[0][0] * 60 + li[0][1]
        val2 = li[-1][0] * 60 + li[-1][1]
        diff = min(diff, total_min - abs(val2 - val1))
        return diff