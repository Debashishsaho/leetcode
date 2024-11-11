class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_sorted(a):
            return all(a[i] <= a[i + 1] for i in range(len(a) - 1))

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        max_num = max(nums)
        primes = [i for i in range(2, max_num) if is_prime(i)]
        
        prev = 0
        for num in nums:
            valid = False
            for p in reversed(primes):
                if num - p > prev:
                    num -= p
                    valid = True
                    break
            if not valid and num <= prev:
                return False
            prev = num
        
        return True