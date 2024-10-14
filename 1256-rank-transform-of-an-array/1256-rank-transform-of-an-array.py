class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        numbers=sorted(arr)
        hash_map={}
        j=1
        hash_map[numbers[0]]=j
        n=len(numbers)
        for i in range(1,n):
            if numbers[i]==numbers[i-1]:
                continue
            else:
                hash_map[numbers[i]]=j+1
                j+=1
        for i in range(n):
            numbers[i]=hash_map[arr[i]]
        return numbers
