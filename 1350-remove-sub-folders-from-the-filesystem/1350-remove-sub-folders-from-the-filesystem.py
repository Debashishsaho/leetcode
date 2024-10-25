class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        li=[]
        folder.sort()
        li.append(folder[0])
        for i in range(1,len(folder)):
            m,n=len(li[-1]),len(folder[i])
            if m>=n or not (folder[i][:m]==li[-1] and folder[i][m]=="/"):
                li.append(folder[i])
        return li