class Solution:
    def fractionAddition(self, expression: str) -> str:
        import re
        from fractions import Fraction
        pattern = r'([+-]?\d+)/(\d+)'
        matches = re.findall(pattern, expression)
        nums = [int(num) if i % 2 == 0 else int(den) for match in matches for i, (num, den) in enumerate(zip(match, match))]
        val = sum(Fraction(nums[i], nums[i+1]) for i in range(0, len(nums), 2))
        if val==0:
            return "0/1"
        elif val.denominator==1:
            return f"{val.numerator}/1"
        return str(val)
