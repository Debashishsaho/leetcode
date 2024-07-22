class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_map={}
        for i in range(len(names)):
            hash_map[heights[i]]=names[i]
        sorted_key=sorted(hash_map.keys(),reverse=True)
        li=[hash_map[key] for key in sorted_key]
        return li