class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # hash_map={}
        # for num in mapping:
        #     hash_map[str(num)]=mapping[num]
        # res=[]
        # hash_map2={}
        # for num in nums:
        #     digit=0
        #     if num in hash_map2:
        #         hash_map2[num][1] +=1
        #     else:
        #         digit=0
        #         for val in str(num):
        #             digit=digit*10+hash_map[val]
        #         hash_map2[num]=[digit,1]
        # print(hash_map2)
        # sorted_hash=sorted(hash_map2.items(),key= lambda x:(x[1][0],-x[0]))
        # print(sorted_hash)
        # for key,(value,freq) in sorted_hash:
        #     res.extend([key]*freq)
        # return res
        mapped_with_index = []
        for index, num in enumerate(nums):
            mapped_num = mapping[0] if num == 0 else 0
            power_of_ten = 1
            while num:
                num, digit = divmod(num, 10)
                mapped_num = mapping[digit] * power_of_ten + mapped_num
                power_of_ten *= 10
            mapped_with_index.append((mapped_num, index))
        mapped_with_index.sort()
        return [nums[i] for _, i in mapped_with_index]