class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0
        elif n == 3:
            return 1
        count = 1
        idx = 2
        prime_check = [True]*n
        prime_check[0] = prime_check[1] = False

        while(idx < n):
            if prime_check[idx]:
                multiple = 2
                while(idx*multiple < n):
                    prime_check[idx*multiple] = False
                    multiple += 1
            idx += 1
        return sum(prime_check)
