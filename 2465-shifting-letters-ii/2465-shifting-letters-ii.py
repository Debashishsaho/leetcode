class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def shifting_char(char,shift):
            total_s = total_s = 'abcdefghijklmnopqrstuvwxyz'
            ind=total_s.index(char)
            new_index = (ind + shift) % 26
            return total_s[new_index]
        n = len(s)
        shift_accum = [0] * (n + 1)
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            shift_accum[start] += shift_value
            if end + 1 < n:
                shift_accum[end + 1] -= shift_value
        current_shift = 0
        result = []
        for i in range(n):
            current_shift += shift_accum[i]
            result.append(shifting_char(s[i], current_shift))
        
        return ''.join(result)