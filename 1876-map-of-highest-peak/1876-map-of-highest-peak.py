class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        from collections import deque
        n, m = len(isWater), len(isWater[0])
        ans = [[-1]*m for i in range(n)]
        que = deque()
        for i, row in enumerate(isWater):
            for j,col in enumerate(row):
                if col:
                    que.append((i,j))
                    ans[i][j] = 0
        direction = [(-1,0),(0,1),(1,0),(0,-1)]
        while que:
            i, j = que.popleft()
            for a,b in direction:
                v1, v2 = i+a,j+b
                if (0 <= v1 < n) and (0 <= v2 < m) and ans[v1][v2]==-1:
                    ans[v1][v2] = ans[i][j]+1
                    que.append((v1,v2))
        return ans