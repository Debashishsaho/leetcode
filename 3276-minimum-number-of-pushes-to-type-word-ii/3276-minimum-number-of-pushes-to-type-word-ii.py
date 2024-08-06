class Solution:
    def minimumPushes(self, word: str) -> int:
        hash_map={}
        for char in word:
            hash_map[char]=hash_map.get(char,0)+1
        hash_sort=dict(sorted(hash_map.items(),key=lambda x:x[1],reverse=True))
        count=1
        pushes=0
        for key,val in hash_sort.items():
            if count<=8:
                pushes +=val
            elif count<=16:
                pushes += (val*2)
            elif count<=24:
                pushes += (val*3)
            else:
                pushes += (val*4)
            count +=1
        return pushes