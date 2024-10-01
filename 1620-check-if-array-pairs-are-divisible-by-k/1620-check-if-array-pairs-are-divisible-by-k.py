class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hash_map={}
        for i in range(len(arr)):
            hash_map[arr[i]%k]=hash_map.get(arr[i]%k,0)+1
        if hash_map.get(0,0) % 2!=0:
            return False
        for i in range(1,k):
            if hash_map.get(i,0) != hash_map.get(k-i,0):
                return False
        return True