class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash_map={5:0,10:0,20:0}
        for bill in bills:
            if bill==5:
                hash_map[bill]=hash_map.get(bill,0)+1
            elif bill==10:
                if hash_map and hash_map[5]>0:
                    hash_map[5]-=1
                    hash_map[bill]=hash_map.get(bill,0)+1
                else:
                    return False
            else:
                if hash_map and hash_map[5]>0:
                    if hash_map[10]>0:
                        hash_map[5]-=1
                        hash_map[10]-=1
                    elif hash_map[5]>=3:
                        hash_map[5]-=3
                    else:
                        return False
                    hash_map[bill]=hash_map.get(bill,0)+1
                else:
                    return False
        return True