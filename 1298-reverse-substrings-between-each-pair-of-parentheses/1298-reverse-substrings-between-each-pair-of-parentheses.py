class Solution:
    def reverseParentheses(self, s: str) -> str:
        length_of_string = len(s)
        mapping = [0] * length_of_string
        stack = []
        for index, character in enumerate(s):
            if character == '(':
                stack.append(index)
            elif character == ')':
                opening_index = stack.pop()
                mapping[index], mapping[opening_index] = opening_index, index
        index = 0
        direction = 1
        result = []
        while index < length_of_string:
            print(direction)
            if s[index] in '()':
                index = mapping[index]
                direction = -direction
            else:
                result.append(s[index])
            index += direction
        return ''.join(result)