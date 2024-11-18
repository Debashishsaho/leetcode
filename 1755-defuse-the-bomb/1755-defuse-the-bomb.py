class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length_of_code = len(code)
        # Initial answer list filled with zeros
        decrypted_code = [0] * length_of_code
      
        # If k is 0, the task is to return a list of the same length filled with zeros
        if k == 0:
            return decrypted_code
      
        # Create a prefix sum array with the code list repeated twice
        # 'initial=0' is to set the starting value of the accumulation to zero
        prefix_sum = list(accumulate(code + code, initial=0))
      
        # Iterate through each element in the code list to compute its decrypted value
        for i in range(length_of_code):
            if k > 0:
                # If k is positive, sum the next k values from the element's position
                decrypted_code[i] = prefix_sum[i + k + 1] - prefix_sum[i + 1]
            else:
                # If k is negative, sum the k values preceding the element's position
                decrypted_code[i] = prefix_sum[i + length_of_code] - prefix_sum[i + k + length_of_code]
        return decrypted_code