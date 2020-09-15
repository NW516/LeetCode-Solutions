class Solution:
    def countPrimes(self, n: int) -> int:
        # Uses the Sieve of Eratosthenes

        # Create array "prime[0..n]" and initialize
        # all entries to true. A value in prime[i] will 
        # become false if i is NOT a prime.
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):

            # If prime[p] is not changed, then it is a prime
            if (prime[p] == True):

                # Update all multiples of p (this is the sieve part!)
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0]= False
        if (n >= 1):
            prime[1]= False
        total = 0
        for p in range(n + 1):
            if (prime[p]) and (p != n):
                print(p)
                total += 1
        return(total)
