class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for chars in details:
            age=int(chars[11]+chars[12])
            if age>60:
                count+=1
        return count